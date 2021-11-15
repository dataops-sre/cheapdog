FROM python:3.9-alpine

COPY app/requirements.txt /opt/fake_datadog/requirements.txt

RUN apk update && \
    apk add python3-dev gcc g++ musl-dev libstdc++ && \
    pip install -r /opt/fake_datadog/requirements.txt && \
    apk del python3-dev gcc g++ musl-dev && \
    rm -rf /var/cache/apk/*

#COPY app /opt/fake_datadog
VOLUME /opt/fake_datadog/recorded
#CMD ["gunicorn", "--bind", "0.0.0.0:80", "--pythonpath", "/opt/fake_datadog", "api:app"]
CMD ["python", "/opt/fake_datadog/api.py"]
