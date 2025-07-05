FROM python:latest

WORKDIR /flask

COPY . .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000