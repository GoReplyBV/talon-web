#syntax=docker/dockerfile:1.4

FROM python:3.10-slim-bullseye AS compile-image

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY --link talon talon
RUN pip install --user ./talon

COPY --link requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.10-slim-bullseye

COPY --link --from=compile-image /root/.local /root/.local

COPY --link app.py .
COPY --link healthcheck.py .

ENV PATH=/root/.local/bin:$PATH

HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD ["python", "healthcheck.py"]

ENTRYPOINT ["gunicorn", "app:app", "--bind=0.0.0.0:5000", "--log-level=debug", "--workers=4"]
