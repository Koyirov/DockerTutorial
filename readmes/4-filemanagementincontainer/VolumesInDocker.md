## Was ist ein *Volume*?

* **Was sind volumes?**
  * Eine Möglichkeit, um Daten außerhalb eines Containers zu speichern
  * Besonders praktisch für z.B. Datenbanken
  * Volumes werden von Docker verwaltet, und sind daher besonders effizient
  * Wo werden Volumes gespeichert (auf dem Host)?
    * Unter Linux werden deine Volumes in deinem lokalen System in dem
    Verzeichnis */var/lib/docker/volumes/* gespeichert
    * Unter Windows/macOS wird dieses Verzeichnis im Dateisystem der 
    entsprechenden Linux-VM angelegt
    * Auf dieses Verzeichnis kannst (Windows/macOS) oder solltest (Linux) du 
    nicht direkt zugreifen, sondern es ausschließlich über docker volume ansteuern


## Wie erzeugt man und verwaltet ein *Volume*?

* Mit **docker volume create [Name]** kann man ein neues Volume erzeugen
  * **docker volume create ubu-vol**
* Alle Volumes anzeigen: **docker volume ls**
* Mit **docker volume inspect [name]** kann man einzelne Volumes untersuchen
* Man kann auch wie sonst ein Volume mit **docker volume rm [name]** löschen
* Weiter kann man mit **docker volume prune** alle Volumes löschen, die nicht
mit mindestens einem Container verbunden sind
* Es ist nicht möglich, ein Volume umzubenennen
  * Man muss ein neues Volume erstellen, und dort alle Dateien hinüber kopieren