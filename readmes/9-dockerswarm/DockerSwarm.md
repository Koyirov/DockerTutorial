## Warum Docker Swarm?

###  Warum braucht man ein Tool zur Container-Orchestrierung?

* Unser Ziel: Anwendungen **steuern und verwalten**, die aus mehreren
Containern bestehen (deployment)
* **Die Anwendung hier:**
  * Die Container soll sich auf verschiedenen physischen Servern in einem
  Netzwerk befinden und ausgeführt werden (Cloud-Architektur)
  * In der professionellen Praxis: Cluster bestehen aus hundert bis tausend
  separaten Containern!
* Docker hat dazu bereit ein Tool integriert: **Docker Swarm**
  * Im Prinzip: **docker compose** aber auf mehreren Host-Systemen
  * Ermöglicht den Produktivbetrieb ("Deployment") von Multi-Container-Anwendung
  in der Cloud
  * **Ein Docker Swarm ist also ein Cluster von Docker Engines**

#### Was liefert uns ein solches Tool?

* **Durchgängige Verfügbarkeit:**
  * Vermeidung von Downtime
* **Skalierbarkeit von Anwendungen:**
  * Performante Ausführung sorgt für geringe Ladezeiten, schnelle Reaktionszeiten
  * Man kann komfortabel auch nachträglich noch weitere Server hinzufügen
* Absicherung vor Infrastruktur-Schäden:
  * Bereitstellung von Backups und Wiederherstellung von früheren Zuständen