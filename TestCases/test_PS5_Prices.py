import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from Locators.locators_Mercado_Libre import Locators_Mercado_Libre

class Test_PS5_Prices():

    def __init__(self):
        self.Driver_path = Locators_Mercado_Libre.Driver_path
        self.Download_path = Locators_Mercado_Libre.Download_path
        self.file_name = Locators_Mercado_Libre.file_name
        self.General_File_path = Locators_Mercado_Libre.General_File_path
        self.URL = Locators_Mercado_Libre.URL
        self.id_MX = Locators_Mercado_Libre.id_MX
        self.xpath_Button_Cookies = Locators_Mercado_Libre.xpath_Button_Cookies
        self.id_Search_Box = Locators_Mercado_Libre.id_Search_Box
        self.xpath_mainframe = Locators_Mercado_Libre.xpath_mainframe
        self.xpath_Button_Mas_Tarde = Locators_Mercado_Libre.xpath_Button_Mas_Tarde
        self.xpath_Nuevo = Locators_Mercado_Libre.xpath_Nuevo
        self.xpath_Button_Order_By = Locators_Mercado_Libre.xpath_Button_Order_By
        self.xpath_Button_Order_Higher_Price = Locators_Mercado_Libre.xpath_Button_Order_Higher_Price
        self.get_Product_Name = Locators_Mercado_Libre.get_Product_Name
        self.get_Product_Price = Locators_Mercado_Libre.get_Product_Price
        self.str_Email = Locators_Mercado_Libre.str_Email
        self.str_Password = Locators_Mercado_Libre.str_Password

    def write_file(self, message):
        # 'a' for Append/Agregar
        with open(self.General_File_path, 'a') as fichero:
            fichero.write(message) 

    def test_Obtain_Prices(self):
        # Specify Services as Driver Path
        service = Service(executable_path = self.Driver_path , log_path=os.devnull)
        # Specify Chrome Options
        options = webdriver.ChromeOptions()
        # For Chrome we ignore any Secure Certificate
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--silent")
        options.add_argument("--log-level=1")  # 0: INFO, 1: WARNING, 2: ERROR, 3: FATAL
        options.add_argument("--disable-logging")  # Desactivar logging
        #options.add_argument('--headless')
        # Specify the Path of any Download
        options.add_experimental_option('prefs', {'download.default_directory' : self.Download_path} )
        driver = webdriver.Chrome(service = service, options = options)
        driver.maximize_window()
        driver.get(self.URL)

        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.id_MX))
            )
        except TimeoutException as toe:
            print("Timeout Error on Selecting Mexico: ", toe)

        # Click on Mexico
        driver.find_element(By.ID, self.id_MX).click()

        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.id_Search_Box))
            )
        except TimeoutException as toe:
            print("Timeout Error on Search Box: ", toe)

        # Popup 'Codigo Postal'.
        try:
            popup_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.xpath_Button_Mas_Tarde))
            )
            popup_button.click()
        except Exception as e:
            print("\nError on Button 'Mas Tarde': " , e)

        # Click on Cookies
        try:
            button_Nuevo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.xpath_Button_Cookies))
            )
            actions = ActionChains(driver)
            actions.move_to_element(button_Nuevo).click().perform()
        except Exception as e:
            print("\nError on Button 'Aceptar Cookies': ", e )

        # Search 'PlayStation 5
        driver.find_element(By.ID, self.id_Search_Box).click()
        driver.find_element(By.ID, self.id_Search_Box).send_keys("playstation 5")
        driver.find_element(By.ID, self.id_Search_Box).send_keys(Keys.ENTER)

        # Click on 'Nuevo'
        try:
            button_Nuevo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.xpath_Nuevo))
            )
            actions = ActionChains(driver)
            actions.move_to_element(button_Nuevo).click().perform()
            time.sleep(10)
        except Exception as e:
            print("\nError on Click 'Nuevo': ", e)

        # Order by Price
        try:
            button_Order_By = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_Button_Order_By))
            )
            button_Order_By.click()
        except Exception as e:
            print("Error: ", e)

        # Choose Higher Price
        try:
            button_Order_Higher_Price = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_Button_Order_Higher_Price))
            )
            button_Order_Higher_Price.click()
            
        except Exception as e:
            print("Error: ", e)

        time.sleep(5)

        try:
            for i in range(1,6):
                # Product
                name_xpath = self.get_Product_Name( i)

                # Price
                price_xpath = self.get_Product_Price(driver, i)

                # Obtain the Text
                product_name = driver.find_element(By.XPATH, name_xpath).text
                product_price = driver.find_element(By.XPATH, price_xpath).text
                
                print(f"\nNombre: {product_name}, Precio: {product_price}\n")

                # Write the Product and the Price in a File
                self.write_file(f"\nNombre: {product_name}")
                self.write_file(f"\nPrecio: {product_price}\n")

        except Exception as e:
            print(f"Error on Product {i}: {e}")

        driver.close()
        driver.quit()