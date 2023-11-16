from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
user1 = 'standard_user'
user2 = 'locked_out_user'
user3 = 'problem_user'
user4 = 'performance_glitch_user'
user5 = 'error_user'
user6 = 'visual_user'
password = 'secret_sauce'
first_name = 'John'
last_name = 'Smith'
postal_code = '00007'
driver.get('https://www.saucedemo.com/')
username_feel = driver.find_element('xpath', '//*[@id="user-name"]')
password_feel = driver.find_element('xpath', '//*[@id="password"]')
username_feel.click()
time.sleep(2)
time.sleep(2)
username_feel.send_keys(user1)
password_feel.send_keys(password)
time.sleep(2)
driver.find_element('xpath', '//*[@id="login-button"]').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()
time.sleep(3)
driver.find_element('xpath', '//*[@id="checkout"]').click()
time.sleep(3)
first_feel = driver.find_element('xpath', '//*[@id="first-name"]')
first_feel.click()
time.sleep(2)
first_feel.send_keys(first_name)
time.sleep(2)
last_feel = driver.find_element('xpath', '//*[@id="last-name"]')
last_feel.click()
last_feel.send_keys(last_name)
time.sleep(2)
postal_feel = driver.find_element('xpath', '//*[@id="postal-code"]')
postal_feel.click()
postal_feel.send_keys(postal_code)
time.sleep(2)
driver.find_element('xpath', '//*[@id="continue"]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="finish"]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="back-to-products"]').click()
time.sleep(3)

#Home










