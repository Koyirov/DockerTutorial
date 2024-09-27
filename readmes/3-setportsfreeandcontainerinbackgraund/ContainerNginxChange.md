## Aufgabe: (HTML-Seite im nginx-Container anpassen)

Ziel dieser Aufgabe ist es, die Willkommensseite vom nginx-Container, die 
standardmäßig im Browser angezeigt wird, zu modifizieren
* Starte dazu einen *nginx*-Container und verbinde einen beliebigen,
freien Port zu ihm.
  * **Erinnerung:** Der nginx-Webserver erwartet eingehende Verbindung auf Port 80!
* Greife auf die bash von deinem nginx-Container zu (während der Webserver läuft)
* Navigiere über die bash in das Verzeichnis */usr/share/nginx/html*
* Verändere dann den Inhalt der Datei *index.html*, speichere die Änderung ab und
aktualisiere URL in deinem Browser.
  * Dazu kann es wie üblich hilfreich sein, den Editor *nano* nachzuinstallieren