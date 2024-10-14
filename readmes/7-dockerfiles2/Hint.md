## Hinweis zur nächsten Lektion

In der nächsten Lektion werden wir LABELs hinzufügen. Wenn 
du dies in der PowerShell unter Windows machst, musst du 
die Anführungszeichen u.U. noch Escape'n, d.h. einen 
Backslash davorstellen. Damit verhinderst du, dass 
diese Anführungszeichen vom Terminal verarbeitet werden:

```
docker image inspect -f '{{index .Config.Labels \"eu.codingcoursestv.courses.server\"}}'
```