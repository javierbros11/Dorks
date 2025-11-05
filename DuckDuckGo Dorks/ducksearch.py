from serpapi import GoogleSearch

class DuckDuckSearch:
    """
    Clase creada con el objetivo de llevar a cabo una búsqueda a través del navegador web DuckDuckGo.
    """

    def __init__(self,params):
        """
        Inicializa los atributos de instancia.

        Args:
            params(dict): Contiene los parámentros necesarios para poder realizar una búsqueda
        """

        self.params = params
    
    def search(self):
        """
        Realiza la búsqueda personalizada.
        """

        return GoogleSearch(self.params)