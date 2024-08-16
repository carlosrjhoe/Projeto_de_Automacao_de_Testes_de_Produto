# drivers/driver_edge.py
from selenium.webdriver import EdgeOptions, Edge

def iniciar_driver_edge():
    opcoes = EdgeOptions()
    opcoes.add_argument("--disable-popup-blocking")
    opcoes.add_argument("--disable-notifications")
    opcoes.add_argument("--disable-extensions")
    opcoes.add_argument("--start-maximized")
    
    return Edge(options=opcoes)
