## Was sind Nodes in einem Swarm?

* Alle Server in einem Swarm werden als **Nodes** bezeichnet
* Es gibt zwei Arten von Nodes:
  * **Manager Nodes**
    * Kommunizieren mit den Worker Nodes
    * Verteilen und starten Prozesse auf den Nodes
    * Es kann mehrere Manager Nodes geben, aber nur einen **Primary Manager Node**
  * **Worker Nodes**
    * Führen Prozesse aus, die von Manager Nodes zugewiesen wurden
    * Kommunizieren ihren Status zum Manager Node


### Docker Swarm testen mit einem Node

* Nachschauen, ob Docker Swarm aktiv ist
  * **docker system info**
* Einen Swarm starten:
  * docker swarm init
    * Erzeugt in unserem Fall einen Swarm, der nur aus einem Manager Node besteht
* Einen Swarm wieder verlassen
  * **docker swarm leave --force**
* Infos über Nodes anzeigen (auf einem Swarm-Manager):
  * **docker node ls**
    * Ein Node sollte angezeigt werden mit *Manager Status:* **Leader**