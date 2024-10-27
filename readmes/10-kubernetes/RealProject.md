## Eigene Images verwenden

* **Problem:**
  * Wir können nicht ohne weiteres auf eigene Images zugreifen, 
  die lokal bei uns gespeichert sind
  * Denn unser Standard *Docker Daemon* läuft außerhalb des Clusters,
  beim Erstellen eines Pods wird aber der innere *Docker Daemon* verwendet,
  um das Image auszuführen
* **Lösung:**
  * Wir konfigurieren die aktuelle Shell, dass sie nicht mehr den
  lokalen Docker Daemon nutzt, sondern zu dem von minikube verbindet
    * **eval $(minikube docker-env)**
    * Oder: eval $(minikube -p minikube docker-env)
    * nur innerhalb der aktuellen Shell-Session gültig
  * Dann braucht man Image vie **docker build -t [gewünschter Name von dem Image] .**
* Mann kan anschließend (am besten in einer weiteren Shell) unter **minikube ssh**
und **docker images** nachschauen, ob der neues Image im Docker Daemon von minikube
existiert


### Eigene Images verwenden: In der Praxis

* In der Praxis
  * Wir möchten nicht auf allen Nodes vom Kubernetes-Cluster alle Images bauen wollen
  * Cloud-Provider stellen daher i.d.R. ein Cloud-Interne, privates Repository
  (quasi ein cloud-internes "Docker-Hub") zur Verfügung
  * Die Nodes sind so eingerichtet, dass Images von dort heruntergeladen werden können
  * Alle Nodes haben Zugriff auf alle Images
* Ansonsten kann man sich auch bei Docker-Hub registrieren, und Images dort hochladen