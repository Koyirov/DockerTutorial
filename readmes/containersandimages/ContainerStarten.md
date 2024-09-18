## Container: Programme starten

* In einem Container wird i.d.R. immer ein hinterlegtes default Programm gestartet.
* Bei Ubuntu ist es z.B. die Bash, bei Python ist es eine Python-Shell
* Hierbei ist die Schreibweise wie folgt:
  * **docker container run [OPTIONS] IMAGE [COMMAND]**
  * **docker container create [OPTIONS] IMAGE [COMMAND]**
* Man kann hier das Kommando austauschen!

## Container: Zusätzliche Programme starten

* Mit der Hilfe von folgendem Befehl kann man mehrere Programme 
innerhalb des gleichen Containers starten:
  * **docker container exec [OPTIONS] CONTAINER COMMAND**
* Dies kann praktisch sein, wenn man z.B. in einem Python-Container ist,
aber z.B.:
  * Man möchtet eine zusätzliche Datei im Container platzieren
  * Man möchtet Programme nachinstallieren