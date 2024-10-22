## Ein echtes Cluster

* In diesem Projekt werden wir ein echtes Cluster in Betrieb nehmen
* **Setup bei mir:** 
  * 3x Raspberry Pi (armhf, raspbian Linux)
  * Alle im gleichen Netzwerk
* **Generell, was ist wichtig:**
  * Alle Computer, müssen untereinander im Netzwerk
  kommunizieren können (u.A. auch fürs Routing Mesh)
  * Alle Computer müssen Zugriff auf die Images haben, die wir auf
  dem Manager ansteuern wollen
  * Alle Computer müssen Linux verwenden
* **Bei mir anscheinend auch:**
  * Docker muss immer mit root-Rechten gestartet werden, 
  rootless-Docker hat bei mir nicht funktioniert
* Worauf soll man noch achten?
* Die Verbindung zu den Nodes sollte möglichst stabil sein
(idealerweise Ethernet, bei mir jetzt 5Ghz WLAN)
* Die Manager-Nodes sollten statische IPs haben
  * Das sorgt bei einem Reboot eines Managers dafür, dass sich das
  Cluster wieder besser neu aufbauen kann
* Das Netzwerk sollte hinreichend schnell sein