## Das Kommando *docker create*

* Wie kommt man nun von einem Image zu einem Container?
  * **docker [container] create**
    * **docker create -it ubuntu**
      * Wenn man den Container im Terminal ausführen möchtet, 
      ist es wichtig die Flag -t(oder --tty) zu setzen.
        * Terminal-Treiber hinzufügen, um später beim Betrieb des Containers 
        ein Pseudo-Terminal mit dem Container verbinden zu können.
        * Nachträglich nicht mehr möglich!
      * Zudem sollte noch die Flag **i** (oder --interactive) gesetzt sein!
    * Speicherplatzoptimierung: Ein Container enthält nur die geänderten 
    Daten in dem Bezug zum Image, aus dem erstellt wurde.

## Das Kommando *docker start*

* Wie startet man nun einen Container?
  * **docker [container] start**
    * Sofern man den Container im Terminal ausführen möchtet,
    muss man noch die Flag **-i** (oder **--interactive**) setzen.
      * Es muss i.d.r ein Pseude-Terminal mit dem Container
      verbunden sein (Flag -t beim Erzeugen des Containers),
      damit er die Benutzereingaben auch verarbeiten kann.