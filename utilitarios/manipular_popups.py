# utilitarios/manipulador_popups.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ManipuladorPopups:
    @staticmethod
    def fechar_popups(driver):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='wrap-text-1454703513202']"))
            )
            print("Pop-up removido com sucesso.")
        except:
            print("Pop-up não encontrado ou já removido.")
