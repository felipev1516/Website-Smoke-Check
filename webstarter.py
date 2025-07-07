import selenium.webdriver as webdriver
import time

#def get_results(search_term):
url = "https://www.bing.com"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)
browser.close()
	
