import streamlit as st
from utils.data import load_dataset, preprocess
from utils.models import train_all

def render_explainable():
    st.header('Explainable AI')
    df = load_dataset()
    X, y, preprocessor, label_encoder, meta = preprocess(df)
    for w in meta.get('warnings', []):
        st.warning(w)
    models = train_all(X, y)

    st.write('Select a model to view SHAP explanations (if available)')
    model_choice = st.selectbox('Model', list(models.keys()))
    model = models[model_choice]

    try:
        import shap
        explainer = shap.Explainer(model.predict, X)
        shap_values = explainer(X[:50])
        st.subheader('SHAP Summary (sample)')
        st.pyplot(shap.plots.beeswarm(shap_values, show=False))
    except Exception as e:
        st.error('SHAP not available or model incompatible: ' + str(e))
