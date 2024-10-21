## Was sind Microservices?

* Paradigmenwechsel im Software-Engineering:
  * Von "monolithischen Architekturen" zu **Microservices**
  * **Monolithisch:** alle Komponenten in einer Code-Basis
  * **Microservices:** Funktional eng begrenzte und eigenständige Software-Komponenten, 
  die über Schnittstellen miteinander kommunizieren
  * **Vorteile von Microservices:**
    * Leichtere Aktualisierung/Weiterentwicklung durch gezielten 
    Austausch von Komponenten möglich
    * Verschiedene Technologien lassen sich besser miteinander zu kombinieren
    * Mehrere Entwicklerteams können parallel arbeiten
    * Skalierbarkeit: flexible Verteilung von Rechenlast auf mehrere Hosts
    * Ausfallsicherheit
  * **Nachteile:**
    * Zunahme an Komplexität beim Entwicklern, Testen & Deployen
    * Komplizierte Kommunikation zwischen Services
      * Z.B. um die Konsistenz von Datenbanken zu gewährleisten
    * Architektur insgesamt unübersichtlicher


### Wichtiger Hinweis: Persistenz bei Microservices

* Microservices sollen oft automatisch skaliert werden
* **Beispiel**
  * Wenn mehr Anfragen an eine Webseite gestellt werden, können automatisch
  weitere Server mit Webseiten gestartet werden (z.B. in der Cloud)
  * Oft sind Microservices daher "stateless" (zustandlos)
  * **Was bedeutet stateless?**
    * Sie speichern keine Daten
    * Die gesamte Datenspeicherung ist ausgelagert
    * Beispielweise an eine große Datenbank, oder an eine Database-as-a-Service
    (z.B. von Google Cloud oder Amazon AWS)
  * **Wichtig:** Es gibt natürlich auch stateful Microservices!
  * Wir schauen uns in diesem Abschnitt an, wie wir zustandlose Microservices
  mit Docker Swarm skalieren können