## Umgebungsvariablen

* Wir möchten Umgebungsvariablen für unsere Container definieren
* Quasi wie ein ENV aus dem Dockerfile, aber wir möchten es über die
Kubernetes-Konfiguration steuern
* **Warum?**
  * Dinge, die sich ändern aber können wir dann in diese 
  Umgebungsvariablen auslagern
  * Oder z.B. später den DNS-namen von einem anderen Service aus Kubernetes