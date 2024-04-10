import json

def JsonLectura(ruta):
    # Abre el archivo en modo lectura y carga el contenido JSON en un diccionario
    with open(f'{ruta}', "r") as archivo:
        jsdic= json.load(archivo)
    return jsdic

def JsonGuardar(ruta, jsdic):
    # Abre el archivo en modo escritura y guarda el diccionario como JSON
    # jsdic es un dict()
    with open(ruta, "w") as archivo:
        json.dump(jsdic, archivo)