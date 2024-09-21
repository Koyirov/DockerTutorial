## Infos zu Containern abrufen

* Auch bei **docker container** können wir uns Informationen 
zu allen Containern anzeigen lassen.
* **docker container ls -a -s**
  * Mit der Flag **-a** (oder **--all**) werden alle Container 
  aufgelistet (sonst nur die gerade aktiven!).
  * Mit der Flag **-s** (oder **--size**) wird zu jedem Container 
  noch die Größe angegeben.
* Alternativ (abel älteres Kommando): **docker ps** (Flags beachten)


## Infos zu Containern abrufen (Teil 2)
* **docker container stats** Zeige dir z.B Arbeitsspeichernutzung 
von den Containern an
* **docker [container] inspect** 
  * Man kann einen Container über seine ID oder seinen Namen ansteuern