## Was sind der Unterschied zwischen **Docker Swarm** und K8s?

* K8s ist komplexer und mächtiger
  * professionaller Standard Container-Orchestrierung gemäß
  **Cloud Native Computing Foundation** (CNFC, gehört zur Linux-Foundation)
  * Umfangreicher Ökoseystem
  * Installation sehr umfangreich
  * K8s braucht aber eigentlich nicht lokal eingerichtet zu werden
    * wird i.d.R. vom Cloud-Anbieter zur Verfügung gestellt (AWS, 
    Digital Ocean, Google Cloud, ...)
  * Kann lokal per Minikube ausgeführt werden -> gleich
  * **Trend:** Größere Community und institutioneller

|                |                   docker swarm                   |                   K8s                    |
|:--------------:|:------------------------------------------------:|:----------------------------------------:|
|      CLI       |            Integration von Docker CLI            |                 kubectl                  |
| UI-Monitoring  | zusätzliches Tool notwendig,<br/> z.B. Portainer |           Dashboard integriert           |
| Load Balancing |                   automatisch                    | Viele manuelle Konfiguration<br/>möglich |
| Auto-Scalling  |             nur manuelle Skalierung              |                    Ja                    |



