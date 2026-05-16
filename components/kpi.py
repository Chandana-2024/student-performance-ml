import streamlit as st

def kpi(title, value, delta=None, icon=None):
    html = f"""
    <div class='kpi'>
      <div class='kpi-title'>{icon or ''} {title}</div>
      <div class='kpi-value'>{value}</div>
      <div class='kpi-delta'>{delta or ''}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
