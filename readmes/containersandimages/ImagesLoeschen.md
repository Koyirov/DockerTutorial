## Wie kann man Images löschen?

* Einen tag bzw. ein Image löschen
  * **docker image rm ubuntu-new**
    * dabei wird erstmal nur der als Parameter verwendete tag gelöscht
    * deswegen erhält man als Feedback eine untagged-Info

Alle Images auf einmal löschen:

```
docker image rm $(docker image ls -aq)
```