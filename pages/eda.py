import streamlit as st
try:
    import plotly.express as px
    import plotly.figure_factory as ff
    PLOTLY_AVAILABLE = True
except Exception:
    px = None
    ff = None
    PLOTLY_AVAILABLE = False
from utils.data import load_dataset, preprocess
import pandas as pd

def render_eda():
    st.header('Exploratory Data Analysis')
    df = load_dataset()
    _, _, _, _, meta = preprocess(df)
    for w in meta.get('warnings', []):
        st.warning(w)

    st.subheader('Correlation Heatmap')
    corr = df.select_dtypes(include=['number']).corr()
    if PLOTLY_AVAILABLE:
        fig = px.imshow(corr, color_continuous_scale='Turbo')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning('Plotly not available — skipping heatmap')

    st.subheader('Feature Distributions')
    numeric_cols = meta.get('numeric_cols', [])
    if not numeric_cols:
        st.info('No numeric columns found for distribution plots.')
        return
    cols = st.multiselect('Select numeric features', numeric_cols, default=[numeric_cols[0]])
    for c in cols:
        if PLOTLY_AVAILABLE:
            fig = px.histogram(df, x=c, color='performance', barmode='overlay')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write(df[[c, 'performance']].groupby('performance')[c].plot(kind='hist'))

    st.subheader('Pairplot (sample)')
    sample = df.sample(min(200, len(df)))
    if PLOTLY_AVAILABLE:
        fig = px.scatter_matrix(sample, dimensions=numeric_cols[:3], color='performance')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info('Plotly not available — skipping scatter matrix')
