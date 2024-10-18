## Was ist Kubernetes?

* Eine Plattform zur Steuerung und Verwaltung von Container-basierten Anwendungen
  * "*kubernetes*" griechisch für "Steuermann" / "Pilot"
  * Deutlicher größerer Funktionsumfang als Docker Swarm
  * Plattform nicht nur für Docker-basierte Container, sondern allgemeine
  Container-Engines
    * Insbesondere: **containerd, Mirantis Container Runtime, CRI-O**
    * Auch: **CoreOS rtk, runC (Open Container Initiative)**
  * Häufig abgekürzt als **K8s** (8 steht für die Anzahl der ausgelassenen Buchstaben)
  * Von Google in Go entwickelt
  * 2015 als Open Source veröffentlicht
  * Mit der Prüfung zum **Certified Kubernetes Administrator** (CKA exam) kann man 
  sich zertifizieren lassen


## Was ist Kubernetes nicht?

* Es deployt weder unseren Quellcode, noch baut es unsere Anwendung
  * Wir müssen uns darum selbst kümmern (z.B. mit Docker)
* Es kümmert sich nicht um unsere physischen Maschinen - die müssen wir für 
Kubernetes bereitstellen
* Kubernetes bietet keine Dienste auf Anwendungsebene