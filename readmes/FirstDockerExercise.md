## Docker Übungen

```
docker run -it node
```

Mit **Strg + C** oder **.exit** den Prozess im Terminal wieder beenden.

### Aufgabe 1:

Nachdem man den Node.js - Container gestartet hat, überprüfen 
die Ausgaben von folgenden JavaScript-Befehlen:

<ol type="a">
  <li>3 > 2 > 1</li>
  <li>typeof NaN;</li>
  <li>[1, 2, 3] + [4, 5, 6]</li>
</ol>

Ergebnis:

<ol type="a">
  <li>false</li>
  <li>number</li>
  <li>[1, 2, 34, 5, 6]</li>
</ol>

### Aufgabe 2:

Starte in Docker einen (neuen) Ubuntu - Container

* Lerne das Ubuntu - Program **tree** kennen
  * Aktualisiere den Paketmanager apt und installiere dann das Programm **tree**
    * Ganz analog wie man den Texteditor nano installiert hat
  * Wechsel anschließend in das Stammverzeichnis:
    * **cd /**
  * Führe dann den Befehl **tree** aus - was passiert, 
  welchen Zweck erfüllt das Programm **tree**?

Ergebnis: Verzeichnisbaum und denen Inhalte wird angezeigt.

### Aufgabe 3:

Starte in Docker einen (neuen) Ubuntu - Container

* Lerne das Ubuntu - Program **cmatrix** kennen
    * Aktualisiere den Paketmanager apt und installiere dann das Programm **cmatrix**
        * Ganz analog wie man den Texteditor nano installiert hat.
    * Hier kann man die Flag **-y** setzen, um eine manuelle Bestätigung zu überspringen.
    * Während der Installation wird man mehrmals aufgefordert Zahlen
      zur Konfiguration einzutragen: es spielt inhaltlich keine Rolle,
      welche der angegebenen Optionen du dich entscheidest.
    * Wechsel anschließend in das Stammverzeichnis:
        * **cd /**
    * Führe dann den Befehl **cmatrix** aus - was passiert,
      welchen Zweck erfüllt das Programm **cmatrix**?

Ergebnis: Es zeigt Text, der in ein Terminal hinein- und herausfliegt, wie im Film 
„Matrix“. Es kann Zeilen mit der gleichen Geschwindigkeit oder asynchron und mit 
einer benutzerdefinierten Geschwindigkeit scrollen. CMATRIX ist vom Film „Matrix“ inspiriert.
