<html lang="en">
<head>
<title>Hello Docker</title>
</head>
<body>
<p>Hallo mit Umgebungsvariable {{ env "HALLO" }}!. Ich bin Service {{ .Service.Name}}, mit Task-ID: {{ .Task.ID }}.</p>
</body>
</html>
