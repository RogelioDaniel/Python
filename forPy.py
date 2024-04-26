import time
import openai
# import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# create webdriver object
driver = webdriver.Chrome()
x_coordinate = 900 # coordenadas para BANCA
y_coordinate = 300

 
# get geeksforgeeks.org
driver.get("https://workontime.net/Time/")
 
# get element
time.sleep(3)
element = driver.find_element(By.NAME, "user")
element.send_keys("") # reemplazar con tu correo
element = driver.find_element(By.NAME, "password")
element.send_keys("") # reemplazar con tu password
time.sleep(1)
element = driver.find_element(By.CLASS_NAME, "loginButton")
element.click()
time.sleep(1)
actions = ActionChains(driver)
actions.move_by_offset(x_coordinate, y_coordinate)
time.sleep(3)
actions.click()
actions.click()
time.sleep(3)

time.sleep(1)
actions.perform()
element = driver.find_element(By.XPATH, "/html/body/span[11]/div/timesheet/div/time-list/div/table/tbody/tr[3]/td/task-row/div/div/div[2]/table/tbody/tr[1]/td[2]/input")
element.send_keys(8)
element = driver.find_element(By.XPATH, "/html/body/span[11]/div/timesheet/div/time-list/div/table/tbody/tr[3]/td/task-row/div/div/div[3]/div/textarea")
# Configura tu clave de API de OpenAI

openai.api_key = ''

def resumenGPT(texto_a_resumir = "Quiero que me hagas un texto mas profesional de lo siguiente: Hoy segui con mi path de python, vi orientada a objetos y creacion de app con chromedriver"
):
    # Define el texto que quieres resumir

    # Define el modelo de GPT-3 que quieres utilizar (p. ej., 'text-davinci-002')
    modelo = 'gpt-3.5-turbo-instruct'

    # Define la solicitud a la API de GPT-3
    solicitud = {
        "prompt": texto_a_resumir,
        "max_tokens": 200,
        "temperature": 0.7,
        "engine": modelo
    }

    # Envía la solicitud a la API de GPT-3 para generar el resumen
    respuesta = openai.Completion.create(**solicitud)
    return respuesta.choices[0].text.strip()

# Imprime el resumen generado por GPT-3
print("Resumen generado por GPT-3:")
print(resumenGPT())
texto_a_escribir = "Texto que quiero escribir"
element.send_keys(resumenGPT())
element = driver.find_element(By.XPATH, "/html/body/span[11]/div/timesheet/div/div/div/div/span[1]")
element.click()

time.sleep(10)  # Espera 5 segundos antes de cerrar la página


# send keys
