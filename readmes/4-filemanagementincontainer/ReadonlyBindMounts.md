## Readonly Bind Mounts

* Man kann einen Bind Mount auch auf Readonly schalten
* Dann darf der Container auf diesen Ordner nur lesend zugreifen
* Wenn man dann aus dem Container heraus doch versuchen, eine Datei zu schreiben,
* bekommt man einen Fehler:
  * Read-only file system
* Änderungen vom Host werden natürlich weiterhin direkt in den Container übernommen.
  * **-v [absoluter Pfad zu lokalem Verzeichnis][Pfad zu Container-Verzeichnis]:ro**
  * **--mount type=bind,source=[Pfad zu lokalem Verzeichnis], destination=[Pfad zu Container-Verzeichnis], readonly**