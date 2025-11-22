### Hexlet tests and linter status:
[![Actions Status](https://github.com/AlphaConstuye/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AlphaConstuye/python-project-174/actions)


# gendiff

**gendiff** es una herramienta de línea de comandos que compara dos archivos de configuración y muestra sus diferencias de forma clara y estructurada.  
Actualmente soporta archivos **JSON** y presenta las diferencias en un formato legible tipo “stylish”.

---

## Características

- Compara archivos JSON.
- Muestra qué claves fueron:
  - Eliminadas (`-`)
  - Agregadas (`+`)
  - Modificadas
  - Sin cambios
- Ordena las claves alfabéticamente.
- Puede usarse tanto:
  - Desde la línea de comandos
  - Como biblioteca dentro de un script Python

---

## Instalación

Clona este repositorio:

```bash
git clone https://github.com/AlphaConstuye/python-project-174
cd python-project-174

## Video demostración:
 https://asciinema.org/a/UFayigku3W3FhrwEJxMYLmana

## Soporte para formatos

Ahora soporta tanto JSON como YAML:

```bash
# Comparar archivos JSON
gendiff file1.json file2.json

# Comparar archivos YAML
gendiff file1.yml file2.yaml

# Comparar formatos mixtos
gendiff file1.json file2.yml

## Soporte para YAML

El comparador ahora soporta archivos YAML (.yml y .yaml):

```bash
gendiff file1.yml file2.yaml
