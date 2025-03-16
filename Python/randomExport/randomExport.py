import os
import random
from pydub import AudioSegment
from tqdm import tqdm  # Importar tqdm para la barra de progreso


# Función para procesar la carpeta de archivos de audio

def concatenate_audios(input_folder, output_file):

    # Lista para almacenar todos los archivos de audio

    audio_files = []

    # Recorrer todos los archivos de la carpeta

    for file_name in os.listdir(input_folder):

        if file_name.endswith(".wav"):
            file_path = os.path.join(input_folder, file_name )
            audio_files.append(file_path)

    # Ordenar aleatoriamente los archivos

    random.shuffle(audio_files)

    # Crear una instancia final vacía para el audio final concatenado
    final_audio = AudioSegment.empty()

    # Crear un segundo de silencio
    one_second_silence = AudioSegment.silent(duration=2000)


    # Usar tqdm para crear una barra de progreso
    with tqdm(total=len(audio_files), desc ="Procesando audios") as pbar:


    #Recorrer cada archivo y concatenarlos
        for audio_file in audio_files:
            # Cargar el archivo de audio
            audio = AudioSegment.from_wav(audio_file)

            # Añadir el audio al final del audio concatenado
            final_audio += audio

            # Añadir un segundo de silencio
            final_audio += one_second_silence

            # Actualizar la barra de progreso
            pbar.update(1)

    # Exportar el archivo final en formato mp3
    final_audio.export(output_file, format="mp3")

# Ruta de la carpeta de entrada y archivo de salida

input_folder = "/home/teqkat/Downloads/Audios/Camino/"
output_file = "Camino.mp3"

# Llamar a la funcion para procesar y exportar
concatenate_audios(input_folder, output_file)

print("Concatenacion completada")
