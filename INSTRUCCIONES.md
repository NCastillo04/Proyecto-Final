py -m venv .venv
.venv\Scripts\activate
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\pip install -e .
.\.venv\Scripts\python -m playwright install chromium
.\.venv\Scripts\python -m pip install pytest-html

.\.venv\Scripts\python -m pytest --html=report.html --self-contained-html
