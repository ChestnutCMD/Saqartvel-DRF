FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY /Saqartvel .
COPY .envs :/app/.env

ENTRYPOINT ["bash", "/app/entrypoint.sh"]
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]