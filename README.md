# Google/DuckDuckGo Dorks

Este repositorio consta de un conjunto conformado por dos directorios en el que agrupan los ficheros necesarios para la ejecución de dos programas principales que emplean Dorks para realizar **hacking con buscadores**, así como llevar a cabo una recopilación de los resultados encontrados en la búsqueda, descarga de ficheros según su formato, entre otras funcionalidades, así como destacar que se basan en el buscador de Google y DuckDuckGo.

Se trata de un proyecto creado para aprender a usar Python orientado a la Ciberseguridad, en este caso al **hacking con buscadores**.
## Installation

Antes de llevar a cabo la instalación requerimos previamente que se encuentre instalado Python en el equipo:

[Download Python](https://www.python.org/downloads/)

Para la ejecución de los dos programas basta con descargar los ficheros correspondientes y haber instalado los paquetes necesarios referenciados en el archivo **requirements.txt** dentro de ambos ficheros.

A continuación, el comando de instalación de dichos paquetes:

**Google Dorks**
```bash
  pip install requests dotenv rich selenium gpt4all webdriver_manager
```

**DuckDuckGo Dorks**
```bash
  pip install requests dotenv rich selenium gpt4all webdriver_manager google-search-results serpapi
```


## API Reference

Para el correcto funcionamiento de los programas requerimos tener una API asociada que haga referencia al navegador que vayamos a utilizar, así como el ID del motor de búsqueda en el caso de que usemos Google.

#### Con Google

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `API_KEY_GOOGLE` | `string` | **Necesario**. API key de Google |
| `SEARCH_ENGINE_ID` | `string` | **Necesario**. ID del motor de búsqueda |

Para más información de como establecer la `API_KEY_GOOGLE` y `SEARCH_ENGINE_ID` se recomienda visitar los siguentes enlaces:

`API_KEY_GOOGLE` -> https://developers.google.com/apis-explorer?hl=es-419

`SEARCH_ENGINE_ID` -> https://developers.google.com/custom-search/v1/overview?hl=es-419


#### Con DuckDuckGo

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `API_KEY_DUCK`      | `string` | **Necesario**. API key de DuckDuckGo |


Para más información de como establecer la `API_KEY_DUCK` se recomienda visitar el siguente enlace:

`API_KEY_DUCK`  -> https://serpapi.com/duckduckgo-search-api



## Features (Google Dorks)

- **Configuración**: Inicia el proceso de configuración del archivo .env. Utiliza esta opcion sin otros argumentos para configurar las claves.
- **Consulta**: Indica la consulta que queremos realizar en el buscador.
- **Página de inicio**: Define la página de incio del buscador donde empezará a recibir resultados.
- **Número de Páginas**: Número de páginas en total que se desean consultar. Cada página consta de 10 resultados de búsqueda
- **Lenguaje de búsqueda**: Código de idioma de cara a los resultados de búsqueda. Por defecto es 'lang-es' (español).
- **Exportar resultados como html**: Exporta los resultados en formarto HTML indicando el nombre del archivo con la extensión ".html". Se almacena en la misma ruta que el programa principal.
- **Exportar resultados como json**: Exporta los resultados en formato JSON, indicando el nombre del archivo con la extensión ".json". Se almacena en la misma ruta que el programa principal.
- **Descargar ficheros**: Permite la descarga de ficheros, indicando previamente la extensión de los archivos que se desean descargar.
- **Generar un Dork personalizado mediante IA**: Genera un Dork a través de una descripción otorgada por el usuario. GPT4All será el encargado de generar dicha consulta.
- **Búsqueda automatizada con selenium**: Permite realizar una consulta con Selenium, imitando el comportamiento humano a la hora de realizar cualquier búsqueda.

Así mismo con la opción -h o --help podemos encontrar de manera resumida los parámetros para ejecutar cada una de las funciones descritas:

```bash
python google_dork.py -h            

usage: google_dork.py [-h] [-q QUERY] [-c] [--start-page START_PAGE] [--pages PAGES] [--lang LANG] [--html HTML]
                      [--json JSON] [--download DOWNLOAD] [-gd GENERATE_DORK] [--selenium]

Esta herramienta permite realizar Hacking con buscadores de forma automática. En este caso emplearemos principalmente
el buscador de Google Chrome/Bing.

options:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Indica la consulta que queremos realizar en el buscador. Por ejemplo: 'filetype:sql "MySQL
                        dump" (pass|password|passwd|pwd)'.
  -c, --configure       Inicia el proceso de configuración del archivo .env. Utiliza esta opcion sin otros argumentos
                        para configurar las claves.
  --start-page START_PAGE
                        Define la página de incio del buscador donde empezará a recibir resultados.
  --pages PAGES         Es el número de páginas en total que se desean consultar. Cada página consta de 10 resultados
                        de búsqueda.
  --lang LANG           Código de idioma de cara a los resultados de búsqueda. Por defecto es 'lang-es' (español)
  --html HTML           Exporta los resultados en formarto HTML indicando el nombre del archivo con su extensión
                        .html. Se almacena en la misma ruta que el programa principal.
  --json JSON           Exporta los resultados en formato JSON, indicando el nombre del archivo con su extensión
                        .json. Se almacena en la misma ruta que el programa principal.
  --download DOWNLOAD   Permite la descarga de ficheros, indicando previamente la extensión de los archivos que se
                        desean descargar. Ejemplo: --download 'pdf,sql,doc' Si deseas descargar todos los formatos de
                        archivos. Ejemplo: --download 'all'
  -gd GENERATE_DORK, --generate-dork GENERATE_DORK
                        Genera un Dork a través de una descripción otorgada por el usuario. GPT4All será el encargado
                        de generar dicha consulta.Por ejemplo: --generate-dork 'Listado de usuarios y passwds en un
                        fichero de texto.'
  --selenium            Permite realizar una consulta con Selenium, imitando el comportamiento humano a la hora de
                        realizar cualquier búsqueda.
```

## Features (DuckDuckGo Dorks)

- **Configuración**: Inicia el proceso de configuración del archivo .env. Utiliza esta opcion sin otros argumentos para configurar las claves.
- **Motor de búsqueda**: Indica el motor de búsqueda que se usará para realizar peticiones. Por ejemplo: 'duckduckgo' (parámetro obligatorio).
- **Consulta**: Indica la consulta que queremos realizar en el buscador.
- **Número de Páginas**: Número de páginas en total que se desean consultar. Cada página consta de 10 resultados de búsqueda.
- **Lenguaje de búsqueda**: Código de idioma de cara a los resultados de búsqueda. Por defecto es 'lang-es' (español).
- **Exportar resultados como html**: Exporta los resultados en formarto HTML indicando el nombre del archivo con la extensión ".html". Se almacena en la misma ruta que el programa principal.
- **Exportar resultados como json**: Exporta los resultados en formato JSON, indicando el nombre del archivo con la extensión ".json". Se almacena en la misma ruta que el programa principal.
- **Descargar ficheros**: Permite la descarga de ficheros, indicando previamente la extensión de los archivos que se desean descargar.
- **Generar un Dork personalizado mediante IA**: Genera un Dork a través de una descripción otorgada por el usuario. GPT4All será el encargado de generar dicha consulta.
- **Búsqueda automatizada con selenium**: Permite realizar una consulta con Selenium, imitando el comportamiento humano a la hora de realizar cualquier búsqueda.

Así mismo con la opción -h o --help podemos encontrar de manera resumida los parámetros para ejecutar cada una de las funciones descritas:

```bash
python duck_dork.py -h
                                   
usage: duck_dork.py [-h] [-c] [-e ENGINE] [-q QUERY] [--lang LANG] [--pages PAGES] [--html HTML] [--json JSON]
                    [--download DOWNLOAD] [-gd GENERATE_DORK] [--selenium]

Esto es una herramienta que permite realizar hacking con búscadores a través del servicio de DuckDuckGo.

options:
  -h, --help            show this help message and exit
  -c, --configure       Indica si existe el archivo de configuración .env para posteriormente cargarlo en el programa.
  -e ENGINE, --engine ENGINE
                        Indica el motor de búsqueda que se usará para realizar peticiones. Por ejemplo: 'duckduckgo'.
  -q QUERY, --query QUERY
                        Indica la consulta que queremos realizar en el buscador. Por ejemplo: 'filetype:sql "MySQL
                        dump" (pass|password|passwd|pwd)'.
  --lang LANG           Código de idioma de cara a los resultados de búsqueda. Por defecto: 'es-es'.
  --pages PAGES         Es el número de páginas en total que se desean consultar. Cada página consta de 10 resultados
                        de búsqueda.
  --html HTML           Exporta los resultados en formarto HTML indicando el nombre del archivo con su extensión
                        .html. Se almacena en la misma ruta que el programa principal.
  --json JSON           Exporta los resultados en formato JSON, indicando el nombre del archivo con su extensión
                        .json. Se almacena en la misma ruta que el programa principal.
  --download DOWNLOAD   Permite la descarga de ficheros, indicando previamente la extensión de los archivos que se
                        desean descargar. Ejemplo: --download 'pdf,sql,doc' Si deseas descargar todos los formatos de
                        archivos. Ejemplo: --download 'all'
  -gd GENERATE_DORK, --generate-dork GENERATE_DORK
                        Genera un Dork a través de una descripción otorgada por el usuario. GPT4All será el encargado
                        de generar dicha consulta.Por ejemplo: --generate-dork 'Listado de usuarios y passwds en un
                        fichero de texto.'
  --selenium            Permite realizar una consulta con Selenium, imitando el comportamiento humano a la hora de
                        realizar cualquier búsqueda.
```

# Usage/Examples

Recopilar los 10 primeros resultados web de una búsqueda y los muestre por pantalla:

**Con Google**
```bash
  python google_dork.py -q "website"
```

**Con DuckDuckGo**
```bash
  python duck_dork.py -e "duckduckgo" -q "website"
```

Realizar una búsqueda y almacenar todos los ficheros 'pdf' que se encuentren:

**Con Google**
```bash
  python google_dork.py -q "consulta" --download 'pdf'
```

**Con DuckDuckGo**
```bash
  python duck_dork.py -e "duckduckgo" -q "consulta" --download 'pdf'
```
## Tech Stack

Todos los archivos necesarios para el correcto funcionamiento de ambos programas presentados se encuentran desarrollados en **Python**.
