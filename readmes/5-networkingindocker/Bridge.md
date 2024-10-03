## Bridge

Ermöglicht die Kommunikation zwischen eigenständigen (standalone)
Containern bei Isolation von Containern von außerhalb
* Genauer wird dabei ein privates Subnetz angelegt mit IP-Adressen der Form 172.?.?.?
* Container müssen dazu auf demselben Host laufen (bei uns bisher immer der Fall)
* Wenn wir nichts angeben, landet ein Container im bridge-Netzwerk
* Wenn ein Port vom Host aus weitergeleitet werden soll, müssen wir dies
  manuell angeben (Parameter: -p)