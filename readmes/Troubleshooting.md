## Troubleshooting

* Wenn beim Ausführen docker Befehle solche

```
docker: error during connect: Head "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/_ping": 
open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
```

kommt, das heißt Docker Desktop ist noch nicht gestartet.

* Manchmal wenn man neue Container starten will, kommt die Meldung, dass es 
keinen genügenden Speicherplatz mehr vorhanden ist. In dem Fall hat man die 
Möglichkeit die Ressourcen über Docker Desktop zu verwalten (erhöhen oder vermindern).
```
Docker Desktop -> Einstellungen -> Ressourcen
```

Oder manchmal Docker Desktop Restarten und alte Daten entfernen hilft auch 

```
Docker Desktop -> Troubleshoot -> Restart
```
oder
```
Docker Desktop -> Troubleshoot -> Clean / Purge data (WSL2 auswählen)
```
oder
```
Docker Desktop -> Troubleshoot -> Reset to factory defaults
```

* Verbindung mit laufendem Docker Container über Terminal erstellen

```
ssh adressofcontainer
```

* Manchmal beim Ausführen docker Befehl im Linux Terminal, der Befehl 
wird nicht ausgeführt. In manchen Fällen das liegt an fehlenden Berechtigung.
In dem Fall hilft vor dem Befehl einmal **sudo** anzugeben.

```
sudo docker run -it ubuntu
```