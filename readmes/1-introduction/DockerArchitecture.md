## Die Architektur von virtuellen Maschine

```
Web-Anwendung 
->
Anwendungssoftware der virtuellen Maschine 
->
Kernel der virtuellen Maschine 
->
Virtuelle Maschine 
->
Virtualisierungssoftware 
->
Anwendungssoftware 
->
Kernel
->
Physikalische Hardware (SPU, RAM, SSD, ...)
```

## Die Architektur von Docker

```
Unsere Web-Anwendung 
->
Anwendungssoftware der virtuellen Maschine 
->
Kernel
->
Physikalische Hardware (SPU, RAM, SSD, ...)
```

* Docker braucht einen Linux-Kernel, um Linux-Container ausführen zu können 
(Windows-Container können nur unter einem Windows-Host ausgeführt werden (Serverlizenz nötig))
* Unter macOS & Windows wird im Hintergrund eine 
virtuelle Maschine mit einer sehr kleinen und optimierten Linux Distribution ausgeführt
  * Overhead bei der Entwicklung vernachlässigbar wegen Deployment auf Linux (in der Regel)
* Unter Windows ist es dank der Virtualisierungssoftware WSL 2 (Windows Subsystem for Linux) 
möglich, Windows- und Linux-Container auf dem gleichen rechner auszuführen.
* Unter Linux kann Docker den Kernel nutzen und somit im Vergleich virtuellen 
Maschinen Redundanzen sparen.