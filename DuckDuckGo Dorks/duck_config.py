# Packages

from dotenv import load_dotenv,set_key
import os
import sys

# Class

class DuckConfig:
    """
    Realiza la configuración del archivo .env.
    """

    def __init__(self,configure_env):
        """
        Inicializa los atributos de instancia.
        Args:
            configure_env(bool): Indica si se quiere configurar las APIs.
        """
        self.configure = configure_env

    def _env_config(self):
        """
        Comprueba si existe el archivo de configuración, en caso contrario, lo crea de cero.
        """

        api_key = input("Dime tu API_KEY para realizar la búsqueda a tu nombre: ")
        set_key(".env","API_KEY_DUCK",api_key)

    def load_env(self):
        """
        Cargamos el entorno y se comprueba si el archivo .env se ha creado satisfactoriamente.
        """

        # Comprobamos archivo .env
        env_exists = os.path.exists(".env")

        if not env_exists or self.configure:
            self._env_config()
            print("Archivo .env configurado satisfactoriamente.")
            sys.exit(1)
        
        else:
            print("El archivo .env ya estaba creado.\n Cargando las APIs de entorno...")
    
        # Cargamos las variables en el entorno S.O
        load_dotenv()

        # Una vez cargado el entorno extraemos la API
        API_KEY_DUCK = os.getenv("API_KEY_DUCK")

        print("API de entorno cargada satisfactoriamente.")
        return API_KEY_DUCK
