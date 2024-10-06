## Die Kommandos **ADD** & **COPY**

* **COPY**: kopiert lokale Daten aus dem Projektverzeichnis in das Image
  * Sollte im Regelfall verwendet werden!
* **ADD**: wie **COPY** aber mit einigen (nicht-offensichtlichen) Zusatzfeatures
  * Erlaubt auch per URL, Daten aus dem Internet zu kopieren
    * Allerdings, best practice: stattdessen **curl** oder **wget** in einer
    **RUN**-Anweisung nutzen
    * Das ist oft sehr viel übersichtlicher, als den ADD-Befehl zu verwenden
  * Entpackt Archive automatisch (grip, tar, bzip2, xz)
    * Einziger Fall, in dem du ADD statt COPY verwenden solltest