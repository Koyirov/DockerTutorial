## Virtuelle Maschine

### Was ist eine virtuelle Maschine?

*   Virtuelle Maschinen simulieren die komplette Architektur 
eines Rechners und sind vom Host-System abgekapselt.
* Idee: man kann eine virtuelle Maschine auf dem Entwicklungssystem verwenden:
  * diese dann unabhängig
  * und einfach portierbar
* Bekannte Virtualisierungssoftwares:
  * vmware
  * oracle virtualbox

### Was ist ein Kernel?

* Kernel: "Kern eines Betriebssystems".
* Das Program, das die unterste Schicht der Betriebssystem-Software darstellt.
* Das erste Programm, das nach dem Systemstart in den Arbeitsspeicher geladen wird.
* Fungiert als Schnitschtelle zwischen Hardware und der Anwendungssoftware:
  * Verwaltet die CPU-Ressourcen für die Prozesse.
  * Steuert die Zugriffe auf den Speicher und die Geräte(Grafikkarte, Tastatur, ...).

### Was sind die Nachteile von VMs?

* Es wird eine komplette Rechnerarchitektur visualisiert mit Anwendungssoftware und Kernel.
* Tendenziell langsamer als ohne VM.
* Hohe Rechenleistung (Arbeitsspeicher, CPU).
* Größerer Speicherplatz-Verbrauch.
* Oft braucht man aber gar keine komplette virtuelle Maschine.
* <b>Idee für mehr Effizient:</b>
  * Man virtualisiert nur die Anwendungssoftware und nicht den Kernel.
  * Dann würde auch der Overhead wegfallen.