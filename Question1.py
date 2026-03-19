from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

# Open Facebook
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)

# Enter email using CSS selector
driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("example@gmail.com")

# Enter password using CSS selector
driver.find_element(By.CSS_SELECTOR, 'input[name="pass"]').send_keys("password")

sleep(1)

# Click login button using CSS selector
# driver.find_element(By.CSS_SELECTOR, 'span[name="Log in"]').click()
driver.find_element(By.CSS_SELECTOR, 'div[role="button"]').click()
sleep(5)

driver.quit()
