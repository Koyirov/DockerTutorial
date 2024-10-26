## Service als .yaml

* Wir können Services auch in einer .yaml-Datei spezifizieren:

````yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
  labels:
    app: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 80
      protocol: TCP
  selector:
    app: nginx
````