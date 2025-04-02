import os
from pathlib import Path
import openpyxl

import requests
from robocorp import browser, vault
from robocorp.tasks import task
from RPA.Excel.Files import Files as Excel

## additional
from datetime import datetime, timedelta

FILE_NAME = "challenge.xlsx"
EXCEL_URL = f"https://rpachallenge.com/assets/downloadFiles/{FILE_NAME}"
OUTPUT_DIR = Path(os.getenv("ROBOT_ARTIFACTS", "output"))


@task
def solve_challenge():
    """
    Main task which solves the RPA challenge!

    Downloads the source data Excel file and uses Playwright to fill the entries inside
    rpachallenge.com.
    """
    browser.configure(
        browser_engine="chromium",
        screenshot="only-on-failure",
        headless=False, #True
    )
    try:
        """
        Parameters:
        user_info - login information
        input_date - range of days looking to book
        course_name - 'south' or 'north'
        """

        user_info = vault.get_secret('TorreyLoginPersonal')
        print(user_info)

        #### date range
        ## get todays date, with in the week or beyond the week

        #### login
        page = browser.goto("https://foreupsoftware.com/index.php/booking/19347#/login")
        tp_login(user_info, page=page)
        print('Logged In')

        #### get to schedule
        # browser.wait_for_page_to_load()        
        page.click('id=reservations-tab')
        page.click("xpath=//a[@class='btn btn-primary' and text()='Reserve a time now.']")

        ## options here for navigation
        ## residents, date range, course_name
        input_date = datetime(2025, 6, 5).date()
        course_name = 'south'.lower()

        start_of_range = datetime.today().date()
        end_of_range = start_of_range + timedelta(days=7)

        ## drop down course select
        page.click("id=schedule_select")
        # if course_name == 'south':
        #     page.click("xpath=//option[@value='1487']")
        # elif course_name == 'north':
        #     page.click("xpath=//option[@value='1487']")

        # if input_date < end_of_range:
        #     print("0-7")
        #     page.click("xpath=//a[@class='btn btn-primary' and text()='Reserve a time now.']")
        # elif input_date > end_of_range:
        #     print("7+")
        #     page.click("xpath=//a[@class='btn btn-primary' and text()='Reserve a time now.']")

        
        browser.screenshot()

        # page.click("button:text('Start')")

    finally:
        # A place for teardown and cleanups. (Playwright handles browser closing)
        print("Automation finished!")
        # page.close_browser()


def tp_login(row: dict, *, page: browser.Page):
    """
    Fills a single form with the information of a single row from the table.

    Args:
        row: One row from the generated table out of the input Excel file.
        page: The page object over which the browser interactions are done.
    """
    field_data_map = {
        "username": "User Name", #form_field_username
        "password": "Password", #form_field_password
    }

    print('HERE!', row['User Name'])
    for field, key in field_data_map.items():
        print(field, key)
        page.wait_for_selector("//input[@name='username']", timeout=30000)
        page.fill(f"//input[@name='{field}']", row[key])
    
    # page.click("input:text('login_button')")
    page.click("input[type='submit'][name='login_button']")
