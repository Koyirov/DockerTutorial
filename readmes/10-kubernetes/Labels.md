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


### Warum mehrere Labels?

* Unter spect.template.metadata.labels können wir Labels definieren,
die dann auf den jeweiligen Pod angewendet werden
* metadata.labels sind also die Labels für das Deployment,
spect.template.metadata.labels sind die Labels für die Pods die erstellt werden
* Natürlich können wir auch die Pods mit einem bestimmten Label auflisten:
  * **kubectl get pods -l app=nginx**


### Aber warum dann matchLabels?

* Wenn ein Deployment die zugehörigen Pods finden möchte, wird dazu
spec.selector.matchLabels verwendet
* Diese matchLabels sind immutable!
* Dieser Selector muss alle Pods von spec.template.metadata.labels finden!
* In der Regel gibt man hier also 1:1 die gleichen Labels an
* Aber warum dann doppelt?
* **Grund:**
  * Wenn wir ein Update unserer Konfiguration herausbringen, können sich die 
  Labels der Pods unter spec.template.metadata.labels geändert haben!
  * spec.selector kann so entwickelt sein, dass es immer noch die zukünftigen
  Pod findet
  * Übrigens: Statt spec.selector.matchLabels können auch komplexere
  Abfragen mit spec.selector.matchExpression angegeben werden
  (nicht Teil dieses Kurses)