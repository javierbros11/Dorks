# Packages

import json
from rich.console import Console
from rich.table import Table

# Class

class Results_parser_duck:
    """
    Es una clase que permite exportar los resultados de una búsqueda en formato JSON o HTML.
    En caso contrario, muestra los resultados en línea de comandos de forma personalizada.
    """

    def __init__(self,results,pages):
        """
        Inicializa los atributos de instancia.

        Args:
            results(dict): Contiene todos los resultados de la búsqueda realizada.
            pages(int): Indica la cantidad de páginas que quiere que se muestre.
        """

        self.results = results
        self.pages = pages
    
    def export_html(self,ruta_salida):
        """
        Permite exportar los resultados en formato HTML.

        Args:
            ruta_salida(str): Ruta donde se almacena el archivo HTML.
        """
        with open("html_template_duckduckgo_dorks.html","r", encoding="utf-8") as template:
            plantilla = template.read()

        elementos_html= ""
        for indice,resultado in enumerate(self.results["organic_results"], start=1):
            if indice in range(self.pages + 1):
                elemento = f"<div class='resultado'>" \
                f"<div class='indice'> Resultado {indice}</div>" \
                f"<h5>{resultado['title']}</h5>" \
                f"<p>{resultado['snippet']}</p>" \
                f"<a href='{resultado['link']}' target='_blank'>{resultado['link']}</a>" \
                f"</div>"
                elementos_html+=elemento

        inform_html = plantilla.replace("{{ resultados }}", elementos_html)
        
        with open(ruta_salida,"w",encoding="utf-8") as f:
            f.write(inform_html)
        print(f"Se ha exportado con éxito el archivo HTML. Se encuentra en la ruta: {ruta_salida}")
    
    def export_json(self,ruta_salida):
        """
        Permite exportar los resultados en formato JSON

        Args:
            ruta_salida(str): Ruta donde se almacena el archivo JSON.
        """
        inform_json=[]
        for i in self.results["organic_results"]:
            if i["position"] in range(self.pages+1):
                inform_json.append(i)
        with open(ruta_salida, "w",encoding="utf-8") as f:
            json.dump(inform_json, f, ensure_ascii=False, indent=4)
        print(f"Se ha exportado con éxito el archivo JSON. Se encuentra en la ruta: {ruta_salida}")

    def mostrar_pantalla(self):
        """
            Muestra por linea de comandos los resultados obtenidos tras realizar la consultas.
        """

        console = Console()
        table = Table(show_header=True,header_style="bold green")
        table.add_column("#", style="dim")
        table.add_column("Titulo", width=50)
        table.add_column("Descripcion")
        table.add_column("Enlace")

        for indice,resultado in enumerate(self.results["organic_results"],start=1):
            if indice in range(self.pages+1):
                table.add_row(str(indice), resultado["title"],resultado["snippet"],resultado["link"])
                table.add_row("","","","")

        console.print(table)
    
    def mostrar_pantalla_auto(self):
        """
            Muestra por linea de comandos los resultados obtenidos tras realizar la consultas con selenium.
        """

        console = Console()
        table = Table(show_header=True,header_style="bold green")
        table.add_column("#", style="dim")
        table.add_column("Titulo", width=50)
        table.add_column("Descripcion")
        table.add_column("Enlace")

        for indice,resultado in enumerate(self.results,start=1):
            if indice in range(self.pages+1):
                table.add_row(str(indice), resultado["title"],resultado["description"],resultado["link"])
                table.add_row("","","","")

        console.print(table)