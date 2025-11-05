# Packages

import os
import requests

# Class
class FileDownloader:
    """
    Se trata de una clase que permite la descarga de ficheros de aquellos resultados obtenidos anteriormente durante
    una búsqueda con un dork.
    """

    def __init__(self,ruta_destino):
        """
        Constructor de la clase. Realiza la inicialización de las instancias.

        Args:
            ruta_destino(str): Ruta dentro del equipo local donde se almacenará los diferentes ficheros que descarguemos.
        """
        
        self.ruta_destino = ruta_destino
        self.new_directory()
    
    def new_directory(self):
        """
        En el caso de que no exista la ruta de destino proporcionada, este método se encarga de crearla.
        """

        if not os.path.exists(self.ruta_destino):
            os.makedirs(self.ruta_destino)
            print(f"La ruta de destino proporcionada no existe, por lo que se ha creado dicha ruta: {self.ruta_destino}")
        else:
            print(f"La ruta donde se almacenarán los ficheros es en {self.ruta_destino}")
    
    def downloader(self, url):
        """
        Permite la descarga del fichero correspondiente asociada a la URL aportada.

        Args:
            url(str): Contiene la URL donde se almacena el fichero a descargar.
        """

        try:
            ruta_url = requests.get(url)
            nombre_archivo = url.split("/")[-1] # <- Obtenemos el nombre completo del archivo a descargar.
            ruta_descarga = os.path.join(self.ruta_destino,nombre_archivo)

            with open(ruta_descarga, "wb") as archivo:
                archivo.write(ruta_url.content) # <- Se escribe en la ruta el contenido del fichero que hemos descargado.
            print(f"Se ha llevado a cabo la descarga del archivo {nombre_archivo}, se encuentra en {ruta_descarga}")
        except Exception as exception:
            print(f"Durante la descarga del archivo {nombre_archivo} se ha producido una excepción: {exception}.")

    def parser_filetype(self,urls,filetype = ["all"]):
        """
        Este métido realiza el filtrado de descarga de ficheros en función del formato que se quiera descargar.

        Args:
            urls(list): Lista que contiene el conjunto de URLs donde residen los ficheros que queremos descargar.
            filetype(list): Lista donde se almacena los tipos de ficheros que queremos almacenar.
        """

        try:
            if filetype == ["all"]:
                for url in urls:
                    self.downloader(url)

        # Recorre mediante un bucle FOR y comprueba cada uno de las extensiones de los archivos, y los descarga.
        
            else:
                for url in urls:
                    for type in filetype:
                        if any(url.endswith(f".{tipo}") for tipo in filetype):
                            self.downloader(url)
        except:
            print("Se ha producido una excepción al intentar descargar un archivo con un formato incorrecto")