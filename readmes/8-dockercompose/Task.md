## Aufgabe 1: (Flask-Redis-App)

* Ziel von diesem Projekt ist es eine Webanwendung bestehend
aus Frontend (Flask) und Backend (Redis) sowie Proxy-Server
mit Hilfe von **docker-compose** auszuführen
  * Die prinzipielle Vorgehensweise kann man auf eine Vielzahl 
  von ähnlichen Anwendungsfällen übertragen!
* Das Projekt wird in den Kursmaterialien zur Verfügung gestellt.
  * Die Flask-Anwendung ist mit einer Redis-Datenbank verbunden, in der die
  Seitenaufrufe gezählt werden
  * Die Flask-Anwendung enthält Unterseiten (*/visit* und *visits/reset*), wofür
  Nginx bereits entsprechend konfiguriert worden ist


### Aufgabe 1: (Flask-Redis-App)

**Anleitung:**
* Schreibe die *compose.yaml*, in der du drei Services definierst: Frontend, 
Backend und Proxy-Server
  * Für deinen Backend-Service verwendest du das Standard-Redis-Image, bei 
  den anderen beiden Services nutzt du deine anhand der beiden Dockerfiles 
  gebauten Images
  * Damit sich alle Container richtig verbinden können und deine Anwendung
  auch wirklich läuft, ist es entscheidend deinen Frontend- und deinen 
  Backend-Service richtig zu benennen:
    * Den Namen vom Frontend-Service kannst du aus der *nginx-proxy/nginx.conf* erschließen
    Den Name vom Backend-Service kannst du aus der *flask-app/app.py* erschließen