FROM python:3.9.7

COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
