## Services Verwalten

* Services einsehen:
  * Mit **kubectl get services** können wir alle Services einsehen
* Service löschen:
  * Mit **kubectl delete service [Name von deinem Service]** kann man
  einen Service auch wieder löschen
* Ausführlicherer Befehl, um Service zu erstellen:
  * **kubectl create service [Art des Service] [Name von deinem Service] --tcp=[port]:[targetPort]**
  * In unserem nginx-Beispiel verwenden wir
    * **kubectl create service nodeport nginx-service --tcp=80:80**
  * Anschließend müssen wir dem Service sagen, wie die Pods gefunden werden:
    * **kubectl set selector service [Name] [key]=[value]**
    * **kubectl set selector service nginx-service app=nginx**