## Das Projekt in diesem Abschnitt

In diesem Abschnitt werden wir mit einem Projekt arbeiten. 
Das Projekt stelle ich dir hier als Lektionsanhang als .zip-Datei 
zur Verfügung.

Du kannst diese Datei bei dir entpacken, und im Terminal in diesen 
Ordner wechseln. Dort kannst du das Projekt dann mit folgendem 
Befehl starten:

```
docker run -it -p 3000:80 -v $(pwd):/usr/share/nginx/html nginx
```

### Wichtiger Hinweis: Der Fehler "invalid reference format"

**Ein kleiner Hinweis:**

Solltest du PowerShell verwenden, kann es sein, dass dir beim Ausführen 
der Befehle in diesem (oder zukünftigen) Abschnitten ein kleiner Fehler 
angezeigt wird:

```
docker: invalid reference format
```

Das liegt daran, dass die PowerShell den Befehl **\$(pwd)** nicht kennt - innerhalb 
der PowerShell muss dieser als **\${pwd}** geschrieben werden.

Mit diesem Teil-Befehl wird an diese Stelle der Pfad zum aktuellen Ordner 
eingesetzt - es wird also der aktuelle Pfad ermittelt (über pwd) und an 
diese Stelle eingesetzt.

Dieser Befehl wird von der Shell verarbeitet, bevor Docker überhaupt 
den Parameter entgegennimmt. Für Docker ist dies immer noch 1:1 der 
gleiche Befehl - je nach Shell aber unterschiedlich geschrieben.

PS: Sollte auch dies nicht klappen, so musst du den gesamten Pfad 
(z.B. **'C:\Users\Jannis\Desktop'** statt **\$(pwd)**) im Terminal angeben.