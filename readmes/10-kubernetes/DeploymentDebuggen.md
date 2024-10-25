## Deployment Debuggen

* Neuen Zustand des Clusters untersuchen:
  * **kubectl get deployment**
  * **kubectl get replicasets**
  * **kubectl get pods**
    * erweiterte Ansicht
      * **kubectl get pods -o wide**
    * falls es mal länger dauert, bis ein Pod startet
      * **kubectl get pods --watch**
* Logs anzeigen: **kubectl logs [Name vom Pod]**
* Zusätzliche Infos anzeigen: **kubectl describe pod [Name vom Pod]**
* Zusätzliche Infos anzeigen2: **kubectl describe replicaset [Name vom Replicaset]**
* Zusätzliche Infos anzeigen3: **kubectl describe deployment [Name vom Deployment]**
* Auf das Terminal in einem Pod zugreifen:
  * **kubectl exec -it [Name vom Pod] -- /bin/bash**
* Mit **kubectl delete deployment [Name vom Deployment]** kann man das 
Deployment auch wieder löschen

