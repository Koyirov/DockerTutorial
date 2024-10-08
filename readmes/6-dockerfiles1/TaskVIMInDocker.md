## Aufgabe: VIM in Docker

* **Vim** ist ein Texteditor unter Linux, mit dem amn Dateien
editieren können (ähnlich nano)
* Der Einarbeitungsaufwand ist etwas höher als bei nano
  * Tipp: Über :quit kann man den Editor wieder schließen
* **Aufgabe:**
  * Erstelle ein Docker Image, welches vim als Editor ausführt, 
  und eine hinterlegte Datei (z.B. text.txt) standardmäßig öffnet
  * Man kann hier z.B. ein Ubuntu als Ausgangsbasis verwenden, und
  vim nachinstallieren
  * Kombiniere dafür **CMD** und **ENTRYPOINT**