FROM python:3.10-alpine3.19

WORKDIR /app

ENV PYTHONPATH=/app

EXPOSE 8000

RUN apk add --no-cache openssl && \
    pip install --upgrade pip

COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

COPY . .

COPY /entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]