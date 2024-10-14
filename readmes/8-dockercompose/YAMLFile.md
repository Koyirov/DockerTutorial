## Was ist YAML?

* Ziel: Daten für Menschen gut lesbarer Form darstellen
* **YAML** steht für **Y**aml **a**in't **M**arkup **L**anguage
* Vereinfachte Auszeichnungssprache ("markup language")
  * ähnlich wie **XML** oder **JSON**
  * Jedes JSON-Dokument ist ein gültiges YAML-Dokument
* Endungen: **.yml** oder **.yaml**
* Kannst du prinzipiell in allen Programmiersprachen nutzen,
sofern ein passender Parser vorhanden ist


### YAML Basics

* Wir brauchen nur wenige Elemente von YAML
  * **Einrückungen** legen Strukturen fest!
  * Die wichtigsten Datenstrukturen für uns sind:
    * **Arrays**
    * **Maps**
  * **Datentypen sind quasi wie in JSON:**
    * Zahlen
    * Booleans
    * Strings
  * Website to exercise YAML:
    * https://www.json2yaml.com

Wert in Variable speichern in YAML

```
name: &student Max Mustermann

base_student: *student
```

### JSON and YAML equivalent Code

```
{
  "json": [
    "rigid",
    "better for data interchange"
  ],
  "yaml": [
    "slim and flexible",
    "better for configuration"
  ],
  "object": {
    "key": "value",
    "array": [
      {
        "null_value": null
      },
      {
        "boolean": true
      },
      {
        "integer": 1
      },
      {
        "alias": "aliases are like variables"
      },
      {
        "alias": "aliases are like variables"
      }
    ]
  },
  "paragraph": "Blank lines denote\nparagraph breaks\n",
  "content": "Or we\ncan auto\nconvert line breaks\nto save space",
  "alias": {
    "bar": "baz"
  },
  "alias_reuse": {
    "bar": "baz"
  }
}
```
and
```
---
# <- yaml supports comments, json does not
# did you know you can embed json in yaml?
# try uncommenting the next line
# { foo: 'bar' }

json:
  - rigid
  - better for data interchange
yaml:
  - slim and flexible
  - better for configuration
object:
  key: value
  array:
    - null_value: null
    - boolean: true
    - integer: 1
    - alias: aliases are like variables
    - alias: aliases are like variables
paragraph: |
  Blank lines denote
  paragraph breaks
content: |-
  Or we
  can auto
  convert line breaks
  to save space
alias:
  bar: baz
alias_reuse:
  bar: baz 
```