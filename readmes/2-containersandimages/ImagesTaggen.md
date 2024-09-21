## Wie kann man ein Image taggen

* Ein Image kann Nicht umbenannt werden, aber man kann es mit einem **tag** versehen,
um das Image dann darüber anzusteuern.
  * **docker image tag [Name von Image][neuer tag für Image]**
    * **docker image tag ubuntu ubuntu-new**
    * Die tags tauchen dann als Metadaten auch bei **docker image inspect** für das Image auf:
      * **docker image inspect -f="{{.RepoTags}}" ubuntu**