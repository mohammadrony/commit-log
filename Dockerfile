FROM python:3.12-slim

WORKDIR /

COPY main.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
