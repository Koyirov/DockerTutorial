## Copy vs. Bind-Mount: Funktionsweise

* **Copy:**
  * Ein *docker cp* kopiert die entsprechenden Dateien in den "writable layer"
  von unserem container
  * Dies is performant, da Zugriffe direkt von Docker optimiert werden können
* **Bind-Mount:**
  * Ein bind mount erzeugt einen gewissen Overhead
  * Warum?
    * Änderungen an Dateien müssen direkt im Container sichtbar sein
    * Ggf. müssen auch Änderungen aus dem Container auf den Host zurückgeschrieben werden
    * Dieses kostet zusätzliche Performance


## Copy vs. Bind-Mount: Wann nutzen?

* Manchmal müssen wir für einen Anwendungszweck z.B. ein bind mount benutzen
* Wenn wir aber die Wahl haben:
  * **Copy:**
    * Ein Copy ist ideal im Produktivbetrieb, wo es auf Performance ankommt
    * Wenn der Container einmal eingerichtet ist, dann bleibt er so, und 
    Änderungen müssen manuell übernommen werden (oft gut!)
  * **Bind-Mount:**
      * Ein Bind-Mount ist praktisch während der Entwicklung
      * Änderungen müssen nicht in den Container übertragen werden