# Packages

from selenium import webdriver # Hace referencia al conjunto de drivers necesarios para la ejecución del navegador
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

# Class

class BrowserAutoSearch:
    """
    Esta clase permite utilizar la librería Selenium para realizar búsquedas automáticas imitando el comportamiento humano.
    """
    def __init__(self):
        """
        Función constructora. Inicializa los atributos de instancia.
        """

        self.browser = self._initialize_browser()

    def _initialize_browser(self):
        """
        Permite inicializar los buscadores en función de los que instalados en el S.O, ya sea Firefox o Google Chrome.
        """
        
        browsers = {
            "firefox" : {
                "service" : FirefoxService(GeckoDriverManager().install()),
                "options" : webdriver.FirefoxOptions(),
                "driver" : webdriver.Firefox
            },
            "chrome" : {
                "service" : ChromeService(ChromeDriverManager().install()),
                "options" : webdriver.ChromeOptions(),
                "driver" : webdriver.Chrome
            }
        }

        # Incializamos los navegadores
        for browser_name,browser_info in browsers.items():
            try:
                return browser_info["driver"](service=browser_info["service"],options=browser_info["options"])
            except Exception as e:
                print(f"Error al intentar inicializar el navegador {browser_name}: {e}")
        
        raise Exception("No se pudo inicial ningún navegador, ¿tiene instalador Firefox o Chrome?")

    def search_duck(self,query):
        """
        Realiza una búsqueda en Microsoft Bing.

        Args:
            query(str): Se trata de la consulta que desea realizar el usuario.
        """
        
        # Abre Google
        self.browser.get("https://www.duckduckgo.com")

        # Esperamos unos segundos hasta que aparezca la opción de aceptar cookies.
        time.sleep(5)

        # Encuentra el cuadro de búsqueda y envia la cadena de texto
        
        search_box = self.browser.find_element(By.ID, "searchbox_input")
        search_box.send_keys(query + Keys.ENTER)

        # Esperamos a que la página cargue los resultados
        time.sleep(5)

    def duck_search_results(self):
        """
        Extrae los resultados de la consulta.
        """
        
        # Extraemos los enlaces y descripciones de los primeros resultados
        results = self.browser.find_elements(By.CLASS_NAME, "wLL07_0Xnd1QZpzpfR4W")
        custom_results = []
        for resultado in results:
            try:
                cresult = {}
                cresult["title"] = resultado.find_element(By.CLASS_NAME, "pAgARfGNTRe_uaK72TAD").text
                cresult["link"] = resultado.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                
                cresult["description"] = resultado.find_element(By.CLASS_NAME, "E2eLOJr8HctVnDOTM8fs").text

                custom_results.append(cresult)
            except Exception as e:
                print(f"Se ha producido una excepción a la hora de recolectar los resultados: {e}")
                continue
        return custom_results
    
    def quit(self):
        """
        Se cierra el navegador tras realizar la consulta y extraer los datos.
        """

        self.browser.quit()