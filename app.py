from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://10fastfingers.com/login')

time.sleep(3)

email_input = driver.find_element_by_id("UserEmail")
# Your email here
email_input.send_keys("mail@domain.com")

password_input = driver.find_element_by_id("UserPassword")
# Your password here
password_input.send_keys("password")

login_button = driver.find_element_by_id("login-form-submit")
login_button.click()

time.sleep(3)

input_element = driver.find_element_by_id("inputfield")

done = False
while not done:
    try:
        wpm_element = driver.find_element_by_id("wpm")
        print(wpm_element)
        done = True

    except:
        highligt_element = driver.find_element_by_class_name('highlight')
        word = highligt_element.get_attribute('innerHTML')
        input_element.send_keys(word + " ")
        time.sleep(random.random()/3)