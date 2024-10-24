## Was machen die "labels"?

* Bei unserem Deployment haben wir metadata.labels angegeben
* Aber was machen die genau?
  * Damit können wir später das Deployment komfortabel finden
  * Wir können dann z.B. sagen:
    * **kubectl get deployments -l app=nginx**
  * Welche Labels wir vergeben, bleibt komplett uns überlasen
  * Wir dürfen auch mehrere Labels vergeben, und können dann nach
  mehreren filtern:
    * **kubectl get deployments -l app=nginx,version=1.0**