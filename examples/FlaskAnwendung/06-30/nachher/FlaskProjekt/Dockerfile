FROM python:3.8

WORKDIR /app

# COPY src/requirements.txt .
# COPY src/app.py .

COPY src/* .

RUN pip3 install -r requirements.txt

EXPOSE 80

ENV FLASK_RUN_PORT=80
ENV FLASK_APP=app

CMD ["flask", "run", "--host=0.0.0.0"]
