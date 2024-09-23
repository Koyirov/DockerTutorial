## Was sind Ports?

* Unterschied zwischen einer IP-Adresse und einem Port:
  * IP-Adresse: bezieht sich auf ein Gerät in einem Netzwerk
    * IPv4, z.B. 115.235.253.146 (4x Dezimalzahlen, 0-255)
    * Ipv6, z.B. 2014:0db8:85a5:000:000:8b2e:0432:3562 (8x Hexadezimalzahlen)
  * Port: bezieht sich auf einen Prozess auf einem Gerät in einem Netzwerk
    * Insgesamt gibt es 65.535 die Port Nummern, standardmäßig werden z.B. folgende Ports
    * für folgende Protokolle verwendet:
      * Port 22: SSH
      * Port 80: HTTP
      * Port 443: HTTPS
  * Oft werden IP-Adresse und Port kombiniert geschrieben z.B. 115.235.253.146:80
  * Wenn man versucht einen weiteren Prozess auf einen Port zu starten, auf dem 
  bereits ein Prozess läuft, kommt es zu einer **port collision**
    * Lösung: einen anderen Port wählen
  * *Manchmal können auch Berechtigung fehlen, um bestimmte Ports öffnen zu können*