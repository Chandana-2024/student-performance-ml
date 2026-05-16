import os
from pathlib import Path
import streamlit as st
from components.sidebar import render_sidebar
from components.topbar import render_topbar

# Ensure working directory is the project root so relative asset paths resolve
base_dir = Path(__file__).resolve().parent
os.chdir(base_dir)

st.set_page_config(page_title='Student Performance Analytics', layout='wide')


def main():
    # startup checks
    try:
        from utils.startup import verify_startup
        info = verify_startup()
    except Exception:
        info = {'missing_packages': [], 'dataset_path': None, 'models_dir': None, 'install_cmd': 'python -m pip install -r requirements.txt'}

    if info.get('missing_packages'):
        st.error('Missing Python packages: ' + ', '.join(info['missing_packages']))
        st.info(f"Install with: {info.get('install_cmd')}")
        return

    # inject custom css
    css_path = base_dir / 'styles' / 'main.css'
    if css_path.exists():
        try:
            with open(css_path) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        except Exception:
            st.warning('Unable to apply custom CSS; continuing without it.')
    else:
        st.info('No custom CSS found; continuing with default Streamlit theme.')

    # Top navbar
    render_topbar()

    # Sidebar navigation
    page = render_sidebar()

    # Page routing
    if page == 'Home':
        from pages.home import render_home
        render_home()
    elif page == 'Data Explorer':
        from pages.data_explorer import render_data_explorer
        render_data_explorer()
    elif page == 'EDA':
        from pages.eda import render_eda
        render_eda()
    elif page == 'Model Training':
        from pages.model_training import render_model_training
        render_model_training()
    elif page == 'Prediction Center':
        from pages.prediction import render_prediction
        render_prediction()
    elif page == 'Explainable AI':
        from pages.explainable_ai import render_explainable
        render_explainable()
    elif page == 'Reports':
        from pages.reports import render_reports
        render_reports()


if __name__ == '__main__':
    main()
    # end of router
