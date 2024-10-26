## Einen neuen *Service* erstellen

* Der schnellste Weg einen passenden Service aufzusetzen ist das Kommando
  * **kubectl expose deployment [Name von deinem Deployment] --port=[PORT]**
    * Bei uns: **kubectl expose deployment nginx-deployment --port=80**
* Nun können wir im Browser auf nginx mittels minikube(!) zugreifen:
  * **minikube service nginx-deployment**