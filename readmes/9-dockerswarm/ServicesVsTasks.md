## Services vs. Tasks

* Docker Swarm basiert auf dem Prinzip eines "deklarativen Modells":
  * Wir legen Zielzustand fest, und Swarm versucht diesen zu erreichen
* **Service**: Beschreibung des Zielzustands
  * Beispiel: bestimmte Anzahl von Replicas von einem Container
* **Task**: Durchführung von Arbeitsstufen, um diesen Zustand herzustellen
* Im Rahmen von Docker Swarm kann ein einzelner Container als Instanziierung 
eines Tasks betrachtet werden
* Tasks werden also von / durch Services gestartet

### Wie managen wir einen Service?

* Hierzu haben wir verschiedene Befehle zur Verfügung:
  * **docker service create**: Hiermit erstellen wir einen Service
  * **docker service ls**: Services anzeigen
  * **docker service update**: Service-Konfiguration aktualisieren
  * **docker service remove**: Services entfernen
  * **docker service ps**: Alle Tasks auflisten