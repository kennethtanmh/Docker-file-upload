FROM python:3.10

WORKDIR /backend

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 4000

CMD python ./main.py