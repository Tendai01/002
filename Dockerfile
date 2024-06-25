FROM python:3.9-slim
WORKDIR /app
COPY populacao.py .

CMD ["python", "populacao.py"]
