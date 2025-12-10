# Segregate Project

Short description:
A small ETL script that reads a CSV of app reviews, cleans and segregates records into "good" and "bad" outputs.

Prerequisites:
- Python 3.8+
- pip

Quick setup (PowerShell):
```powershell
cd path
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

Run:
```powershell
python .\segregate_records.py
```

Notes:
- Keep original datasets in a local `data/` directory (excluded by .gitignore).
- Outputs are written to `output/` (excluded).
- Add data validation or tests before productionizing.

License: MIT