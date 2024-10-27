# Basis-Image festlegen
# es reicht hier ein kleines Python-Image zu wählen
FROM python:slim

# Gegebenenfalls den Port ändern
# ENV FLASK_RUN_PORT=80

# Neues Arbeitsverzeichnis anlegen
WORKDIR /app

# Dependencies installieren
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py .

ENTRYPOINT ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000