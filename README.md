### Hexlet tests and linter status:
[![Actions Status](https://github.com/AlphaConstuye/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AlphaConstuye/python-project-174/actions/workflows/hexlet-check.yml)

# Gendiff - Difference Generator

**Gendiff** es una herramienta de línea de comandos que compara dos archivos de configuración (JSON o YAML) y muestra sus diferencias en múltiples formatos.

## Características

- Soporta archivos **JSON** y **YAML**
- Maneja **estructuras anidadas** complejas
- **Tres formatos de salida**: stylish, plain, json
- **Comparación recursiva** de objetos anidados
- **CLI amigable** con opciones de formato

## Instalación

```bash
git clone https://github.com/AlphaConstuye/python-project-174
cd python-project-174
poetry install

# Formato stylish (por defecto)
poetry run gendiff file1.json file2.json

# Formato plain
poetry run gendiff file1.yml file2.yml --format plain

# Formato JSON
poetry run gendiff file1.json file2.json --format json

# Comparar formatos mixtos
poetry run gendiff file1.json file2.yml

from gendiff import generate_diff

# Formato stylish (por defecto)
diff = generate_diff('file1.json', 'file2.json')

# Formato plain
diff = generate_diff('file1.json', 'file2.json', 'plain')

# Formato JSON
diff = generate_diff('file1.json', 'file2.json', 'json')


{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
    }
}


Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]

[
  {
    "key": "common",
    "type": "nested",
    "children": [
      {
        "key": "follow",
        "type": "added",
        "value": false
      },
      {
        "key": "setting2",
        "type": "removed",
        "value": 200
      }
    ]
  }
]


Links Asciinema

asciinema upload demo_stylish.cast
View the recording at:

    https://asciinema.org/a/OCSckhEkFnklB2805dgX6QdZ4

asciinema upload demo_plain.cast
View the recording at:

    https://asciinema.org/a/VO9b22WKMMiPVE4htDAdDryOz

asciinema upload demo_json.cast
View the recording at:

    https://asciinema.org/a/fJI3Ah8EonGQ1kDRJxaLTTyDe

