import streamlit as st
from utils.data import load_dataset, preprocess
from utils.models import train_all, get_model_constructors
from utils.persistence import save_model, list_models
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, f1_score, roc_curve, roc_auc_score, precision_recall_curve, average_precision_score
from sklearn.decomposition import PCA
import pandas as pd
try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except Exception:
    go = None
    px = None
    PLOTLY_AVAILABLE = False

def render_model_training():
    st.header('Model Training')
    df = load_dataset()
    X, y, preprocessor, label_encoder, meta = preprocess(df)
    for w in meta.get('warnings', []):
        st.warning(w)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if st.button('Train All Models'):
        with st.spinner('Training models...'):
            models = train_all(X_train, y_train)
        # evaluate
        rows = []
        for name, m in models.items():
            y_pred = m.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred, average='weighted')
            rows.append({'model':name,'accuracy':acc,'f1':f1})
        dfm = pd.DataFrame(rows).sort_values('accuracy', ascending=False)
        st.subheader('Model Leaderboard')
        st.table(dfm)
        st.success('Training complete')

        # offer to save best model
        best_name = dfm.iloc[0]['model']
        if st.button(f"Save best model: {best_name}"):
            save_model(best_name, models[best_name])
            st.success(f"Saved model '{best_name}' to models/")

        # ROC/PR plots (binary only)
        if len(y_test.unique()) == 2:
            if PLOTLY_AVAILABLE:
                fig_roc = go.Figure()
                fig_pr = go.Figure()
                for name, m in models.items():
                    try:
                        prob = m.predict_proba(X_test)[:,1]
                    except Exception:
                        continue
                    fpr, tpr, _ = roc_curve(y_test, prob)
                    auc = roc_auc_score(y_test, prob)
                    fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, name=f"{name} (AUC={auc:.2f})"))
                    prec, rec, _ = precision_recall_curve(y_test, prob)
                    ap = average_precision_score(y_test, prob)
                    fig_pr.add_trace(go.Scatter(x=rec, y=prec, name=f"{name} (AP={ap:.2f})"))
                fig_roc.update_layout(title='ROC Curves', xaxis_title='FPR', yaxis_title='TPR')
                fig_pr.update_layout(title='Precision-Recall Curves', xaxis_title='Recall', yaxis_title='Precision')
                st.plotly_chart(fig_roc, use_container_width=True)
                st.plotly_chart(fig_pr, use_container_width=True)
            else:
                st.warning('ROC/PR plotting requires Plotly; install it to view these charts.')
        else:
            st.info('ROC/PR plots require binary target — skipping for multiclass')

        # PCA 2D visualization
        try:
            pca = PCA(n_components=2)
            X_proj = pca.fit_transform(X_test)
            best = models[dfm.iloc[0]['model']]
            y_pred_best = best.predict(X_test)
            dfp = pd.DataFrame({'PC1': X_proj[:,0], 'PC2': X_proj[:,1], 'true': y_test, 'pred': y_pred_best})
            if PLOTLY_AVAILABLE:
                fig = px.scatter(dfp, x='PC1', y='PC2', color='true', symbol='pred', title='PCA 2D: true vs predicted (best model)')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info('Plotly not available — skipping PCA scatterplot')
        except Exception:
            st.info('PCA visualization failed (possibly due to categorical features after encoding).')

    st.markdown('---')
    st.subheader('Quick Train (single model)')
    choice = st.selectbox('Choose model', list(get_model_constructors().keys()))
    if st.button('Train Selected'):
        ctor = get_model_constructors()[choice]
        model = ctor()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')
        st.write('Accuracy:', acc)
        st.write('F1 score:', f1)
        if st.button(f"Save '{choice}' model"):
            save_model(choice, model)
            st.success(f"Saved model '{choice}' to models/")
