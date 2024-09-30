## Automatisch generierte Volumes

* Bei manchen Containern wird auch ohne explizite Spezifikation ein Volume angelegt:
* Zum Beispiel beim Datenbank-Management-System **mariadb** bzw. **mySQL**
  * **docker run -it -e MARIADB_ROOT_PASSWORD=password123 mariadb**
    * Per Flag **-e** bzw. **--env** muss hier eine Umgebungsvariable gesetzt werden
    * **docker inspect -f "{{.Mounts}}" [Name / ID]**
    * Das Volume taucht natürlich auch bei *docker volume ls* auf
  * Zur besseren Kontrolle sollte man aber ein eigens benanntes Volume einführen
    * **docker run -it -v mariadb-vol:/var/lib/mysql -e MARIADB_ROOT_PASSWORD=password123 mariadb**