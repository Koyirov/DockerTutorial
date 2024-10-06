## Hinweis für die nächste Lektion

### Debian 12 und Python 2

In der kommenden Lektion werden wir einen Debian-Container 
mit Python 3 erstellen, aber auch mittels einer Build-Variable 
die Installation von Python 3 auf Python 2 ändern.

Da wir in der Dockerfile **FROM debian** nutzen, wird Docker das 
aktuellste Debian-Image herunterladen. In der Zwischenzeit 
wurde Debian jedoch von Version 11 (*bullseye*) auf 12 (*bookworm*) 
aktualisiert. Ab Debian 12 wurde der Support für Python 2 
eingestellt. Das bedeutet, dass die Installation von Python 2 
nicht mehr ohne Weiteres möglich ist.

In dieser Situation können wir jedoch den Vorteil von Docker 
nutzen, indem wir einfach eine ältere Version von Debian verwenden. 
Dazu müssen wir lediglich in der Dockerfile die gewünschte 
Debian-Version angeben, z.B. **FROM debian:11**

Dadurch wird der Container mit Debian 11 erstellt, und wir können 
Python 2 problemlos installieren und verwenden. Dass ein solches 
Downgrade auf eine ältere Version von Debian so einfach möglich 
ist, zeigt gut die Flexibilität von Docker!