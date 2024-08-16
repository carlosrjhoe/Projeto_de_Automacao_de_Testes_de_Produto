from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaginaInicial:
    def __init__(self, driver):
        self.driver = driver
        self.campo_busca = (By.ID, "searchProduct")
        self.botao_busca = (By.CSS_SELECTOR, ".styles__BaseHyperLink-sc-1f5c1fd3-0 > svg")
        self.link_produto = (By.XPATH, "//div[@data-cy='card-container-0']")
        self.botao_adicionar_carrinho = (By.XPATH, "(//span[@data-cy='text-button-cart' and text()='Adicionar ao carrinho'])[2]")

    def inserir_consulta_busca(self, consulta):
        elemento_busca = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.campo_busca)
        )
        elemento_busca.click()
        elemento_busca.send_keys(consulta)

    def clicar_botao_busca(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.botao_busca)
        ).click()

    def selecionar_produto(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.link_produto)
        ).click()

    def adicionar_ao_carrinho(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.botao_adicionar_carrinho))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("window.scrollBy(0, -200);")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.botao_adicionar_carrinho)
        ).click()
