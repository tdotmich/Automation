from selenium import webdriver
# This is a relatively simple response time tester that uses Selenium to retrieve both front and back end response times
# Chrome web driver interface

PATH = r"Your chromedriver.exe location"
hyperlink = "Whatever site you want to test the response times of"
driver = webdriver.Chrome(PATH)
driver.get(hyperlink)

# Use Navigation Timing  API to calculate the timings that matter the most

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

# Calculate the performance
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

print("Back End: %s" % backendPerformance_calc + "ms")
print("Front End: %s" % frontendPerformance_calc + "ms")

driver.quit()