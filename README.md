# Warum docker lernen

## Motivation

* Oft muss man sicherstellen, dass eine Anwendung mit einer bestimmten 
Version (z.B von Java) Kompatibel ist.
* Man will definieren, wie die Software-Umgebung für eine Anwendung 
eingerichtet werden soll.
* Tools verwenden, deren Einrichtung aufwendig ist.
* Mit Docker Swarm bzw. Kubernetes kann man ein Cluster komfortable adminstrieren.

## Problem: Replizierbarkeit von Anwendungen

* Mögliche Probleme (in unserer Anwendung):
  * Verschiedene Versionen von Java
  * Unterschiedliche Versionen von zusätzlichen Modulen (z.B. swing)
  * Java unterschiedlich kompiliert
  * Unterschiedliche Namen für Zeitzonen
* Mögliche Probleme (generell):
  * Unterschiedliche Versionen von externen Tools
  * Unterschiedliche Behandlung von Groß- und Kleinschreibungen im Dateisystem
  * Unterschiedliche, maximale Länge von Dateipfaden
* Zusätzlich
  * Man muss ausführilch beschreiben, wie der Ubuntu-Server eingerichtet werden soll
  * Dieses Dokument muss dann von IT-Department interpretiert werden, um den 
  * korrekten Zustand vom Ubuntu-Server einrichten zu können