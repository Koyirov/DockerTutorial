## Die Client-Server-Architektur von Docker

### Docker Host
* Führt den **Docker Deamon** aus
  * Wenn man die Anwendung Docker Desktop startet, startet man damit automatisch den Docker Deamon.
  * Deamon: ein Prozess, der im Hintergrund arbeitet und Dienste bereitstellt
  * Für das Bauen, Starten und Managen von Containern zuständig.
  * Man kann mit dem Kommando **docker info** einige Daten zu diesem Prozess anzeigen lassen.

### Docker Client
* Kommuniziert mit dem Docker Deamon über die Docker API.
* Man kann darüber Docker über Kommandozeile ansteuern.
* Bei Docker Host und Docker Client kann es sich um dasselbe 
System handeln - so wie in unserem Fall.

### Warum ist Docker so aufgeteilt?
* Der eigentliche Clou von Docker liegt darin, Aufgaben auf mehrere Hosts aufteilen zu können.
  * Später dazu mehr (docker swarm, Kubernetes).