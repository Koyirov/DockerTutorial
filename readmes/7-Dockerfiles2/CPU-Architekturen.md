## CPU-Architekturen: ARM vs. x86

* **x86:** eine Mikroprozessor-/Befehlssatz-Architektur, di bislang,
standardmäßig bei CPUs in Laptops und Desktoprechnern verwendet wird
  * insbesondere stellen Intel und AMD x86-kompatible CPUs her
* **ARM:** eine alternative Mikroprozessor-/Befehlssatz-Architektur,
die vorwiegend in Smartphones und Tablets zum Einsatz kommt
  * Aber auch die Apple-Chips für MacBooks basieren auf ARM
  * Es scheint einen Trend hin zu ARM-basierten CPUs zu geben


## CPU-Architekturen und Docker

* Docker verwendet den Kernel des Host-Betriebssystems mit
* Ein Ändern der CPU-Architektur ist daher nicht so ohne weiteres möglich
* **Das bedeutet:**
  * Ein ARM-Host führt i.d.R. einen Container mit ARM-Architektur aus (linux/arm64)
  * Ein x86-64-Host führt i.d.R. einen Container mit x86-64-Architektur aus (linux/amd64)
* Auf bestimmten Systemen werden aber auch andere Plattformen unterstützt
* **Beispiel:**
  * docker run -it --platform=linux/amd64 ubuntu
  * Führt auf einem modernen Mac den Ubuntu-Container als 64-bit x86 Container aus
  * Achtung: Führt zu signifikanten Performance-Overhead, da ein gesamter 
  Prozessor emuliert werden muss!
* **In der Praxis:**
  * Für jede CPU-Architektur funktioniert unser Image u.U. leicht unterschiedlich
  * Wir müssen das als Nutzer also wissen und beachten!