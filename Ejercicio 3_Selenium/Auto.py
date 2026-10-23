import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def configurar_driver():
    """Configura Microsoft Edge desactivando alertas de contraseñas que puedan estorbar."""
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--inprivate")
    return webdriver.Edge(options=options)


def test_flujo_completo_compra_e2e():
    """
    TC-001: Flujo End-to-End (Login -> Agregar al Carrito -> Registro Checkout -> Confirmación)
    """
    print("\n--- Iniciando TC-001: Flujo Completo E2E (standard_user) ---")
    driver = configurar_driver()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Navegar al sitio
        driver.get("https://www.saucedemo.com/")

        # 2. Login
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Validar ingreso
        titulo_catalogo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert titulo_catalogo.text == "Products", "No se cargó la página de productos."
        print("[OK] Login exitoso. Catálogo de productos visible.")

        # 3. Agregar productos al carrito
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Validar que el ícono del carrito muestre '2'
        badge_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert badge_carrito.text == "2", f"Se esperaban 2 artículos, pero hay {badge_carrito.text}"
        print("[OK] 2 productos agregados al carrito correctamente.")

        # 4. Ir al carrito y proceder al pago
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # 5. Llenar el formulario
        print("[INFO] Llenando formulario de registro de compra (Checkout)...")
        wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Omar")
        driver.find_element(By.ID, "last-name").send_keys("Marta")
        driver.find_element(By.ID, "postal-code").send_keys("06000")
        driver.find_element(By.ID, "continue").click()

        # 6. Verificar resumen de compra y finalizar
        titulo_resumen = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert titulo_resumen.text == "Checkout: Overview", "No se mostró el resumen de la compra."
        
        driver.find_element(By.ID, "finish").click()

        # 7. Validar confirmación final n
        mensaje_exito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        assert mensaje_exito.text == "Thank you for your order!", "El mensaje de confirmación no coincide."
        print(f"[EXITO] Orden completada con mensaje: '{mensaje_exito.text}'")

        time.sleep(3)

    except Exception:
        print(f"\n[ERROR] Falló TC-001 en la URL: {driver.current_url}")
        traceback.print_exc()
        driver.save_screenshot("error_tc001.png")
    finally:
        driver.quit()


def test_login_usuario_bloqueado():
    """
    TC-002: Validar restricción de acceso con usuario bloqueado (locked_out_user)
    """
    print("\n--- Iniciando TC-002: Validación de Usuario Bloqueado (locked_out_user) ---")
    driver = configurar_driver()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Validar mensaje de error esperado
        mensaje_error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
        texto_esperado = "Epic sadface: Sorry, this user has been locked out."
        assert texto_esperado in mensaje_error.text, f"Mensaje inesperado: {mensaje_error.text}"
        print(f"[EXITO] Bloqueo validado correctamente: '{mensaje_error.text}'")

        time.sleep(2)

    except Exception:
        print(f"\n[ERROR] Falló TC-002 en la URL: {driver.current_url}")
        traceback.print_exc()
        driver.save_screenshot("error_tc002.png")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_flujo_completo_compra_e2e()
    test_login_usuario_bloqueado()