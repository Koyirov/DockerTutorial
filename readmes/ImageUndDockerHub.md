## Was ist ein Image?

* Container werden auf Basis von Images erstellt
* Man kann ein Image als Bauplan für Container vorstellen

```
Zum Vergleich: Image (Java Klasse) => Instanzierung => Container (Objekt)
```

* Images sind Pakete mit allen erforderlichen Daten (Dependencies, Konfigurationen),
um einen Container zu bauen.
* Images sind nach ihrem Erstellen unveränderlich (read-only-Dateisystem).


## Wie kommt man an Images?
* **Container Registries** sind Server, die Images bereitstellen
  * Beispiel **Docker Hub**: Plattform mit einer Vielzahl öffentlicher Images:
    * https://hub.docker.com/
  * Plattform wird von Docker, Inc. betrieben
  * Images sind kostenlos und werden von der Community bereitgestellt.
    * **Auf official Image achten!**
    * **Auch Anzahl der Downloads berücksichtigen**
    * Man braucht dich NICHT anmelden, solange man nicht selbst Images veröffentlichen möchtet.
    * Jeder angemeldete Nutzer darf eigene Images auf Docker Hub veröffentlichen.

Der Befehl, um die Images aus **Docker Hub** ziehen:

```
docker pull imageName
```