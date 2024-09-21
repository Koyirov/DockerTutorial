## Hinweis 

In der nächsten Lektion werden wir einen Webserver mit Hilfe von Docker 
starten. Der Befehl, den ich hierzu verwenden werde, ist bei mir:

```
docker run -it -p 3000:80 -v ${pwd}:/var/www/html php:8.1-apache
```

Bitte beachte, dass du diesen Befehl im korrekten Ordner ausführen 
musst, also in dem Ordner, wo es die index.php-Datei gibt, die wir 
im Video gleich anlegen werden.

Bitte beachte zudem, dass du die geschweiften Klammern unter Windows 
ggf. in runde Klammern umwandeln musst. Mit ${pwd} bzw. $(pwd) wird 
der aktuelle Pfad ermittelt (ein Feature der Shell und nicht von Docker), 
und diese Schreibweise ist je nach Terminal leicht unterschiedlich.

Unter Windows ist der Befehl daher u.U. wie folgt:

```
docker run -it -p 3000:80 -v $(pwd):/var/www/html php:8.1-apache
```