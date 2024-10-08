## Build variablem & Umgebungsvariablen

* Der Scope von **ARG**-Variablen beschränkt sich auf die Bauphase
des neuen Images: danach kannst du **ARG**-Variablen nicht mehr nutzen!
  * insbesondere nicht zur Laufzeit in einem Container (**ENTRYPOINT** oder
  **CMD**-Anweisungen)
  * Mit der **ARG**-Anweisungen kann man Parameter vom **docker build** - Befehl
  in Variablen speichern
    * **ARG build_variable=default_wert**
    * **docker build --build-arg build_variable=neuer_wert .**
* Mit **ENV** kann man Umgebungsvariablen definieren, die sowohl in der Bauphase
als auch für Container verfügbar sind
  * also auch in **ENTRYPOINT** oder **CMD**-Anweisungen
  * Diese kann man beim Erstellen eines Containers setzen (über -e)
  * Viele Images (die man als Basis benutzt) verfügen über bereits definierte
  Umgebungsvariablen
    * Beispiel: **MARIADB_ROOT_PASSWORD** (*MariaDB*-Image)
    * Dokumentation lesen