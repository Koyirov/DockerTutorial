## Grundlagen von Docker

### Aufgabe 1: Images

* Finde auf *Docker Hub* das offizielle Node.js - Image
  * Welche drei Hauptvarianten werden in der Dokumentation für 
  das Image aufgeführt und was die Unterschiede zwischen ihnen?
  * Lade das aktuelle **node:alpine** - Image herunter
    * Wie groß ist es im Vergleich zum Standard-Node.js - Image?
  * Benenne das heruntergeladene Image *small-node* um
  * Überzeuge dich, dass bei dir jetzt ein Image namens *small-node* existiert
  * Erzeuge und starte einen Node.js - Container basieren auf dem *small-node* Image,
  welcher automatisch wieder gelöscht werden soll und versuche darin wie gehabt 
  die Bash auszuführen.
    * Welche fehlermeldung tritt dabei auf?
  * Lösche beide Node.js-Images, die auf Alpine basieren

### Aufgabe 1: Container

* Erzeuge einen neuen Node.js - Container namens *test-container* auf Grundlage
des Standard-Node.js - Images und führe darin die *bash* aus.
  * Dieser Container soll nach Beenden NICHT automatisch gelöscht werden
* Steuere mit der *bash* im Container den Ordner *etc* an und finde die Version
der zugrunde liegenden Debian-Distribution heraus (steht in der Datei: "debian_version").
  * Tipp: mit dem *cat*-Befehl kannst du Dateien auslesen
* Gehe dann zurück in den root-Ordner und von dort zu */usr/share*
  * Findest du in dem Ordner Hinweise zu einer anderen Programmiersprache,
  die wir schon verwendet haben und die in diesem Container installiert ist?
* Benenne dann den Container *test-container* um in *my-node-app*
* Erstelle dann dort dann den Ordner /app (Befehl: mkdir /app)
* Wechsel anschließend in diesem Ordner und erstelle eine Datei "main.js" mit
folgendem Inhalt: 
  * console.log("Hallo Welt")
Führe anschließend dein Skript via **node main.js* aus