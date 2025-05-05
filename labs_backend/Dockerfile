FROM python:3.11-slim

WORKDIR /labs_api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /labs_api/app
COPY ./labs_src /labs_api/labs_src

ENV PYTHONPATH=/labs_api

EXPOSE 8000

CMD ["uvicorn", "app.core.main:app", "--host", "0.0.0.0", "--port", "8000"]