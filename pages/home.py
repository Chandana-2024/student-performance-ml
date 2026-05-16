import streamlit as st
import pandas as pd
from components.kpi import kpi
from utils.data import load_dataset
try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except Exception:
    px = None
    PLOTLY_AVAILABLE = False

def render_home():
    st.header('Overview')
    df = load_dataset()

    cols = st.columns(3)
    with cols[0]:
        kpi('Records', f"{df.shape[0]}", icon='📄')
    with cols[1]:
        kpi('Features', f"{df.shape[1]}", icon='⚙️')
    with cols[2]:
        kpi('Classes', f"{df['performance'].nunique()}", icon='🎯')

    st.markdown('---')

    st.subheader('Class distribution')
    if PLOTLY_AVAILABLE:
        fig = px.pie(df, names='performance', hole=0.4, color_discrete_sequence=px.colors.sequential.Blues)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning('Plotly not available — showing table instead')
        st.dataframe(df['performance'].value_counts())
