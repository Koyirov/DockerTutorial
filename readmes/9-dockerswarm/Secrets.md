## Secrets

* Oft möchten wir Passwörter in unserem Cluster verteilen (z.B. sollen alle 
Webserver das MySQL-Passwort kennen, etc.)
* Dafür gibt es in Docker Swarm einen eingebauten Mechanismus:
  * Die sogenannten Secrets:
* Das sind Dateien, die uns dann in unserem Swarm zur Verfügung stehen
* Die Secrets werden dann in unserem Swarm (auf unserem Manager) gespeichert
und verwaltet
* Wie verwenden wir Secrets?

### Secrets: Verwendung

* Zuerst legen wir in der Shell ein Secret an:
  * **printf "This is a secret" | docker secret create top_secret -**
* Anschließend kann man das Secret in unserem Container verwenden:
  * **docker service create --secret top_secret php:8.1-apache**
* Das Secret liegt dann unter /run/secrets/