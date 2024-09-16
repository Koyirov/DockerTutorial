## Das Kommando **docker pull**

* Mit dem Pull-Befehl können wir ein Image herunterladen
  * **docker pull** [Quelle]/[Name von Image]
  * Die Quelle braucht man nur spezifizieren, wenn man eine andere Container 
  Registry als Docker verwenden möchtet.
  * Sonst wird standardmäßig auf Docker Hub gesucht und man kann die Quelle
  somit auch weglassen.
  * Man muss das Image auf **https://hub.docker.com** finden.
    * Auf der Übersichtsseite ist der benötigte Pull-Befehl angegeben, hier: 
      * **docker pull ubuntu**
        * Wir sehen. ist bereits heruntergeladen worden
      * **docker pull alpine**
        * Alpine ist eine besonders kleine Linux-Distribution, 
        die häufig als Basis für Docker-Container verwendet wird.


## Docker-Kommandos via CLI
* Wenn der Docker Deamon läuft, kann man Eingabeaufforderungen (Windows) bzw 
den Terminal macOS öffnen, um Docker per CLI zu nutzen
* In der Regel besteht ein Docker-Kommando aus 4 Bestandteilen
  * Das Schlüsselwort **docker**
  * Auf welche Art von Objekt man sich bezieht, z.B. conatiner, image, ...
    * Kann auch manchmal weggelassen werden
  * Was man machen möchtet: z.B: **pull** (ein image herunterladen)
  * Parameter für den Befehl: z.B. welches Image man herunterladen möchtet (**image, python**)
  * Zusätzlich kann oder muss manchmal noch flags gesetzt werden