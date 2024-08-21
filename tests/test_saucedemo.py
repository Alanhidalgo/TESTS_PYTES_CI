import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver


@pytest.mark.usefixtures("setup")
class TestSaucedemo:
    driver: WebDriver

    def test_validate_title_page(self):
        self.driver.get("https://www.saucedemo.com/")
        assert self.driver.title == "Swag Labs", "El título de la página no es el esperado"