from selenium.webdriver.support import expected_conditions as EC
from driver.driver_edge import iniciar_driver_edge
from paginas.pagina_inicial import PaginaInicial
from paginas.pagina_produto import PaginaProduto
from paginas.pagina_carrinho import PaginaCarrinho
from utilitarios.manipular_popups import ManipuladorPopups

class TesteProduto:
    def setup_method(self):
        self.driver = iniciar_driver_edge()
        self.driver.get("https://www.ferreiracosta.com/")
        # self.driver.maximize_window()
        self.driver.set_window_size(1600, 1080)
        self.pagina_inicial = PaginaInicial(self.driver)
        self.pagina_produto = PaginaProduto(self.driver)
        self.pagina_carrinho = PaginaCarrinho(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_preco_produto(self):
        ManipuladorPopups.fechar_popups(self.driver)
        self.pagina_inicial.inserir_consulta_busca("parafusadeira")
        self.pagina_inicial.clicar_botao_busca()
        self.pagina_inicial.selecionar_produto()
        preco = self.pagina_produto.obter_preco_produto()
        assert preco == 'R$ 229,90'

    def test_quantidade_item_carrinho(self):
        ManipuladorPopups.fechar_popups(self.driver)
        self.pagina_inicial.inserir_consulta_busca("parafusadeira")
        self.pagina_inicial.clicar_botao_busca()
        self.pagina_inicial.selecionar_produto()
        self.pagina_inicial.adicionar_ao_carrinho()
        
        quantidade_itens = self.pagina_carrinho.obter_quantidade_itens()
        assert quantidade_itens == '1 item'

    def test_preco_carrinho(self):
        ManipuladorPopups.fechar_popups(self.driver)
        self.pagina_inicial.inserir_consulta_busca("parafusadeira")
        self.pagina_inicial.clicar_botao_busca()
        self.pagina_inicial.selecionar_produto()
        self.pagina_inicial.adicionar_ao_carrinho()
        
        preco_carrinho = self.pagina_carrinho.obter_preco_carrinho()
        assert preco_carrinho == 'R$ 229,90'
    