##  Routing-Mesh

* Standardmäßig erzeugt Swarm für uns ein Routing-Mesh:
  * Jeder Node nimmt auf einem Port eine Anfrage entgegen, und schickt
  sie an ein beliebiges Replica im Cluster
  * Das funktioniert auch, wenn auf einer Node kein Replica dieses Services läuft
* Das erzeugt natürlich internen Netzwerk-Traffic, da quasi alle Anfragen 
weitergeleitet werden an eine andere Node
* Wenn wir das nicht möchten, können wir den Port auch direkt auf unseren
physischen Servern öffnen
* **Das geht über:**
  * --mode global
* **Wichtig:**
  * Wir müssen uns dann selbst um das Load-Balancing kümmern!