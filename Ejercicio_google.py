from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el controlador de Chrome.
# Asegúrate de que la ruta al 'chromedriver' sea correcta.
driver = webdriver.Chrome('/path/to/chromedriver')

# Abrir WhatsApp Web.
driver.get('https://web.whatsapp.com/')

# Esperar a que el usuario escanee el código QR.
input('Escanea el código QR y presiona Enter para continuar...')

# Buscar el campo de búsqueda y escribir el nombre del contacto.
# La elección del XPath puede variar con el tiempo debido a las actualizaciones de WhatsApp Web.
# Si el script falla, verifica que el XPath sigue siendo válido.
search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys('Nombre del contacto')
search_box.send_keys(Keys.ENTER)

# Esperar a que se cargue la conversación.
time.sleep(5)

# Buscar el campo de texto y escribir el mensaje.
# La elección del XPath puede variar con el tiempo debido a las actualizaciones de WhatsApp Web.
# Si el script falla, verifica que el XPath sigue siendo válido.
text_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
text_box.send_keys('Mensaje')
text_box.send_keys(Keys.ENTER)

# Esperar un momento para asegurar que el mensaje se haya enviado antes de cerrar.
time.sleep(3)

# Cerrar el navegador.
driver.quit()
