## Einen Port mittels Flag *-p* veröffentlichen

* Wir führen Docker auf localhost (127.0.0.1) aus.
* Jeder Container besitzt eine eigene (virtuelle) Netzwerk-Schnittstelle.
* Standardmäßig werden Ports vom Host nicht an den Container weitergeleitet.
* Dadurch können z.B. mehrere Container jeweils Port 80 verwenden.
* Mit der Flag **-p** (oder **--publish**) kann man den Port eines 
Containers veröffentlichen, um mit Diensten außerhalb von Docker
  (z.B. deinen Browser) auf den Container zuzugreifen,
  * Mann kann sich das so vorstellen: Man leitet einen Port von Host 
  zu einem Port auf dem Container weiter:
    * **docker run -p Host-Port:Container-Port Image-Name**
    * Die beiden Ports können natürlich unterschiedlich sein


### Einen nginx - Webserver starten

* **Nginx** ist eine weit verbreitete Software für Webserver (Marktanteil: 
ca. 44% unter den 10.000 meistbesuchten Webseiten)
* **docker run -p 8888:80 --rm nginx**
* Danach kann man im Browser vie http://localhost:8888 den Webserver
auf dem Port 8888 ansteuern.
* Man kann auch andere Ports freigeben, z.B. 8080.
* Der Container-Port muss allerdings 80 (HTTP) lauten, da nginx 
standardmäßig auf Port 80 lauscht.