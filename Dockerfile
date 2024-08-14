FROM python:3.12-slim

WORKDIR /app
COPY . /app

ENV TERM=xterm-256color

CMD ["python", "main.py"]