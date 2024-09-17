## Container umbenennen: *docker rename* und die Flag *--name*

* Einen Container immer über seinen zufallsgenerierten Name oder die ID 
anzusteuern ist ziemlich unpraktisch 
* Also sollte man den Container umbenennen, wofür man verschiedene 
Möglichkeiten hat
  * Namen nachträglich ändern
  * **docker (container) rename [alter Name] [neuer Name]**
    * **docker (container) rename [alter Name] ubuntu-test**
  * Eigenen Namen beim erzeugen festlegen mit der Flag **--name**
    * **docker create --name ubuntu-test -it ubuntu**
    * **docker run --name ubuntu-test -it ubuntu**
  * Namen von Containern müssen eindeutig sein