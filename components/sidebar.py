import streamlit as st

def render_sidebar():
    st.sidebar.markdown("## \n")
    st.sidebar.image('assets/logo.svg', width=48)
    st.sidebar.markdown("# Student Performance")
    st.sidebar.markdown("<small class='muted'>AI Analytics Platform</small>", unsafe_allow_html=True)

    menu = [
        'Home', 'Data Explorer', 'EDA', 'Model Training', 'Prediction Center', 'Explainable AI', 'Reports'
    ]
    icons = ['🏠','📂','📊','🤖','🔮','🔍','📄']

    choice = st.sidebar.radio("Navigation", menu, format_func=lambda x: f"{icons[menu.index(x)]} {x}")
    return choice

