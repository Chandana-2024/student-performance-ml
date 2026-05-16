@echo off
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
echo Installation complete.
echo Run the app with: streamlit run app.py
