## Das Kommando **EXPOSE**

* Mit **EXPOSE [PORT]** bzw. **EXPOSE [PORT]/[PROTOCOL]** können wir
spezifizieren, dass dieser Container z.B. auf einem Port lauschen soll
* So wirklich viel macht das Kommando aber nicht:
  * Man kann auch so einen Port auf unserem Container öffnen
  * Man kann auch so einen Port über **-p** vom Host zum Container weiterleiten
  * Allerdings: Wenn man bei docker run alle Ports automatisch mappen
  möchten (Option: **-P**), dann werden nur Ports verwendet, die mit **EXPOSE**
  angegeben worden sind
  * **Beispiele:**
    * EXPOSE 80/tcp
    * EXPOSE 443/tcp 
    * EXPOSE 80/tcp
    * EXPOSE 443