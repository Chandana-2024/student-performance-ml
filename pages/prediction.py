import streamlit as st
import pandas as pd
from utils.data import load_dataset, preprocess
from utils.models import train_all
from utils.persistence import list_models, load_model

def render_prediction():
    st.header('Prediction Center')
    df = load_dataset()
    X, y, preprocessor, label_encoder, meta = preprocess(df)
    for w in meta.get('warnings', []):
        st.warning(w)

    # try to load persisted models first
    saved = list_models()
    models = {}
    if saved:
        st.info('Found saved models; loading...')
        for s in saved:
            try:
                models[s] = load_model(s)
            except Exception:
                continue
    else:
        # train models if none saved
        models = train_all(X, y)

    st.subheader('Single Prediction')
    cols = st.columns(3)
    cat_vals = meta.get('categorical_values', {})
    with cols[0]:
        gender = st.selectbox('Gender', cat_vals.get('gender', []))
        race = st.selectbox('Race/Ethnicity', cat_vals.get('race/ethnicity', []))
    with cols[1]:
        parent = st.selectbox('Parental Level', cat_vals.get('parental level of education', []))
        lunch = st.selectbox('Lunch', cat_vals.get('lunch', []))
    with cols[2]:
        prep = st.selectbox('Test Prep', cat_vals.get('test preparation course', []))
        math = st.number_input('Math', 0, 100, 50)
        reading = st.number_input('Reading', 0, 100, 50)
        writing = st.number_input('Writing', 0, 100, 50)

    model_choice = st.selectbox('Model', list(models.keys()))
    if st.button('Predict'):
        row = {
            'gender': gender,
            'race/ethnicity': race,
            'parental level of education': parent,
            'lunch': lunch,
            'test preparation course': prep,
            'math score': math,
            'reading score': reading,
            'writing score': writing,
        }
        X_single = pd.DataFrame([row])
        try:
            X_single_t = preprocessor.transform(X_single)
            pred = models[model_choice].predict(X_single_t)[0]
            label = label_encoder.inverse_transform([pred])[0]
            st.success(f'Predicted: {label}')
        except Exception as e:
            st.error(f'Prediction failed: {e}')

    st.markdown('---')
    st.subheader('Batch Prediction (CSV)')
    uploaded = st.file_uploader('Upload CSV', type=['csv'])
    if uploaded is not None:
        df_in = pd.read_csv(uploaded)
        st.write('Preview:')
        st.dataframe(df_in.head())
        if st.button('Run Batch Predict'):
            st.info('Running predictions...')
            # naive: assume same columns
            missing = [c for c in meta.get('feature_cols', []) if c not in df_in.columns]
            if missing:
                st.error(f"Missing columns in upload: {', '.join(missing)}")
            else:
                try:
                    X_batch = preprocessor.transform(df_in[meta.get('feature_cols', [])])
                    preds = models[list(models.keys())[0]].predict(X_batch)
                    df_in['prediction'] = label_encoder.inverse_transform(preds)
                    st.download_button('Download predictions', df_in.to_csv(index=False).encode(), file_name='predictions.csv')
                except Exception as e:
                    st.error(f'Batch prediction failed: {e}')
