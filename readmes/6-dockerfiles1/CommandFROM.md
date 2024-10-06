## Das Kommando *FROM*

* Die Anweisung FROM sieht wi folgt aus:
  * FROM [Image]:[tag]
  * Als Basis-Image solltest du ein offizielles Image verwenden
* Die erste Anweisung in einem *Dockerfile* muss **FROM [Name von Image]** lauten
* Es können auch mehrere **FROM**-Anweisungen in einem *Dockerfile* stehen
  * *Multi-Stage Builds* (später)
* Fun Fact: das Image, von dem alle anderen abstammen ist das scratch-Image
(Wortspiel: "from scratch")
  * **https://hub.docker.com/_/scratch/**