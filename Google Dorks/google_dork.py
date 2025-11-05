# Local Packages

import argparse
import sys

# Local files

from google_config import GoogleConfig
from browserautosearch_bing import BrowserAutoSearch
from ai_agent_google import IAAgent
from google_file_downloader import FileDownloader
from googlesearch import GoogleSearch
from results_parser import ResultsParser


# Main Code

def main(query,configure_env, start_page, pages, lang,output_html,output_json,download,gen_dork,selenium):
    """
    Función principal de código, donde se plantea la obtención de la API SEARCH del navegador que deseemos iniciar una búsqueda.
    En este caso Google, si se trata de realizar una búsqueda con selenium será a través de Bing.
    """

    # Config setup

    configure = GoogleConfig(configure_env)
    API_KEY_GOOGLE, SEARCH_ENGINE_ID = configure.load_env()

    # Conditions

    if gen_dork:
        print("Utilizando gpt4all y ejecutando la generación en local. Puede tardar unos minutos...")
        ia_agent = IAAgent()
        answer = ia_agent.generate_gdork(gen_dork)
        print(f"\nResultado:\n{answer}")
        sys.exit(1)

    if not query:
        print("Indica una consulta con el comando -q. Utiliza el comando -h para ver la ayuda")
        sys.exit(1)

    elif selenium:
        browser = BrowserAutoSearch()
        browser.search_bing(query=query)
        resultados = browser.bing_search_results()
        
    
    else:
        search = GoogleSearch(API_KEY_GOOGLE,SEARCH_ENGINE_ID)
        resultados = search.search(query,start_page=start_page,pages = pages,lang=lang)
    
    # Display the results in command line console

    rparser = ResultsParser(resultados)
    rparser.mostrar_pantalla()

    # Export files

    if output_html:
        rparser.exportar_html(output_html)
    elif output_json:
        rparser.exportar_json(output_json)

    # Downloader

    if download:
        
        file_types = download.split(",")
        
        urls = [resultado['link'] for resultado in resultados]
        descarga_ficheros = FileDownloader("GoogleDorksDownloads")
        descarga_ficheros.filtra_descarga(urls,file_types)

if __name__ == "__main__":

    # Configuration of program arguments

    # Program description

    parser = argparse.ArgumentParser(description = "Esta herramienta permite realizar Hacking con buscadores de forma automática. En este caso emplearemos principalmente el buscador de Google Chrome/Bing.")

    # Program Arguments
    
    parser.add_argument("-q","--query", type=str,
                        help="Indica la consulta que queremos realizar en el buscador. Por ejemplo: 'filetype:sql \"MySQL dump\" (pass|password|passwd|pwd)'.\n")
    parser.add_argument("-c", "--configure", action="store_true",
                        help="Inicia el proceso de configuración del archivo .env. Utiliza esta opcion sin otros argumentos para configurar las claves.\n")
    parser.add_argument("--start-page", type=int, default=1,
                        help="Define la página de incio del buscador donde empezará a recibir resultados.\n")
    parser.add_argument("--pages",type=int,default=1,
                        help="Es el número de páginas en total que se desean consultar. Cada página consta de 10 resultados de búsqueda.\n")
    parser.add_argument("--lang",type=str,default="lang_es",
                        help="Código de idioma de cara a los resultados de búsqueda. Por defecto es 'lang-es' (español)\n")
    parser.add_argument("--html",type=str,
                        help="Exporta los resultados en formarto HTML indicando el nombre del archivo con su extensión .html. Se almacena en la misma ruta que el programa principal.\n")
    parser.add_argument("--json",type=str,
                        help="Exporta los resultados en formato JSON, indicando el nombre del archivo con su extensión .json. Se almacena en la misma ruta que el programa principal.\n")
    parser.add_argument("--download", type=str,
                        help="Permite la descarga de ficheros, indicando previamente la extensión de los archivos que se desean descargar.\nEjemplo: --download 'pdf,sql,doc'\n Si deseas descargar todos los formatos de archivos. Ejemplo: --download 'all'\n")
    parser.add_argument("-gd","--generate-dork", type=str,
                        help="Genera un Dork a través de una descripción otorgada por el usuario. GPT4All será el encargado de generar dicha consulta." \
                        "Por ejemplo: --generate-dork 'Listado de usuarios y passwds en un fichero de texto.'\n")
    parser.add_argument("--selenium",action="store_true", default=False,
                        help="Permite realizar una consulta con Selenium, imitando el comportamiento humano a la hora de realizar cualquier búsqueda.\n")
    
    # Definition of arguments

    args = parser.parse_args()
    
    # Calling the main function

    main(query = args.query,configure_env=args.configure,start_page=args.start_page,pages=args.pages,
         lang=args.lang,output_html=args.html,output_json=args.json,download=args.download,
         gen_dork = args.generate_dork,selenium = args.selenium)