FROM python:3.12.7

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn pydantic openai

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
