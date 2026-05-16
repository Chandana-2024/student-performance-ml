import streamlit as st
import pandas as pd
from utils.data import load_dataset
try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except Exception:
    px = None
    PLOTLY_AVAILABLE = False

def render_data_explorer():
    st.header('Data Explorer')
    df = load_dataset()

    if st.checkbox('Show raw data'):
        st.dataframe(df)

    st.subheader('Null values')
    nulls = df.isnull().sum()
    if PLOTLY_AVAILABLE:
        fig = px.bar(x=nulls.index, y=nulls.values, labels={'x':'Column','y':'Null Count'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.bar_chart(nulls)

    st.subheader('Statistics')
    st.dataframe(df.describe())
