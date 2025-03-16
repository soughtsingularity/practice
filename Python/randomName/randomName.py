import os
import random
import string

def generar_nombre_aleatorio(length=6):
    """Genera un nombre aleatorio de 'length' caracteres."""
    letras = string.ascii_letters + string.digits  # Letras mayúsculas, minúsculas y dígitos
    return ''.join(random.choice(letras) for _ in range(length))

def renombrar_archivos(directorio):
    """Renombra todos los archivos de un directorio con nombres aleatorios."""
    try:
        # Iteramos sobre los archivos en el directorio
        for nombre_archivo in os.listdir(directorio):
            # Creamos la ruta completa del archivo
            ruta_archivo = os.path.join(directorio, nombre_archivo)
            
            # Verificamos que sea un archivo y no un directorio
            if os.path.isfile(ruta_archivo):
                # Generamos un nuevo nombre de archivo con 6 caracteres y mantenemos la extensión
                extension = os.path.splitext(nombre_archivo)[1]  # Extraemos la extensión del archivo
                nuevo_nombre = generar_nombre_aleatorio() + extension
                
                # Renombramos el archivo
                nueva_ruta = os.path.join(directorio, nuevo_nombre)
                os.rename(ruta_archivo, nueva_ruta)
                print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")
    except Exception as e:
        print(f"Error al renombrar archivos: {e}")

# Ruta del directorio que contiene los archivos
directorio = '/home/teqkat/Downloads/Camino/'  # Cambia esto por el directorio donde están tus archivos

# Llamamos a la función
renombrar_archivos(directorio)
