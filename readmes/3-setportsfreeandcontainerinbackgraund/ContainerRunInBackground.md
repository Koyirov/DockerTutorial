## Container im Hintergrund ausführen

* Zuerst
  * Wenn in einem Container der Hauptprozess beendet wird, wird auch 
  der Container beendet (z.B. wenn man die Shell beendet).
* Damit ein Container im Hintergrund laufen kann, braucht er einen Prozess,
der gestartet wird und am Laufen bleibt.
  * Bei **docker container start** läuft der Container standardmäßig bereits
  im Hintergrund (sofern wir nicht -i angeben).
  * Bei *docker run*:
    * Mit der Flag **-d** (detached) kann man einen Container im Hintergrund
    laufen lassen.
  * Wenn ein Container im Hintergrund läuft, kann man mit **docker logs** die 
  Ausgabe einsehen.