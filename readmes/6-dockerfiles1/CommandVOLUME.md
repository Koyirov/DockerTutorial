## Das Kommando **VOLUME**

* **VOLUME** spezifiziert, wo später in einem Container ein Volume
erzeugt werden soll
  * Nimmt nur einen Parameter entgegen: Pfad innerhalb des Containers
  zum Verzeichnis, zu dem ein Volume erstellt werden soll.
  * Enthält keinen Pfad in das Host-System, um die Portierbarkeit
  des Images zu gewährleisten
  * Wenn wir das Volume benennen möchten, können wir dies über **-v**
  zum Zeitpunkt der Container-Erstellung tun
* **Use Case:** Sicherstellen, dass eine Datenbank die Datenbasis immer
in ein Volume auslagert - selbst wenn der Container den -v-Parameter 
erstellt wurde