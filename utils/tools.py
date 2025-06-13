from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


class Tools:
    def __init__(self, driver):
        self.driver = driver
    
    def double_click(self, element=None, locator=None, timeout=10):
        """
        Realiza um duplo clique em um elemento web.
        
        Args:
            element: Elemento web já localizado (opcional)
            locator: Tupla contendo (By.TIPO, 'valor') para localizar o elemento (opcional)
            timeout: Tempo máximo de espera em segundos
            
        Returns:
            bool: True se o duplo clique foi realizado com sucesso, False caso contrário
            
        Raises:
            ValueError: Se nem element nem locator forem fornecidos
        """
        if element is None and locator is None:
            raise ValueError("É necessário fornecer um elemento ou um locator")
        
        try:
            # Se um locator foi fornecido, encontre o elemento
            if element is None and locator is not None:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
            
            # Garante que o elemento está visível e clicável
            self.wait.until(EC.visibility_of(element))
            self.wait.until(EC.element_to_be_clickable(element))
            
            # Executa o duplo clique
            self.actions.double_click(element).perform()
            return True
            
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Erro ao realizar duplo clique: {str(e)}")
            return False
