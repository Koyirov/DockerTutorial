## Projekt: Webserver in Kubernetes

* Wir möchten jetzt einen Webserver in Kubernetes laufen lassen
* Dieser soll unsere eigene Webseite ausliefern
* **Wie bekommen wir das hin?**
  * Schritt 1: Wir erstellen ein Image (per Dockerfile)
  * Schritt 2: Wir stellen dieses Image dem Docker in Kubernetes zur Verfügung
  * Schritt 3: Wir erstellen Deployment und Service