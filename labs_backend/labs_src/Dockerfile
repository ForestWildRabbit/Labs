FROM python:3.11-slim

WORKDIR /labs_src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY __init__.py .
COPY .env .
COPY ./app /labs_src/app

ENV PYTHONPATH=/labs_src

EXPOSE 8001

CMD ["uvicorn", "app.core.main:app", "--host", "0.0.0.0", "--port", "8001"]

