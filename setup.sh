#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

echo "Installation complete. Create and activate a venv before running this script for best results."

echo "Run the app:"
echo "  streamlit run app.py"
