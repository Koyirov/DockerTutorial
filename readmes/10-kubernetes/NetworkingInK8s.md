## Networking Konfigurieren: *Services*

* **Networking in Kubernetes:**
  * **Services**: Mechanismus, um Anwendungen in einem Pod 
  in einem Netzwerk zugänglich zu machen
  * Eine logische Gruppierung von Pods und einer Policy, wie
  darauf zugegriffen werden kann
* Intuition:
  * Ein Service gewährt für eine logische Gruppe von Pods eine
  permanente IP-Adresse
  * Dadurch kann diese Gruppe komfortabel angesteuert werden
* Beachte: Jeder Pod hat eine eigene IP-Adresse und eine logische
Gruppe von Pods trägt einen einzigen DNS-Namen
* https://kubernetes.io/docs/concepts/services-networking/service/


### Arten von *Services*

* Es gibt verschieden Service-Arten, u.a.
  * **ClusterIP:** Cluster-interne Verbindungen
    * Standard-Service
  * **NodePort**: Verbindung auf einem statischen Port auf unseren
  Nodes öffnen
    * Leitet intern auf eine ClusterIP weiter
    * i.d.R. im Port-Bereich 30.000-32767
  * **LoadBalancer:** Verbindung nach außen (unter Verwendung eines
  Load Balancers deines Cloud-Anbieters)

