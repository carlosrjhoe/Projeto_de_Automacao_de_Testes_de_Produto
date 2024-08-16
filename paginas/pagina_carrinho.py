# paginas/pagina_carrinho.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginaCarrinho:
    def __init__(self, driver):
        self.driver = driver
        self.quantidade_itens = (By.XPATH, '//h2[@data-cy="quantity-items-cart"]')
        self.preco_carrinho = (By.XPATH, '//*[@id="__next"]/main/div/main/section[1]/section/section[2]/section[1]/section[2]/h3')

    def obter_quantidade_itens(self):
        elemento_quantidade = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.quantidade_itens)
        )
        return elemento_quantidade.text

    def obter_preco_carrinho(self):
        elemento_preco = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.preco_carrinho)
        )
        return elemento_preco.text
