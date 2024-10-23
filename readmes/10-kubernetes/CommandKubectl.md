## Was ist *kubectl*?

* CLI-Tool für K8s-Cluster
  * Minikube-Cluster oder Cloud-Cluster
* Ermöglicht Kommunikation mit der Komponente *kube-apiserver*
* Wir werden *kubectl* nutzen, um mit dem Minikube-Cluster 
zu interagieren und es konfigurieren
* So ähnlich wie bei Docker kann man das Cluster mit Befehlen in
der Konsole verwalten oder komplexere Konfiguration in Dateien (in yaml-Format)
schreiben und dann anwenden


### Erste Schritte mit **kubectl**

* **kubectl version --output=yaml**
  * Ohne die Flag gibt es eine deprecated-Meldung
  * Client und Server-Versionen
* Mit der Flag **--help** lässt man Infos zu einem **kubectl** - Kommando anzeigen
* Mit **kubectl get [K8s-Ressource]** gibst du Infos zu einer K8s-Ressource aus
* **kubectl get nodes**
  * Zustand von unserem Node abfragen (sollte Status: ready sein)
* **kubectl get pods**
  * Noch keine Pods vorhanden
* **kubectl get pods -A**
  * Alle Prozesse auf Steuerungsebene sollten laufen
* **kubectl get all**
  * 


