## Wie löscht man Container

* Mit dem Kommando **docker [container] rm [Name/ID vom Container]** kann man
einen Container auch wieder löschen.
* Mann kann nur Container löschen, die nicht gerade aktiv sind.

Die IDs von allen vorhandenen Containern anzeigen:
```
docker container ls -aq
```

Alle Containern auf einmal löschen:
```
docker container rm $(docker container ls -aq)
```

* **Tipp:** Bei docker run
  * Mit der Flag **--rm** kann man spezifizieren, dass ein Container direkt
  nach seinem Beenden automatisch wieder gelöscht wird.
    * **docker run -it --rm ubuntu**
      * Praktisch, wenn man kurz mal was ausprobieren will.
