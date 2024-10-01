## Datenbanksoftware ohne Datenverlust aktualisieren

* Wir wollen einen Container, in dem eine MariaDB läuft, updaten
  * Dazu werden wir die Datenbank in einem Volume sichern
* Wir updaten den Container, in dem wir einen neuen Container erstellen,
mit einer neuen Version von MariaDB
* **Wichtig:**
  * mariadb ist i.d.R. nicht abwärtskompatibel: Wenn du stattdessen die Version
  herabstufst, dürfte der Container abstürzen!