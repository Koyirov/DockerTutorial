## Container automatisch starten

* Standardmäßig wird ein Container nicht erneut gestartet
* Man kann aber die **restart policy** auf folgende Werte setzen:
  * **on-failure[:max-retries]**: Startet den Container neu, wenn es einen Error gibt
  * **always**: Der Container wird immer neu gestartet (es sei denn, wir stoppen ihn,
  dann wird er erst beim nächsten Start vom Docker Daemon erneut gestartet)
  * **unless-stopped**: Der Container wird immer neu gestartet (und wenn wir ihn
  stoppen, bleibt er gestoppt)
* Wie setzt man die restart policy?
  * **docker run -d --restart unless-stopped [Image-Name]**
  * **docker update -d --restart unless-stopped [Image-Name]**
  * **docker update -d --restart always [Image-Name]**
  * **docker update --restart on-failure:5 [Image-Name]**