# paginas/pagina_produto.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginaProduto:
    def __init__(self, driver):
        self.driver = driver
        self.preco_locator = (By.XPATH, '//*[@id="__next"]/main/div[1]/div/section[1]/section[2]/div[1]/section/h1')

    def obter_preco_produto(self):
        elemento_preco = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.preco_locator)
        )
        return elemento_preco.text
