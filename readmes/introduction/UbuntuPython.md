## Ubuntu container starten

```
docker run -it ubuntu
```

Ubuntu container wird gestartet und wir landen in ubuntu container. 
Wir können dann ganz normale linux Befehle im Terminal ausführen:

```
ls -al
```

## Python container starten

```
docker run -it python
```

Python container wird gestartet und wir landen in Python container.
Wir können dann ganz normale Python Code im Terminal ausführen:

```
print("Hallo Welt")
exit()
```

## Python container mit bestimmten Version starten

```
docker run -it python:3.8
```

or

```
docker run -it python:2
```

Python container wird gestartet und wir landen in Python container.
Wir können dann ganz normale Python Code im Terminal ausführen:

```
print("Hallo Welt")
exit()
```