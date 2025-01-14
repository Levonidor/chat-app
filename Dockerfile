FROM python:3.9-slim

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir aiogram==3.7 python-dotenv==0.19.2

EXPOSE 80

CMD ["python", "main.py"]
