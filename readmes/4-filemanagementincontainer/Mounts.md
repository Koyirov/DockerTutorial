## Was sind *Mounts*?

* Als Mounts bezeichnet man allgemein die Verknüpfung von der
Verzeichnisstruktur eines Containers mit Daten, die außerhalb 
von Container liegen
  * Das erlaubt uns Dateien, die in Container erzeugt und genutzt werden,
  **persistent** zu sichern
    * Dateien bleiben auch nach dem Löschen des Containers bestehen


### Welche Arten von *Mounts* gibt es?

* Es gibt drei verschiedene Arten von Mounts
  * **bind**
    * Ein Container wird mit dem lokalen Dateisystem verknüpft
    * Man kann dann von einem Container aus in einem Ordner des Host-Systems operieren
  * **volume**
    * Bestimmte Daten in dem Container werden an einen Docker-spezifischen Speicherort ausgelagert
    * Volumes werden (in der Regel) mit Docker verwaltet
  * **tmpfs**
    * nur unter Linux verfügbar!
    * Daten werden in den Arbeitsspeicher deines lokalen Systems geschrieben
    * Daten werden sofort gelöscht, sobald der Container anhält
      * Use Case: sensible Daten


### Wie führt man einen *Bind Mount* durch?

* Zur Erinnerung, bind mount:
  * Ein Container wird mit dem lokalen Dateisystem verknüpft
* Es gibt zwei Schreibweisen, um ein **bind mount** durchzuführen
* Schauen wir uns zuerst die ausführlichere Schreibweise an:
  * Flag **--mount** setzen und spezifizieren
    * **type=bind**
    * **source:** enthält den Pfad zum lokalen Verzeichnis, das du mit der 
    Verzeichnisstruktur des Containers verknüpfen möchtet
    * **destination:** enthält den Pfad zum Verzeichnis im Container
  * Insgesamt:
    * **--mount type=bind,source=[Pfad zu lokalem Verzeichnis], destination=[Pfad zu Container-Verzeichnis]**

### Die Flags --mount vs. -v

* Es gibt noch eine alternative (und kürzere) Schreibweise für einen bind *mount*
  * Man kann auch die Flag -v (oder: --volume) verwenden:
    * **-v [absoluter Pfad zu lokalem Verzeichnis][Pfad zu Container-Verzeichnis]**
      * Man muss immer den absoluten Pfad zu dem lokalen Verzeichnis angeben!
* Der wesentliche Unterschied zwischen den beiden Schreibweisen besteht darin, dass Docker bei *-v*
ein neues Verzeichnis im Host-System anlegen wird, falls es noch nicht existieren sollte, während
bei *--mount* das Verzeichnis in *src* tatsächlich existieren muss (sonst: Fehlermeldung)
* Die Syntax mit der Flag -v ist übersichtlicher, daher wird sie häufiger verwendet

```
docker run -it -v ${pwd}:/projekt ubuntu
```