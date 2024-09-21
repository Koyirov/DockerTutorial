## Das Kommando *docker run*

**docker run** zusammenfasst drei Kommandos

* **docker [image] pull**
  * Ein Image herunterladen (in der Regel von Docker Hub)
* **docker [container] create**
  * Einen Container auf Grundlage vom heruntergeladenen Image erstellen
* **docker [container] start**
  * Den neu gebauten Container ausführen

### Beachte:
* **docker [container] run** bezieht sich auf *Images*
* **docker [container] start** bezieht sich auf *Container*

Bei der Ausführung **docker run** wird immer ein neuer **Container** erzeugt!
  