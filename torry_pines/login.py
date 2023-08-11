## log in to torry pines website
## 8/11
## Jake W

## imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import sys
import time
import yaml


## testing
# os.environ['WDM_SSL_VERIFY']='0'


yml_config = """user: jweeren97@gmail.com
pwd: Graham01!
"""

with open("login_details.yaml", "r") as f:
    user_data = yaml.load(f, Loader=yaml.FullLoader)


## log in variables
login_url = 'https://foreupsoftware.com/index.php/booking/index/19347#/login'
user = user_data['user']
pwd = user_data['pwd']

print(user, pwd)
# sys.exit()


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
    
    driver.find_element(By.NAME, "username").send_keys(user)

    # find the password by inspecting on password input
    driver.find_element(By.NAME, "password").send_keys(pwd)
     
    time.sleep(2)
    # click on submit
    driver.find_element(By.NAME, "login_button").click()

    time.sleep(10)

print('hi')
# Call the function
startBot(user, pwd, login_url)




