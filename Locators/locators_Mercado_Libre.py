from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Locators_Mercado_Libre():
    Driver_path = "C:\\Automation\\Mercado_Libre\\Drivers\\chromedriver.exe"

    Download_path = "C:\\Automation\\Mercado_Libre\\Downloads"

    file_name = f"Test_Playstation5_{date.today()}.txt"

    General_File_path = f"C:\\Automation\\Mercado_Libre\\Evidence\\{file_name}"

    URL = "https://www.mercadolibre.com"

    id_MX = "MX"

    id_Search_Box = "cb1-edit"

    xpath_mainframe = "/html/body/main/div/div[2]"

    xpath_Button_Cookies = "//button[contains(text(), 'Aceptar') or contains(text(), 'Accept') or contains(text(), 'OK')]"

    xpath_Button_Mas_Tarde = "/html/body/div[5]/div/div/div[2]/div/div/div[2]/button[2]"

    xpath_Nuevo = '//a[span[contains(@class, "ui-search-filter-name") and contains(text(), "Nuevo")]]'

    xpath_Button_Order_By = '/html/body/main/div/div[2]/section/div[2]/div/div/div/div[2]/div/div/button'

    xpath_Button_Order_Higher_Price = '/html/body/main/div/div[2]/section/div[2]/div/div/div/div[2]/div/div/div/div/div/ul/li[3]'

    @staticmethod
    def get_Product_Name(i): 
        return f"/html/body/main/div/div[2]/section/div[5]/ol/li[{i}]/div/div/div/div[2]/h3/a"

    @staticmethod
    def get_Product_Price(driver, i):
        # Posible XPaths
        possible_xpaths = [
            f"/html/body/main/div/div[2]/section/div[5]/ol/li[{i}]/div/div/div/div[2]/div/div[1]/div/div/span/span[2]",
            f"/html/body/main/div/div[2]/section/div[5]/ol/li[{i}]/div/div/div/div[2]/div[1]/div/span/span[2]"
        ]
        
        for xpath in possible_xpaths:
            try:
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                return xpath  # Return the correct XPATH
            except Exception:
                continue  # try to the next XPATH
    
    str_Email = "pruebasl735@gmail.com"

    str_Password = "ntgd rzno bgea zquo"

    list_To_Email =  ['cabreraemi@globalhitss.com', 's_fuentesrj@globalhitss.com', 'ruizro@hitss.com']