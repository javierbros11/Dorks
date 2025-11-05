# Local Packages

import argparse
import sys

# Local files

from ai_agent_duck import IAagent
from duck_file_downloader import FileDownloader
from results_parser_duck import  Results_parser_duck
from duck_autosearch import BrowserAutoSearch
from ducksearch import DuckDuckSearch
from duck_config import DuckConfig

# Main code

def main(config,engine,query,lang,pages,output_html,output_json,download,gen_dork,selenium):
    """
    Función principal de código, donde se plantea la obtención de la API SEARCH del navegador que deseemos iniciar una búsqueda.
    En este caso DuckDuckGo.
    """

    # Config setup

    configure = DuckConfig(config)
    API_KEY_DUCK = configure.load_env()

    # Params
    params= {
        "engine": engine,
        "q": query,
        "kl": lang,
        "api_key": API_KEY_DUCK
    }
            
    # Conditions
    
    if not engine:
        print("El programa requiere de un navegador para realizar una consulta.\n" \
        "Comprueba el parámetro '-e' o consulte la ayuda con '--help'.")
        sys.exit(1)

    if gen_dork:
            print("Utilizando gpt4all y ejecutando la generación en local. Puede tardar unos minutos...")
            ia_test = IAagent()
            answer = ia_test.generate_dork(gen_dork)
            print(f"\nResultado:\n{answer}")
            sys.exit(1)
    
    if not query:
        print("El programa requiere de una consulta para realizar la búsqueda.\n" \
        "Comprueba el parámetro '-q' o consulte la ayuda con '--help'.")
        sys.exit(1)

    
    elif selenium:
        browser = BrowserAutoSearch()
        browser.search_duck(query)
        results = browser.duck_search_results()
        browser.quit()
        
    else:
        search = DuckDuckSearch(params)
        results = search.search().get_dict()


    # Display the results in command line console

    rparser = Results_parser_duck(results,pages)
    if selenium:
        rparser.mostrar_pantalla_auto()
    else:
        rparser.mostrar_pantalla()
    
    # Export files

    if output_html:
        rparser.export_html(output_html)
    elif output_json:
        rparser.export_json(output_json)

    # Downloader

    if download:

        # Sacamos las extensiones de los archivos que queremos.
        
        filetype = download.split(",")
        
        # Obtenemos las URLs
        
        urls = []
        for indice,resultado in enumerate(results["organic_results"], start=1):
            if indice in range(pages + 1):
                urls.append(resultado["link"])
        descarga = FileDownloader("DuckDorksDownloads")
        descarga.parser_filetype(urls,filetype)

if __name__ == "__main__":

    # Configuration of program arguments

    # Program description
    
    parser = argparse.ArgumentParser(description="Esto es una herramienta que permite realizar hacking con búscadores a través del servicio de DuckDuckGo.")
    parser.add_argument("-c","--configure",action="store_true",
                        help="Indica si existe el archivo de configuración .env para posteriormente cargarlo en el programa.\n")
    parser.add_argument("-e","--engine",type=str,
                        help="Indica el motor de búsqueda que se usará para realizar peticiones. Por ejemplo: 'duckduckgo'.\n")
    parser.add_argument("-q","--query",type=str,
                        help="Indica la consulta que queremos realizar en el buscador. Por ejemplo: 'filetype:sql \"MySQL dump\" (pass|password|passwd|pwd)'.\n")
    parser.add_argument("--lang",type=str,default="es-es",
                        help="Código de idioma de cara a los resultados de búsqueda. Por defecto: 'es-es'.\n")
    parser.add_argument("--pages",type=int,default=10,
                        help="Es el número de páginas en total que se desean consultar. Cada página consta de 10 resultados de búsqueda.\n")
    parser.add_argument("--html",type=str,
                        help="Exporta los resultados en formarto HTML indicando el nombre del archivo con su extensión .html. Se almacena en la misma ruta que el programa principal.\n")
    parser.add_argument("--json",type=str,
                        help="Exporta los resultados en formato JSON, indicando el nombre del archivo con su extensión .json. Se almacena en la misma ruta que el programa principal.\n")
    parser.add_argument("--download", type=str,
                        help="Permite la descarga de ficheros, indicando previamente la extensión de los archivos que se desean descargar. Ejemplo: --download 'pdf,sql,doc'\n Si deseas descargar todos los formatos de archivos. Ejemplo: --download 'all'\n")
    parser.add_argument("-gd","--generate-dork", type=str,
                        help="Genera un Dork a través de una descripción otorgada por el usuario. GPT4All será el encargado de generar dicha consulta." \
                        "Por ejemplo: --generate-dork 'Listado de usuarios y passwds en un fichero de texto.'\n")
    parser.add_argument("--selenium",action="store_true",
                        help="Permite realizar una consulta con Selenium, imitando el comportamiento humano a la hora de realizar cualquier búsqueda.\n")
    
    # Definition of arguments
    
    args = parser.parse_args()
    
    #Calling the main function
    
    main(config=args.configure,engine=args.engine,query=args.query,lang=args.lang,pages=args.pages,
         output_html=args.html,output_json=args.json, download = args.download,gen_dork = args.generate_dork,selenium=args.selenium)