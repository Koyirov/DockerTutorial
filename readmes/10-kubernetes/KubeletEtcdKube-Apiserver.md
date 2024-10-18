## Wie ist ein Kubernetes-Netzwerk aufgebaut?

* Ein K8s-Cluster besteht aus mindestens einem Node
* **Node:** physikalische oder virtuelle Maschine
  * Nodes, auf denen Pods ausgeführt werden, nennt man manchmal auch *worker* nodes
* In der Praxis laufen auf jedem Node in einem Cluster mehrere Pods
* Die Steuerung des Clusters erfolgt über die sogenannte **control plane**
(Steuerungsebene), deren Komponenten prinzipiell auf jedem Nodes des Clusters 
aufgeführt werden können
* Cluster lassen sich beliebig erweitern durch neue Server, auf denen die entsprechenden 
Prozesse installiert sind


### Was sind die Komponenten in einem K8s-Netzwerk?

* Die Steuerungsebene eines Clusters setzt sich aus folgenden Komponenten zusammen
  * **kube-apiserver**: Frontend zur Kommunikation zwischen, stellt K8s-API 
  zur Verfügung, nimmt *requests* von Client an
    * Einziger *entrypoint* zum Cluster (Sicherheit)
  * **etcd**: Speicher für Konfigurationsdateien, die Zustände der ausgeführten
  Anwendungen und Metadaten des Clusters
  * **kube-scheduler**: Verteilung von Pods auf Nodes entsprechend 
  verfügbaren Ressourcen
  * **kube-controller-manager**: Überweichungsschleifen für die Nodes im Cluster,
  um auf Zustandsveränderungen reagieren (z.B. Ausfälle)
  * **cloud-controller-manager**: Cloud-Anbieter-spezifische Überwachungsschleifen
* Die Steuerungsebene kann auf mehrere Nodes aufgeteilt werden
  * => Ausfallsicherheit


* Auf jedem Node laufen immer diese Komponenten:
  * **kubelet**: Ausführung von Pods, in denen Container laufen
    * gemäß *request* von *kube-scheduler*
  * **kube-porxy**: Umsetzung von Netzwerkregeln und der Verbindungsweiterleitungen 
  zum Host; leitet **requests** zwischen Pods weiter und gewährleistet performante 
  Kommunikation
  * **Container Runtime**: z.B. Docker
* Zusätzliche Addons (Wissen für Fortgeschrittene):
  * https://kubernetes.io/docs/concepts/cluster-administration/addons/