## musl vs. glibc

* Was ist musl bzw. glibc?
  * Beides sind Implementierungen der C-Standard-Bibliothek
  * Stellt diverse grundlegende Funktionen zur Verfügung:
    * Einlesen und Öffnen von Dateien
    * Ein- und Ausgaben von Programmen (z.B. printf)
    * Umwandlung von Kodierungen (z.B. iconv für Unicode / UTF-8)
    * Formatierung von Datumsangaben
    * Grundlegende Netzwerkkommunikation
  * glibc:
    * Der defacto-Standard unter Linux
  * Musl:
    * Kleinere, modernere Implementierung der C-Standard-Bibliothek


### Problem 1: Software funktioniert u.U. anders

* Code ist oft auf glibc optimiert
* Und wir als Programmierer gehen oft nicht davon aus, dass C-Standard-Bibliothek 
anders funktioniert
  * **Beispiel:**
    * Performance-unterschiede:
      * https://news.ycombinator.com/item?id=27379482
    * strftime hat z.B. in Python anders funktioniert unter musl vs glibc
      * https://bugs.python.org/issue34672


### Das Problem: musl vs. glibc

* Wenn wir Alpine Linux verwenden (musl):
  * Code, der auf der C-Standard-Bibliothek aufbaut, muss für musl kompiliert sein
  * **Beispiel:**
    * *pip install pandas*
    * Damit wird das Python-Tool "pandas" nachinstalliert (Python und pip muss
    natürlich installiert sein im Container)
    * Das pip-Repository stellt folgendes zur Verfügung
      * Den Quellcode, um das Tool "pandas" zu bauen
      * Und ggf. eine fertig kompilierte Version von Pandas
    * Oft steht dort aber nur eine Version für glibc-Betriebssysteme zur Verfügung
    * Auf Alpine Linux muss der Code also manuell kompiliert werden