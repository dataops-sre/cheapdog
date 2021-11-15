FROM python:3.9-alpine

COPY app/requirements.txt /opt/process.fake_datadog/requirements.txt

RUN apk update && \
    apk add python3-dev gcc g++ musl-dev libstdc++ && \
    pip install -r /opt/process.fake_datadog/requirements.txt && \
    apk del python3-dev gcc g++ musl-dev && \
    rm -rf /var/cache/apk/*

COPY app /opt/process.fake_datadog

ENV prometheus_multiproc_dir "/var/lib/prometheus"

CMD ["gunicorn", "--bind", "0.0.0.0:80", "--pythonpath", "/opt/process.fake_datadog", "api:app"]
