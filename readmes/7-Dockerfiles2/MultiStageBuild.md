## Was ist ein Multi-Stage Build?

* **Problem:**
  * Images sind oft unnötig groß, weil sie z.B. einen Compiler
  erhalten
  * Dieser wird später zur Laufzeit aber gar nicht benötigt
  * Lösung:
    * **Multi-Stage Build:** Build-Image(s) und Produktivbetriebs-Image
      * Wir erzeugen erst die für unsere Anwendung benötigten Artefakte
      (z.B. Binärdateien) und kopieren sie dann in ein kleineres Image
      (in der Regel die Linux-Distribution *Alpine*)
      * Dieses Image für den Produktivbetrieb enthält nur noch die
      Komponenten, die zur Ausführung notwendig sind (aber z.B.
      keinen *Compiler* mehr)
* Praxis:
  * Wir verwenden in einem *Dockerfile* mehrere **FROM**-Anweisungen
  * Du kannst dann z.B. mit **COPY --from=0 [Ort alt] [Ort neu]**
  Artefakte aus vorherige Bauphasen in die aktuelle Phase kopieren und nutzen
    * Die Phase sind aufsteigend numeriert, beginnt bei 0
  * Du solltest die Bauphasen mit **AS** benennen und sie über ihre Namen ansteuern
    * **FROM golang:1.15.1-alpine AS builder**
    * **...**
    * **COPY --from=builder [Ort im alten Image] [Ort im neuen Image]**