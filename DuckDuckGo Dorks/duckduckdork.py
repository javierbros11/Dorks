from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

# Cargamos las variables en el entorno
load_dotenv()

# Leer las variables del entorno en nuestro programa (API -> 100 peticiones/dia ID -> Engine_ID)
API_KEY_DUCK = os.getenv("API_KEY_DUCK")

# Parámetros
params = {
    "engine" : "duckduckgo",
    "q" : "marca.com",
    "kl" : "es-es",
    "api_key" : API_KEY_DUCK
}

busqueda = GoogleSearch(params)
results = busqueda.get_dict()
print(results)