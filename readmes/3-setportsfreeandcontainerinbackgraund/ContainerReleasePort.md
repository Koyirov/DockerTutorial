## Docker container create

* Auch beim Erstellen von einem Container kann man eine Port-Weiterleitung
spezifizieren:
  * **docker container create -p HostPort:Container-Port Image-Name**
  * Warum beim Erstellen des Containers, und nicht beim Starten?
  * Weil das Starten kann ja automatisch passieren (je nach restart-policy)
  * Daher muss das beim Erstellen eines Containers spezifiziert werden.