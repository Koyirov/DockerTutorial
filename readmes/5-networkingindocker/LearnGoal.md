## Lernziele für diesen Abschnitt

* Wie kann man mit Docker mehrere Container miteinander verbinden?
* Wie richtet man ein Netzwerk ein, in dem mehrere Container
miteinander kommunizieren kann?
* Was sind *bridge*-Netzwerke und welche anderen Netzwerk-Arten gibt es noch?


## Kommunikation zwischen Containern

* Wir wollen mehrere (eigenständig) laufenden Containern miteinander verbinden
* In Docker läuft jeder Dienst i.d.R. in einem eigenen Container
* **Beispiel:**
  * 1 Container für MySQL bzw. MariaDB
  * 1 Container für phpmyadmin (Verwaltungssoftware für MySQL/MariaDB)
  * 1 Container für Wordpress
* Aber wie verbinden wir die Container?
* Lösung: **Wir richten ein Netzwerk ein!**
* Die Interaktion zwischen mehreren Containern ist eine der größten Stärken von Docker 
und macht die Container-Technologie so mächtig.


## Netzwerk-Treiber in Docker

* Standardmäßig laufen bereits einige Netzwerke in docker
  * **docker network ls**
  * Die Standard-Netzwerke heißen: **bridge**, **host** und **none**
    * Später werden noch weitere dazu kommen
  * Jedes **Netzwerk** hat einen eigenen **Namen** sowie eine **Network ID**
  * genauer gibt es verschiedene Netzwerk-Treiber (Driver) und 
  für jeden davon ein Standard-Netzwerk
  * Diese Treiber fungieren als Vorlagen, die das Verhalten von Containern spezifizieren
  * Wie üblich können wir mit dem Kommando **docker inspect** ein Netzwerk genauer untersuchen
    * **docker netzwerk inspect bridge**

## Welche Netzwerk-Treiber gibt es in Docker?

* **Bridge:** ermöglicht die Kommunikation zwischen eigenständigen (standalone) 
Containern bei Isolation von Containern von außerhalb
  * Genauer wird dabei ein privates Subnetz angelegt mit IP-Adressen der Form 172.?.?.?
  * Container müssen dazu auf demselben Host laufen (bei uns bisher immer der Fall)
  * Wenn wir nichts angeben, landet ein Container im bridge-Netzwerk
  * Wenn ein Port vom Host aus weitergeleitet werden soll, müssen wir dies 
  manuell angeben (Parameter: -p)
