from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/georgehanna/Downloads/chromedriver-mac-x64/chromedriver"

service = Service(executable_path = path)
driver = webdriver.Chrome(service = service)
driver.get(website)