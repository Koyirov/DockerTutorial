## Das Kommando: ENTRYPOINT

* **ENTRYPOINT**: Ähnlich wie **CMD**, allerdings mit ein paar Unterschieden:
  * Zusätzliche Befehle, die bei **docker run** als Parameter mitgegeben werden,
  werden als Parameter interpretiert
  * Ein solcher Hauptbefehl ermöglicht es dir den Container wie eine ausführbare
  Datei zu nutzen ("service-based image")
  * Gibt es **ENTRYPOINT** und **CMD**, so werden die Kommandos aus **CMD** an den
  **ENTRYPOINT** dran gehängt
  * Mit dem Parameter **--entrypoint** bei **docker run** kann man den 
  **ENTRYPOINT** manuell überschreiben


### Wann was?

* CMD:
  * Grundsätzlich zu bevorzugen
* ENTRYPOINT:
  * Ausschließlich für Service-based Images