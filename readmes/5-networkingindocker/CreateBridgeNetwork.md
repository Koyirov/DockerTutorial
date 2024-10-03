## Ein neues (bridge-)Network erstellen

* Man kann ein neues bridge-Network via **docker network create** erstellen
* Anschließend kann man einen Container über den Parameter --network zu diesem
Network verbinden
  * **docker network create my-network**
  * **docker container run --network my-network [Image Name]**
* Mit **docker network rm** bzw. **docker network prune** kann man 
(ungenutzte) Netzwerke auch wieder löschen
  * Die drei Standard-netzwerke (*bridge*, *host* und *none*) kann man nicht löschen
* Warum ein eigenes Netzwerk?
  * Abschottung von anderen Containern
  * Gerade im produktiv-Betrieb sicherer und stabiler


### Container nachträglich verbinden

* Mann kann einen Container vie **docker network connect [Name/ID vom Network][Name/ID vom Container]**
nachträglich mit einem Netzwerk verbinden
  * **docker network connect bridge my-mariadb**
  * Per **docker network inspect bridge** kann man dann prüfen, ob der Container
  dem Network angehört
  * Mit **docker network disconnect**, kann man einen Container auch wieder aus 
  einem Netzwerk entfernen