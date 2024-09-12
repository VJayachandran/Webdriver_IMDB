from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# For Explicit wait only
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Jaya:

   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   wait = WebDriverWait(driver, 10)

   def __init__(self, web_url):
       self.url = web_url

   def fill_data(self):
       try:
           self.driver.get(self.url)
           Name = self.wait.until(EC.presence_of_element_located((By.NAME, "Name")))
           DOB_Min = self.wait.until(EC.presence_of_element_located((By.NAME, "birth_date-min")))
           DOB_Max = self.wait.until(EC.presence_of_element_located((By.NAME, "birth_date-max")))
           submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
           Name.send_keys("Tom Hanks")
           DOB_Min.send_keys("01/01/1950")
           DOB_Max.send_keys("12/31/1970")
          # submit_button.click()



       except NoSuchElementException as e:
           print(e)
       finally:
           self.driver.quit()

url = "https://www.imdb.com/search/name/"
jaya = Jaya(url)
jaya.fill_data()
