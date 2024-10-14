## Der Aufbau von **compose.yaml**

* Üblicherweise wird die Konfigurationsdatei für *docker compose*
**compose.yaml (empfohlen)** oder **docker-compose.yaml** gennant
* Du kannst sie auch **compose.yaml** oder **docker-compose.yaml** nennen
* Ganz oben sieht man sehr häufig die Spezifikation der Version
  * **version: '3'**
    * Aktuell: 3
    * Legacy: 2
  * Ist aber veraltet: https://github.com/compose-spec/compose-spec/blob/master/spec.md


### Services spezifizieren: *compose.yaml*

* Unsere Dienste (jetzt erstmal: Container die gestartet werden) können
wir wie folgt definieren:
  * **services**:
    * Erforderlich!
    * Hier werden die einzelnen Container aufgeführt, die du konfigurieren
    und starten (und evtl. replizieren) möchtest
    * Oft: Ein Service entspricht einem Container
    * Aber: wir können auch sagen, dass ein Container mehrfach ausgeführt
    werden soll
      * z.B. Service "webserver" soll 3x einen nginx-Container starten


### Services definieren

* In der YAML wird jeder Service wird separat konfiguriert, z.B.
  * **image:** das Basis-Image festlegen
  * **build:** falls ein Image basieren auf einem *Dockerfile* gebaut werden soll
  * **volumes:** persistenten Speicherort festlegen
  * **ports:** Verbindung *Docker-Host:Container-Port* herstellen
  * **environment:** Umgebungsvariablen setzen
  * **command:** Befehle in Container ausführen
  * **restart:** Neustart-Verhalten festlegen (*no, always. on-failure, unless-stopped*)
  * **expose:** Ports freischalten
  * **depends_on:** Abhängigkeiten zwischen Services definieren, sodass sie in der 
  richtigen Reihenfolge gestartet und gestoppt werden
  * **container_name:** Container benennen
  * **expose:** interne Container-Ports freischalten
  * **links:** den Service mit Containern in einem anderen Service aber innerhalb 
  desselben Netzwerks verbinden
  * **secrets:** vertrauliche Daten verwenden, die in einer separaten Datei aus
  gelagert worden sind
  * Mehr: https://github.com/compose/compose-file/#version-top-level-element


### Das Kommando **docker compose**

* Ähnlich wie bei einem *Dockerfile* solltest du ein leeres Projektverzeichnis anlegen und 
nur eine **docker-compose.yaml** sowie benötigte Daten speichern (Kontext!)
* Besonders praktisch ist das Kommando **docker compose up**
  * Images ggf. herunterladen
  * Container erzeugen
  * Netzwerk erzeugen
  * Container im Netzwerk starten
* Anders als bei **docker build** brauchst du keinen Pfad als Parameter zu übergeben,
der Standardpfad ist nämlich auf **./compose.yaml** bzw. **./docker-compose.yaml** gesetzt.
* Du siehst via **docker network ls**, dass standardmäßig ein *bridge*-Netzwerk eingerichtet,
benannt nach dem Projektverzeichnis
* Mehrere Container starten:
  * **docker compose up**
* Die Container stoppen, die Container und das Netzwerk automatisch löschen, Volumes bleiben
natürlich bestehen
  * **docker compose down**
* Weitere nützliche Sub-Kommandos
  * Container temporär stoppen:
    * **docker compose stop**
  * Container wieder starten
    * **docker compose start**
  * Container pausieren / fortsetzen
    * **docker compose pause**
    * **docker compose unpause**