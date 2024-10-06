## Das Kommando **RUN**

* Befehle, die beim Bau des neuen Images ausgeführt werden sollen
  * Setup: dienen in der Regel dazu das Basis-Image durch Installation
  zusätzlicher Pakete zu erweitern
    * Typischer Use Case:
      * Alpine: **RUN apk update && apk add [Paket]**
      * Ubuntu/Debian: **RUN apt-get update && apt-get install -y [Paket]**
  * Jede **RUN**-Zeile fügt eine neue Schicht zum neuen Image hinzu
    * Deswegen: einzelne Befehle mit && bündeln