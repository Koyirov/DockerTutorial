## Der Aufbau von kubectl - Kommandos

Im Allgemeinen haben **kubectl**-Kommandos folgenden Aufbau:

* **kubectl**

* **[Aktion: was möchtest du tun?]**: z.B. create, apply, edit usw.

* **[Objekttyp: auf welche Art von Objekt bezieht sich die Aktion?]**: deployment, pod usw.

* **[Objektname]**

* **[Zusätzliche Flaggen]**: z.B. **--replicas=10**, **--port=80** usw.

Statt zwischen dem *Objekttyp* und dem *Objektnamen* ein Leerzeichen 
zu setzen (**deployment nginx-deployment**), kannst du auch gleichbedeutend, 
so wie im vorherigen Video gesehen, einen Schrägstrich schreiben 
(**deployment/nginx-deployment**).

Es spielt also keine Rolle, ob du das Kommando

```shell
kubectl edit deployment/nginx-deployment
```

oder aber das Kommando

```shell
kubectl edit deployment nginx-deployment
```

verwendest.