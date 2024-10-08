## Sicherheitshinweise: ENV und ARG

* Wenn wir über **ENV** oder **ARG** Parameter definieren, sind
diese später immer einsehbar (z.B. über die docker image history)
* Man sollte diese also nur für unsensible Informationen verwenden
* Mann sollte sich also bewusst sein, wenn man z.B. das Image später
an Dritte übertragen