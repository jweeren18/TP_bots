## log in to torry pines website
## 8/11
## Jake W

## imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import sys
from selenium.webdriver.support.ui import WebDriverWait


## testing
os.environ['WDM_SSL_VERIFY']='0'


## log in variables
login_url = 'https://foreupsoftware.com/index.php/booking/index/19347#/login'
user = 'jweeren97@gmail.com'
pwd = 'Graham01!'


## class/id/selecotr of user name and passowrd
'''
<div id="form_field_username">
<input type="text" name="username" value id="login_email" placeholder="Username" size="20">

<div id="form_field_password">
<input type="password" name="password" value id="login_password" placeholder="Password" size="20">

<div id="submit_button">
<input type="submit" name="login_button" value="SIGN IN">

## error
<div id="login-error" class="alert alert-danger" style="display: none"></div>
or
<div id="user-info-error" class="alert alert-danger" style="display: none; margin-left: 15px; margin-right: 15px;"></div>
'''

html_user = 'form_field_username'
html_pass =  'form_filed_password'
submit_button = 'submit_button'

def startBot (user, pwd, url):
    # path = "C:\\Users\\Jake\\Desktop\\bots\\chromedriver"

    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome()
     
    # opening the website in chrome.
    driver.get(url)
     
    user_test = driver.find_element(By.NAME, "username") #.send_keys(user)
    print(user_test)
    # sys.exit()

    # find the password by inspecting on password input
    driver.find_element(By.NAME, "password").send_keys(pwd)
     
    # click on submit
    driver.find_element(By.NAME, "login_button").click()


    WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Incorrect username or password."
    # get the errors (if there are)
    errors = driver.find_elements("css selector", ".flash-error")
    # print the errors optionally
    # for e in errors:
    #     print(e.text)
    # if we find that error message within errors, then login is failed
    if any(error_message in e.text for e in errors):
        print("[!] Login failed")
    else:
        print("[+] Login successful")

print('hi')
# Call the function
startBot(user, pwd, login_url)




