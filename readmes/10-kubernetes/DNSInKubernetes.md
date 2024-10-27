## DNS in Kubernetes

* Das ziel (generell):
  * Wir möchten, dass mehrere Pods untereinander kommunizieren können
  * Beispielweise:
    * 1x Frontend (z.B. Flask)
    * Kommuniziert zu einem Backend (z.B. einem Redis)
* Wie geht das?
* Ein Service:
  * Ist innerhalb vom Kubernetes-Cluster unter seinem DNS-Namen zu Verfügung
  * Das ermöglicht, dass ein Pod auf einen Service (und damit auf andere Pods)
  zugreifen kann!
* Das schauen wir uns am Bestens am Beispiel an