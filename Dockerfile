FROM python:3.9-slim

WORKDIR /scripts

COPY requirements.txt /scripts/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./scripts /scripts

CMD ["python", "record_call.py"]
