## Docker

* Die Firma <b>Docker, Inc</b> hat ein Industrie-Standart für solche Container etabliert
* <b>Docker</> ist die Standart-Container-Software
* Docker selbst ist freie Software und als Open-Source verfügbar
* Docker Desktop(die Benutzeroberfläche und ggf. der Zugang zu Dockerhub) 
ist aber nicht frei, ggf. sind Lizenzgebühren fällig (z.B. für größere Unternehmen)

### Hinwies:

Hinweis [Windows]: WSL2 Installation is incomplete
Hallo liebe(r) Teilnehmer(in),

in der nächsten Lektion werden wir Docker Desktop bei dir installieren. 
Ein kleiner Hinweis für Windows-Nutzer:

Es kann passieren, dass beim ersten Start von Docker Desktop eine Fehlermeldung angezeigt wird:


In dem Fall musst du noch ein Update für den Linux-Kernel installieren, 
der vom Windows Subsystem for Linux mitgeliefert wurde. Du musst in diesem Fall den Anweisungen in diesem Hinweis folgen, d.h. du musst https://aka.ms/wsl2kernel aufrufen.

Dein Browser sollte auf der Seite schon auf den richtigen Schritt 
gesprungen sein, bei mir ist das zum aktuellen Zeitpunkt "Schritt 4". Die anderen Schritte sind für uns nicht relevant.

Lade dir dort ein Update für das Windows Subsystem for Linux herunter 
(eine .msi-Datei), und führe diese Datei aus. Klicke dich durch diesen 
Installationsassistenten, und klicke anschließend in Docker Desktop auf 
"Restart". Damit wird Docker Desktop neu gestartet, und Docker sollte 
jetzt funktionieren :)

Hinweis: Sollte Docker Desktop nach der Installation des Kernels dies 
nicht direkt erkennen, musst du ggf. zwischendurch noch deinen Computer 
einmal neu starten.