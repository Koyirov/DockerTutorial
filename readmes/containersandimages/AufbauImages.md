## Wie ist ein Image aufgebaut

* Jedes Image besteht aus mehreren Schichten ("Layers")
* Mit jedem Layer entsteht wiederum selbst ein neues Image
* Die Layers bauen aufeinander auf: jeder Layer enthält die Veränderungen 
zum vorherigen Zustand des Images (prinzipiell wie ein diff).
  * Informationseffizienz: da jedes Image im Cache von Docker gespeichert wird,
  brauchen bei einem Update von einem Image nur die aktualisierten Layers 
  heruntergeladen zu werden.

```
Code-Basis -> 1.Schicht(+-) -> 2.Schicht(+-) -> 3.Schicht(+-) -> 4.Schicht(+-) -> 5.Schicht(+-) -> Image:latest
```

## Das Kommando **docker image**

* Eine Übersicht über alle lokalen Images kann man dir per CLI anzeigen 
lassen mit dem Befehl
  * **docker image ls** bzw. **docker images**
* Die Historie eines images abrufen
  * **docker image history [Name vom Image]**
    * **docker image history ubuntu**
    * **docker image history --no-trunc ubuntu**
* Detaillierte Infos zu einem Image abfragen (z.B. "Created")
  * **docker image inspect [Name vom Image]**
    * **docker image history ubuntu**
  * Man kann auch gezielt eine Eigenschaft abfragen
    * **docker image inspect ubuntu --format="{{.Created}}"**
      * Die Flag -f (oder auch **--format**) steht für Formatierungsoptionen einer Ausgabe.
      * Im Wert wird **Go Template Syntax** verwendet, um eine Eigenschaft gezielt anzusteuern.



