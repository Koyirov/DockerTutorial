## Was sollte man bei der Docker Ordner-Struktur beachten?

* Der Pfad **docker build [Pfad]** übergeben wird, wird zum *Kontext*
für den Bau deines Images
  * Mit Kontext ist die Gesamtheit aller Daten gemeint, auf die der
  docker *deamon* beim Abhandeln der Anweisungen im *Dockerfile*
  zugreifen darf
  * Pass auf also, worauf du **docker build** ausführst!
  * **Best Practice**:
    * speichere das *Dockerfile* in einem leeren verzeichnis bzw. darin
    sollten sich nur die Dateien befinden, die nötig sind, um das Image zu bauen
    * Dann führst du **docker build** auf dieses Verzeichnis aus
  * Wenn du **docker build** auf dein root-Verzeichnis ausführst (z.B. weil du darin
  dein Dockerfile gespeichert hast), kann über das Dockerfile auf alle Daten 
  zugegriffen werden


### Was passiert bei *docker build*

* Zunächst wird das gesamte *Dockerfile* validiert: bei einem Syntax-Fehler wird
keine Anweisung ausgeführt und du erhältst eine fehlermeldung
* Falls die Validierung fehlerfrei abgeschlossen wurde, werden danach nacheinander 
die einzelnen Anweisungen ausgeführt
  * Bestimmte Anweisungen können bestimmte Schichten erzeugen
* Ganz am Ende wird eine ID für das Image generiert
* Docker ist hierbei effizient:
  * Um den Bau-Vorgang zu beschleunigen, nutzt Docker sein *build-cache* ("CACHED")
* 