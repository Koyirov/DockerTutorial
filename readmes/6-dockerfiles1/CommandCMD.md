## Das Kommando: **CMD**

* Mit CMD kann man ein Kommando definieren, welches standardmäßig 
ausgeführt wird
* Hierbei ist die Schreibweise wie folgt:
  * Exec-Form (offiziell empfohlen):
    * Das Programm wird direkt gestartet
    * **CMD ["Programm/Datei", "Parameter1", "Parameter2"]**
  * Shell-Form
    * Hier wird eine Shell gestartet, die das Programm dann abruft
    * Vorteil: Platzhalter wir z.B. "*", und Variablen können aufgelöst werden
    * **CMD Programm/Date Parameter1 Parameter2**
  * **Wichtig**:
    * Es wird immer nur das letzte CMD-Kommando beachtet!