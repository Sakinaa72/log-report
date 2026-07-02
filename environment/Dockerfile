
FROM python:3.12-slim@sha256:2ea4d6f8d2c11b0a2aa12be3d2fc06339315138f5116cfd2e662c5325b0ef23b

RUN pip install --no-cache-dir \
    pytest==8.4.1 \
    pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
