## .dockerignore: Daten nicht berücksichtigen

* In der **.dockerignore** - Datei führst du Dateien und Verzeichnisse auf,
die beim Bau des Images nicht berücksichtigt werden
  * Achtung: Versteckte Datei (Punkt am Anfang vom Dateinamen)
* Die *.dockerfile* muss in dem Verzeichnis liegen, für das wir docker
build ausführen
* Man kann Namen explizit in die *.dockerignore* schreiben, aber auch *Patterns*
mithilfe der Wildcard * vorgeben:
  * **data***: alle Dateien und Verzeichnisse (im root-Verzeichnis), die mit 
  der Zeichenfolge "data" beginnen, werden ignoriert (z.B. eine Datei *data.txt*)
  * ***data**: alle Dateien und Verzeichnisse (im root-Verzeichnis), die mit der 
  Zeichenfolge "data" aufhören, werden ignoriert (z.B. ein Ordner *more-data*)
  * ****data**: Ordner in allen Unterverzeichnissen, die *data* heißen, werden ignoriert
    * Hierbei darf der Ordner "data" auch in einem tiefen Unterverzeichnis liegen 
    (daher hier die mehreren **). Beispielweise würde auch folgender Ordner ignoriert:
      * a/b/data