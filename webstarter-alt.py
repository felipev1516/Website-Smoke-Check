from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
#options.binary_location = "C:\\Program Files\\Chrome\\chrome64_55.0.2883.75\\chrome.exe"
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'C:\Selenium\Chrome\76.0.3809.68\chromedriver_win32\chromedriver.exe')
driver.get('http://google.com/')
print("Chrome Browser Invoked")
driver.quit()
