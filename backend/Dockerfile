FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# VOLUME [ "/app/data" ]

EXPOSE 5000

CMD ["python3", "-m", "flask", "--app", "main.py", "run" , "--host=0.0.0.0" ,"--port=5000"]