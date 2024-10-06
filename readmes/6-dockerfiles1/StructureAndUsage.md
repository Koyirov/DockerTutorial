## Lernziele für diesen Abschnitt

* Was sind **Dockerfiles**?
* Wie sieht die Syntax von einem *Dockerfile* aus?
  * Wie laufen die wichtigsten Anweisungen?
* Wie funktioniert das Kommando **docker build**?
* Was sind **Multi-Stage Builds**?


### **Dockerfiles** und **docker build**

* **Problem:**
  * CLI-Kommandos können umfangreich und übersichtlich werden
  * Häufig wollen wir Container verwenden, die auf ähnliche Weise konfiguriert sind
  * Zudem können wir manche Befehle nicht automatisieren (z.B. das Nachinstallieren
  und Konfigurieren von Software)
* **Lösung:**
  * Wir schreiben unsere Konfigurationen für ein neues Image in eine Datei
  (genannt **Dockerfile**) und führen dann das Kommando **docker build** aus,
  um ein für unsere Zwecke maßgeschneidertes Image zu erstellen.

### Was ist ein **Dockerfile**?
* In einem **Dockerfile** wird ein neues Image anhand von Anweisungen entsprechend 
einer vorgegebenen Syntax konfiguriert
* Jede Zeile hat die Form
  * **[Anweisung]:[Parameter]**
  * Nach Konvention werden die Anweisungen immer groß-geschrieben (um sie
  von den Parametern besser unterscheiden zu können); sie sind aber nicht
  *case-sensitive*
  * Kommentare beginnen mit **#** und werden beim Bauen ignoriert
    * **#** muss am Anfang einer Zeile stehen
  * Ein **Dockerfile** hat keine Endung und heißt standardmäßig **Dockerfile**
  * Man kann einen beliebigen Texteditor verwenden, um *Dockerfile* zu erstellen


## Das Kommando **docker build**

* Der Builder erzeugt aus einem *Dockerfile* ein Image
  * **docker build [Pfad zum Dockerfile]**
* Falls sich im aktuellen Arbeitsverzeichnis das *Dockerfile* befinden sollte, 
braucht man nur auszuführen:
  * **docker build .**
    * der Punkt **.** verweist auf das aktuelle Verzeichnis
* Wenn dein **Dockerfile nicht **Dockerfile** heißen sollte, kann man es mit
dem Flag **-f** (bzw. --file) ansteuern
  * **docker build -f mydockerfile .**
* Man kann auch ein Git-Repository via URL ansteuern
* Mit der Flag **-t** bzw. (**--tag**) kann man dem Image einen neuen *tag*
zuweisen, um komfortabler darauf zugreifen zu können