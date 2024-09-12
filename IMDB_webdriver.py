from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open IMDb search page
url = "https://www.imdb.com/search/name/"
driver.get(url)

try:
    # Wait for the search form to be visible and interactable
    search_form = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "search-main")))

    # Find input boxes and fill them
    driver.find_element(By.ID, "name").send_keys("Tom Hanks")
    #name_input

    driver.find_element(By.ID, "birth_date-min").send_keys("01/01/1950")
    #birth_date_min_input

    driver.find_element(By.ID, "birth_date-max").send_keys("12/31/1970")
    #birth_date_max_input

    # Find select boxes and select options
    gender_select = driver.find_element(By.ID, "gender")
    gender_options = gender_select.find_elements(By.TAG_NAME, "option")
    for option in gender_options:
        if option.text == "Male":
            option.click()
            break

    # Find dropdown menu and select an option
    known_for_dropdown = driver.find_element(By.ID, "known_for")
    action_chains = ActionChains(driver)
    action_chains.move_to_element(known_for_dropdown).click().perform()
    option_to_select = known_for_dropdown.find_element(By.XPATH, "//option[text()='Acting']")
    option_to_select.click()

    # Perform the search
    search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
    search_button.click()

    # Wait for search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lister-list"))
    )

    # Print the current URL after search
    print("Current URL after search:", driver.current_url)

finally:
    # Close the browser
    driver.quit()