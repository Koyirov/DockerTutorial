## Lernziele für diesen Abschnitt

* Was ist ein **Service**?
* Wie ist eine **docker-compose.yaml**-Datei aufgebaut?
  * Wofür ist das Format **YAML** gut?
* Wie funktioniert der Befehl **docker compose**?


## Was ist *docker compose*?

* **Problem**:
  * Bislang is es aufwändig Anwendungen aufzustellen, die aus mehreren
  Containern bestehen
    * Wir müssen für jeden Container separat **docker run** ausführen
    * Mit *Dockerfiles* können wir zwar einzelne Images konfigurieren,
    aber keinen Verbund von Containern
      * z.B. können wir Images per Dockerfile nicht miteinander verbinden
* **Lösung**:
  * In einer Konfigurationsdatei (üblicherweise *compose.yaml* oder
  *docker-compose.yaml* genannt) spezifizieren wir mehrere Container und
  ihre Verbindung zueinander
  * Dann führen wir das Kommando **docker compose** aus
  * Damit wird automatisch *ein neues Netzwerk* erzeugt und die Container 
  darin gestartet
  * Du kannst **docker run** - Befehle als **compose.yaml (bzw. 
  docker-compose.yaml)** Konfiguration umformulieren