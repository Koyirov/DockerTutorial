## Wie werden Daten in Docker gespeichert (was wir bislang wissen)

* Images sind read-only, und können nicht verändert werden
* Dateien, die in einem Docker-Container erzeugt oder
verändert werden, befinden sich in einem speziellen *writable*
layer des Containers
* Wenn man einen Container löscht, dann gehen auch alle seine
Dateien verloren


### Das Kommando *docker cp* 

* Mit dem Befehl **docker cp** kann man schnell Dateien oder Ordner in einem Container
und aus einem Container kopieren
* Mann muss zwei Argumente übergeben:
  * Name bzw. Pfad zu dem Element (Datei oder Ordner), das kopiert werden soll
  * Verzeichnis, in das das Element kopiert werden soll

```
1.Parameter: Speicherort von Datei/Verzeichnis (in Container oder Host System)

->

2.Parameter: Neuer Speicherort von Datei/Verzeichnis (in Container oder Host-System)
```

* Element vom Host-System in einen Container hinein kopieren:
  * **docker cp [Element im Host-System bzw. Pfad dahin] [Name/ID des Containers]:[Verzeichnis im Container]**
* Element aus einem Container heraus in das Host-System kopieren:
    * **docker cp [Name/ID des Containers]:[Element im Container bzw. Pfad dahin] [Verzeichnis im Host-System]**

