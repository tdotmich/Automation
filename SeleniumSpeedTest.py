import os
from selenium import webdriver
from selenium.webdriver.common.by import By  # Required to identify elements
from selenium.webdriver import Keys  # Send keystrokes to browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

os.environ['PATH'] += r"C:\Users\thoma\Downloads\seleniumdrivers\chromedriver.exe"
driver = webdriver.Chrome(r'C:\Users\thoma\Downloads\seleniumdrivers\chromedriver.exe')

# Open chrome and head to google homepage
driver.get("https://www.google.com")

# Wait for cookie policy popup
driver.implicitly_wait(10)

# Click accept on cookie policy
accept = driver.find_element(By.ID, "L2AGLb")
accept.click()

# Find and click search bar
search = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")
search.click()

# Search for Googles speed test
search.send_keys("google speed test")
search.send_keys(Keys.RETURN)

# Use text() function to click "Run Speed Test" button
runTest = driver.find_element(By.CLASS_NAME, "fSXkBc")
runTest.click()

# Wait for result of test
wait = WebDriverWait(driver, 30)
resultWait = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "fSXkBc")))

# Grab result from webpage, unfortunately still work in progress as this class value starts empty on page load
result = driver.find_element(By.CSS_SELECTOR, 'p.spiqle').get_attribute('innerHTML')


print(result)



print("Test")
