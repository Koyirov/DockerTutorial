## Kubernetes Grundlagen: Was ist ein **Pod**?

* In K8s interagieren wir nicht mit der zugrunde liegenden Container-Engine
  * Wir könnten also irgendwann mal Container-Technologie wechseln, ohne auf Ebene
  von K8s Änderungen vornehmen müssen
* Diese "Austauschbarkeit" wird u.A. durch die Einführung einer neuen 
Abstraktionsebene erreicht
* Die kleinste Einheit in K8s stellen **Pods** dar:
  * High-level-Perspektive auf container-basierte Anwendungen
  * **Pod**: eine Umgebung, in der ein Container oder eine "logische" Gruppe aus
  mehreren Containern ausgeführt wird
    * Intuition: zusätzliche "Isolationsschicht" um Container
    * Oft, aber nicht immer: Ein Container in einem Pod
  * Alle Container in einem Pod laufen auf der gleichen physischen Maschine
  * Pods sind "Wegwerf"-Objekte (ähnlich wie Container): bei neuen Konfigurationen 
  werden Pods gelöscht und neue erstellt