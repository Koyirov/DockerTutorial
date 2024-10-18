## Was ist Minikube?

* Problem:
  * Zum Entwickeln und Testen ist es aufwendig ein Cluster
  bestehend aus verschieden Nodes so wie im Produktivbetrieb einzurichten
* Lösung: **minikube**
  * CLI-Tool (Open Source)
  * Erzeugt eine virtuelle Umgebung, in dem ein K8s-Cluster bestehend
  aus einem Node läuft
  * Wichtig: wir verwenden minikube nur für die Einrichtung des Clusters verwenden!
    * Tool **kubectl**

### Minikube installieren

* Wir werden Minikube als Docker-Container ausführen
  * Praktisch, da wir Docker bereits installiert haben
  * Weitere mögliche Treiber:
    * https:/minikube.sigs.k8s.io/docks/drivers/ 
  * Systemanforderungen beachten
    * https:/minikube.sigs.k8s.io/docks/start/ 
  * Windows: Installer verwenden
    * minikube-installer.exe** herunterladen und ausführen
  * MacOS: Homebrew Package Manager (https://brew.sh)
    * **brew install minikube**
  * Nach der Installation führst du bei dir im Terminal **minikube start** aus
    * Kann beim ersten Mal etwas länger dauern, da sehr viel heruntergeladen werden muss
    * **minikube** hat **kubectl** als dependency; wird hier automatisch installiert


### Troubleshooting

* Bei **minikube start** kann es gerade unter Windows zu Problemen kommen
* Mögliche Lösungen:
  * Internetverbindung checken
  * Aktuelles Terminal schließen und neues öffnen
  * nacheinander folgende Befehle ausführen
    * **minikube config set driver docker**
    * **minikube delete**
    * **minikube start --driver=docker**
  * Nur im Notfall, wenn gar nichts anders funktioniert:
  * Anderen Treiber verwenden
    * https://minikube.sigs.k8s.io/docs/drivers/
  * Einen der Online-Playground nutzen (erfordern User-Accounts):
    * Killercoda
    * Play with Kubernetes