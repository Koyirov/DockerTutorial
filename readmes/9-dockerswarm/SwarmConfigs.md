## Configs

* Oft möchten wir auch Konfigurationsdateien im Cluster verteilen
* Das funktioniert über Configs
* Diese funktionieren ähnlich wie Secrets:
  * **docker config create [Dateiname]**
* Weitere Befehle:
  * **docker config ls**
  * **docker config rm**
* Können bis zu 500kb groß sein
* Wo ist der Unterschied zwischen Secrets und Configs?
  * Secrets: Werden verschlüsselt gespeichert, und intern als
  RAM-Disk gemounted
  * Configs: Werden unverschlüsselt gespeichert und als 
  ohne RAM-Disk gemounted