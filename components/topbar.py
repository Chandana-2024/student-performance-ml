import streamlit as st

def render_topbar():
    cols = st.columns([1,6,1])
    with cols[0]:
        st.markdown("<div class='brand'>🚀</div>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown("<h1 class='title'>Student Performance Analytics</h1>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown("<div style='text-align:right'>v1.0</div>", unsafe_allow_html=True)
