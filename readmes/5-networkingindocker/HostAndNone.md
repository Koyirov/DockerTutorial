## Netzwerk-Treiber in Docker

* **Host:** Container werden nicht vom Host-System isoliert
  * Container mit diesem Treiber sind unter der IP-Adresse des Hosts erreichbar
  * Auf einem Host-System kann es immer nur **ein** Host-Netzwerk geben,
  das schon besteht; du kannst kein weiteres erzeugen
  * **Wichtig:** Funktioniert nur auf linux-Hosts
* **None (bzw. Null):** die Netzwerkfunktionalität des Containers wird deaktiviert
  * Es kann kein *None*-Network erzeugt werden
  * Beim Erstellen eines Containers die Flag **--network none** setzen
* Später werden wir noch weitere Netzwerk-Treiber kennenlernen
  * Z.B. **Overlay** bei *docker swarm*, wenn container auf verschiedenen Hosts laufen