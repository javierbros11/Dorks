#Packages

from gpt4all import GPT4All

#Class

class IAagent:
    """
    Consta del uso de una IA (GPT4All) para crear un Dork en función de las preferencias del usuario.
    """

    def __init__(self,model_name = "orca-mini-3b-gguf2-q4_0.gguf"):
        """
        Inicializamos los atributos de instancia.

        Args:
            model(str): Conforma el modelo de la IA a utilizar.
        """

        self.model_name = GPT4All(model_name)
    
    def generate_dork(self,description):
        """
        Permite la generación de un Dork en función de una descripción proporcionada.

        Args:
            description(str): Descripción introducida por el usuario.
        """

        # Construimos el prompt
        prompt = self._build_prompt(description)
        try:
            respuesta = self.model_name.generate(prompt)
            return respuesta
        except Exception as exception:
            print(f"Se ha producido una excepción: {exception}")

    def _build_prompt(self,description):
        """
        Crea el prompt que será proporciado para general el Dork.

        Args:
            description(str): Descripción introducida por el usuario.
        """

        return f"""

        Genera un Dork específico para el buscador DuckDuckGo basado en la descripción del usuario. Un Dork utiliza operadores avanzados en motores de búsqueda para encontrar información específica que es difícil de encontrar mediante una búsqueda normal. Tu tarea es convertir la descripción del usuario en un Dork preciso. A continuación, se presentan algunos ejemplos de cómo deberías formular los Google Dorks basándote en diferentes descripciones:

        Descripción: Documentos que contengan contraseñas y entornos en la página de GitHub.
        DuckDuckGo Dork: site:github.com "password" "env"

        Descripción: Presentaciones de Powerpoint sobre cambio climático disponibles en sitios .edu.
        DuckDuckGo Dork: site:.edu "cambio climático" filetype:ppt

        Descripción: Listas de correos electrónicos en archivos de texto dentro de dominios gubernamentales.
        DuckDuckGo Dork: site:.gov filetype:txt "email" | "correo electrónico"

        Ahora, basado en la siguiente descripción proporcionada por el usuario, genera el DuckDuckGo Dork correspondiente:

        Descripción: {description}
        """
    