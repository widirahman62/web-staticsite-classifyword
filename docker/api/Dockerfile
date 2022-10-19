FROM python:3.7

WORKDIR /usr/src/server
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8081"]
