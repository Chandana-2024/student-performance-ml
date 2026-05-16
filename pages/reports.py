import streamlit as st
import joblib
from utils.data import load_dataset, preprocess
from utils.models import train_all

def render_reports():
    st.header('Reports & Exports')
    df = load_dataset()
    X, y, preprocessor, label_encoder, meta = preprocess(df)
    for w in meta.get('warnings', []):
        st.warning(w)

    if st.button('Train and Export Best Model'):
        models = train_all(X, y)
        # simplistic best = first
        best = list(models.items())[0]
        name, model = best
        joblib.dump(model, f'models/{name}.pkl')
        st.success(f'Model {name} saved to models/{name}.pkl')
        with open(f'models/{name}.pkl','rb') as f:
            st.download_button('Download model', f, file_name=f'{name}.pkl')
