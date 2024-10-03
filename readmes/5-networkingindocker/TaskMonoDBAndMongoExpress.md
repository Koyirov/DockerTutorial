## Aufgabe: (MongoDB & MongoExpress)

So ähnlich wie bei der Verbindung von einem mariaDB-Container und einem
phpMyAdmin-Container geht es hier darum eine Datenbank (MongoDB) und 
ein grafisches Webinterface für diese Datenbank (Mongo Express) auf
Container-Ebene in einem Netzwerk miteinander zu verbinden.

* Verwendete Images:
  * **MongoDB:** https://hub.docker.com/_/mongo
  * **MongoDB:** https://hub.docker.com/_/mongo-express
* Erstelle ein bridge-netzwerk namens *mongo-net* und starte darin einen
Mongo-Container mit dem Namen *my-mongo*. Verbinde im Zuge dessen auch das
Verzeichnis */data/db* im Container mit einem Volume *mongo-vol*.
  * Tipp: es macht Sinn den Container im Hintergrund laufen zu lassen
  * Falls du den Container erst genauer untersuchen willst: auch er 
  verwendet ein Debian-Image (bash ...)
* Starte nun, ebenfalls in dem Netzwerk mongo-net, einen Mongo Express-Container,
den du zum MongoDB-Container verbindest. Denke daran, einen Port vom Host auf 
den 8081 des Mongo Express-Containers weiterzuleiten, damit du die 
Mongo-Express-Oberfläche aufrufen kannst.
* **Zudem:**
  * Damit Mongo Express sich zu MongoDB verbindet, müssen Umgebungsvariablen
  gesetzt werden.
  * Versuche erst mithilfe der Dokumentation auf Docker Hub selbst 
  herauszufinden, welche Umgebungsvariable du setzen musst
  * Öffne schließlich die Anwendung im Browser