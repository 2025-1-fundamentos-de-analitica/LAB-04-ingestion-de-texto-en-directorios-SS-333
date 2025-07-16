# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa

import os
import zipfile
import pandas as pd
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    # Descomprimir el archivo zip
    if os.path.exists('files/input.zip'):
        with zipfile.ZipFile('files/input.zip', 'r') as zip_ref:
            zip_ref.extractall('.')

    # Crear el directorio de salida si no existe
    if not os.path.exists('files/output'):
        os.makedirs('files/output')

    # Procesar los directorios train y test
    for dataset_type in ['train', 'test']:
        data = []
        data_path = os.path.join('input', dataset_type)
        for sentiment in ['positive', 'negative', 'neutral']:
            sentiment_path = os.path.join(data_path, sentiment)
            if os.path.exists(sentiment_path):
                for filename in os.listdir(sentiment_path):
                    if filename.endswith(".txt"):
                        with open(os.path.join(sentiment_path, filename), 'r', encoding='utf-8') as f:
                            phrase = f.read().strip()
                            data.append({'phrase': phrase, 'target': sentiment})
        
        # Crear DataFrame y guardarlo como CSV
        df = pd.DataFrame(data)
        output_filename = os.path.join('files/output', f'{dataset_type}_dataset.csv')
        df.to_csv(output_filename, index=False)

# --- Bloque para ejecución y prueba ---
# Se llama a la función.
# pregunta_01()