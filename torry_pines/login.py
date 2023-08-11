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
from datetime import datetime
from flask import *
from forms import LoginForm
app=Flask(__name__,template_folder='template')

app.config['SECRET_KEY']='ac54fdb1fe101e5b3590000824ec1e65'

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        setUserInfo(form.email.data, form.password.data)
        startBot()
    return render_template('login_form.html',title='Login', form=form)

## testing
os.environ['WDM_SSL_VERIFY']='0'

## log in variables
with open("login_details.yaml", "r") as f:
    user_data = yaml.load(f, Loader=yaml.FullLoader)


## Login to TP website
def startBot ():
    ## login url
    login_url = 'https://foreupsoftware.com/index.php/booking/index/19347#/login'

    ## log in variables
    with open("login_details.yaml", "r") as f:
        user_data = yaml.load(f, Loader=yaml.FullLoader)
    user = user_data['user']
    pwd = user_data['pwd']

    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome()
    
    # opening the website in chrome.
    driver.get(login_url)
    
    driver.find_element(By.NAME, "username").send_keys(user)

    # find the password by inspecting on password input
    driver.find_element(By.NAME, "password").send_keys(pwd)
    
    time.sleep(1)
    # click on submit
    driver.find_element(By.NAME, "login_button").click()

    element =  driver.find_element(By.XPATH, "//a[@href='#/account/reservations']")
    print(element)
    # driver.find_element(By.ID, "reservations-tab").click()
    # <a id="reservations-tab" href="#/account/reservations">

    # driver.find_element(By.ID, "profile-main").click()

    time.sleep(300)


## Ask for user info
def setUserInfo(username, password):

    now = datetime.now()

    user_info = {
            'user' : username,
            'pwd': password,
            'date':  now.strftime("%d/%m/%Y %H:%M:%S")
        }

    with open("login_details.yaml", 'w') as yamlfile:
        data = yaml.dump(user_info, yamlfile)
        print("Write successful")


## find & book a tee time
def find_and_book():
    print('hi')





################################ run functions #############################################

# user_info()
# startBot()
# find_and_book()




