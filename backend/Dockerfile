FROM python:3.11-slim

WORKDIR /backend

COPY ./app /backend/app
COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt
# RUN cd app/database && alembic revision --autogenerate

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]