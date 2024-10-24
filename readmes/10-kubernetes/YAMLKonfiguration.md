## Beispiel: *Deployment* für nginx!

* Wir können Konfiguration auch selbst per .yaml schreiben
* Warum würden wir das tun wollen?
  * Wir können die Konfiguration für unsere Software z.B. in einem
  git-Repository speichern!
  * Dadurch können wir unseren Cloud-Setup reproduzierbar deployen
* Wir können eine solche .yaml-Datei deployen:
  * **kubectl apply -f deployment.yaml**


### Aufbau von K8s-Konfigurationsdateien

* Wichtigste Eigenschaften:
  * **apiVersion**: bezieht sich auf die Version der K8s-API
  * **kind**: Art des Objektes, z.B. Deployment
  * **metadata**: hier stehen der "name" und die "labels", unter denen das
  Objekt angesteuert werden kann
  * **spec** (specification): beschreibt den gewünschten Zielzustand für dieses
  Objekt; entsprechende Eigenschaften hängen von der Art des Objektes ab
  * **status**: beschreibt den aktuellen Zustand des Objektes im System