## Templated Configs in Docker Swarm

* Docker Swarm kann auch eine Template-Engine auf unsere Konfigurationsdatei anwenden
* Beispiel:
````html
<html lang="en">
    <head>
        <title>Hello Docker</title>
    </head>
    <body>
        <p>Hallo mit Umgebungsvaribable {{env "HALLO"}}!. Ich bin Service {{
            .Service.Name}}, mit Task-ID:{{.Task.ID}}.</p>
    </body>
</html>
````

* Diese kann dan wie folgt hinzugefügt werden:
  * **docker config create --template-driver golang [config-name] index.html.tmpl**