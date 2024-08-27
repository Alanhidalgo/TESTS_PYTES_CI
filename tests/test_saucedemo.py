import pytest
from selenium.webdriver.chrome.webdriver import WebDriver  # Importar el tipo específico del driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestSaucedemo:
    driver: WebDriver

    def test_validate_title_page(self):
        self.driver.get("https://www.saucedemo.com/")
        assert self.driver.title == "Swag Labs", "El título de la página no es el esperado"

        #time.sleep(5)

    def test_login_page(self, credentials, clear_fields):
        self.driver.get("https://www.saucedemo.com/")
        # Obtener las credenciales del primer usuario en el archivo JSON
        username = credentials["users"][0]["username"]
        password = credentials["users"][0]["password"]

        fields = {
            "username": self.driver.find_element(By.ID, "user-name"),
            "password": self.driver.find_element(By.ID, "password"), 
        }

        # Limpiar los campos de texto
        clear_fields(fields.values())
        
        # Ingresar los datos
        fields["username"].send_keys(username)
        fields["password"].send_keys(password)
        # Esto es solo para validación
        #time.sleep(5)
        
        # Encontrar el botón de inicio de sesión y verificar que está habilitado
        login_button = self.driver.find_element(By.ID, "login-button")
        assert login_button.is_enabled(), "El boton de inicio de sesion no esta habilitado"

        # Hacer clic en el botón de inicio de sesión
        login_button.click()

        # Usar self.wait para esperar la visibilidad de un elemento
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert "Swag Labs" in self.driver.title, "El título de la página después de iniciar sesión no es el esperado"