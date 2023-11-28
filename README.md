# To One File 
Sencilla herramienta, un script pyhton que recorre el árbol de directorios de tu proyecto y genera un archivo de texto con la información de cada archivo existente. Ideal para consolidar código para usarlo en chat GPT, por ejemplo.


* excluye los directorios y archivos que no deseas consolidar editando el archivo toonefile.py
```python
exclusions = ["__pycache__", "envpy", "result.txt"]
```
* Define el path inicial, en el ejemplo recorre todo el directorio actual
```python
main_folder_path = './'
```

* ejecuta el script
```python
  python toonefile.py
```
* abre el archivo result.txt

