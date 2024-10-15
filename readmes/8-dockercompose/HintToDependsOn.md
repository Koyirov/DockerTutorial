## Hinweis zu depends_on

Vor Version v2.19 verhielt sich **depends_on** wie folgt:
Es spielte keine Rolle, ob ein Container von einem anderen 
Container abhängig war. Docker startete die Container 
trotzdem, selbst wenn der über **depends_on** angegebene 
Container nicht gestartet wurde.

Ab Version v2.19 hat sich das Verhalten von **depends_on** geändert:
Der Container wird nicht gestartet, wenn eine Abhängigkeit mit 
**depends_on** festgelegt ist und der angegebene Container nicht 
gestartet ist. Hier würden wir dann eine Fehlermeldung erhalten, 
die ungefähr so aussieht:

```
service db is required by pma but is disabled. Can be enabled by profiles
```

Es besteht jedoch die Möglichkeit, das im Video gezeigte Verhalten 
zu reproduzieren. Hierzu müssen wir dem **depends_on** die Optionen 
"**condition**" und "**required**" hinzufügen:

````yaml
pma:
  image: phpmyadmin
  environment:
    PMA_HOST=db
  depends_on:
    db:
      condition: "service_started"
      required: false
````

Diese Konfiguration ermöglicht es, dass der Container **pma** gestartet wird, selbst 
wenn die abhängigen Dienste (hier der Container **db**) nicht gestartet sind.