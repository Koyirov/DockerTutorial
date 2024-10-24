## Konfiguration des Clusters

* **Workloads:** eine containerisierte Anwendung, die auf dem K8s-Cluster
ausgeführt wird.
* K8s stellt diverse verschiedene **Workloads** zur Verfügung
* Diese bestimmen, wie die Anwendung im Cluster ausgeführt und skaliert wird
* **Beispiel:**
  * ReplicaSet bzw. Deployment für stateless Anwendungen
  * StatefulSet für stateful Anwendungen
  * DaemonSet für Pods, die auf jeder Node im Cluster ausgeführt werden sollen
  * Job bzw. CronJob für Cronjobs


### *ReplicaSet* und *Deployments*

* **Hier in diesem Kurs**:
  * Wir möchten eine stateless-Anwendung im Cluster ausführen
* Dafür haben wir 2 Möglichkeiten
  * ReplicaSet
  * Deployment
* **ReplicaSet:**
  * Stellt sicher, dass eine bestimmte Anzahl an Kopien unseres Pods 
  im Cluster ausgeführt wird
* **Deployment:**
  * Verwaltet ein ReplicaSet, aber erlaubt einfachen, nachträglichen 
  Austausch auf eine neuere Version

### Beispiel: *Deployment* für nginx!

* Schauen wir uns mal an, wie wir einen nginx-Webserver deployen können
* Dafür können wir ein Deployment über **kubectl** anlegen:
  * **kubectl create deployment [Name deines Deployments] --image=[Docker Image]**
  * Das Image muss hier auf dem Docker Hub aufrufbar sein!
  * **kubectl create deployment nginx-deployment --image=nginx --replicas=3 --port=80**
    * Mit dem Parameter **--replicas** können wir die Anzahl der Replicas konfigurieren
    * Mit dem Parameter **--port** können wir dokumentieren, welcher Port vom Container
    geöffnet wird (ähnlich wie EXPOSE in Docker, nur Dokumentation)
  * Die Konfiguration können wir anschließend einsehen:
    * **kubectl edit deployment/nginx-deployment**