## Aufgabe: Copy & Bind Mount

* Erstelle einen Webserver mit PHP und Apache (Image: php, z.B. php:8.1-apache),
und liefere darüber eine PHP-Website aus
* Schaue dazu auf Dockerhub nach in welchem Pfad der Webserver die Daten erwartet
* Das Projekt kann ein Ordner mit einer "index.php"-Datei sein, mit folgendem Inhalt:
```
<?php phpinfo(); ?>
```

* **Aufgabe 1)**
  * Kopiere das Projekt in den Container hinein
* **Aufgabe 2**
  * Erstelle Bind-Mount (wahlweise readonly), und liefere darüber
  das Projekt aus
* Was könnten die Vor- und Nachteile von Copy bzw. Bind-Mount sein?