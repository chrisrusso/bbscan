from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = 'chrusso'
password = 'KCCqHhdfuf'

# Google Chrome 
driver = webdriver.Chrome()

driver.get('https://www.bustabit.com/login/')

# Select the Python language option
python_link = driver.find_elements_by_xpath("//html/body/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[1]/div/span/input")[0]


#llenamos el username
elem = driver.find_elements_by_xpath("//html/body/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[1]/div/span/input")
elem.send_keys(username)

#llenamos el password
elem = driver.find_elements_by_xpath("//html/body/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/span/input")
elem.send_keys(password)

#enviar

elem.click()

#click en los records
elem = driver.find_elements_by_xpath("//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div[1]/div/ul/li[2]/a")
elem.click()

#click en keyboard por si las dudas
elem = driver.find_elements_by_xpath("//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[4]/div/div/button/span[2]")
elem.click()