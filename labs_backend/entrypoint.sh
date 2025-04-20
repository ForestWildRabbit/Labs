#!/bin/sh
set -e

alembic_result=$(alembic current)

if [ -z "$alembic_result" ]; then
  echo "No migrations found. Creating an initial migration..."
  alembic revision --autogenerate -m "Initial migration"
else
  echo "Migrations already exist. Skipping migration creation."
fi

echo "Applying any pending migrations..."
alembic upgrade head

uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000