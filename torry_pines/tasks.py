import os
from pathlib import Path
import openpyxl

import requests
from robocorp import browser
from robocorp.tasks import task
from RPA.Excel.Files import Files as Excel

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

        ## get login info
        wb = openpyxl.load_workbook('sample_login_info.xlsx')
        # Select the active sheet or specify the sheet by name
        sheet = wb.active
        header = [cell.value for cell in sheet[1]]
        
        filtered_data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Start from the second row
            row_dict = {header[i]: row[i] for i in range(len(header))}
        
            ## need better login access pre user level
            if row_dict['First Name'] == 'Jake' and row_dict['Last Name'] == 'Weeren':
                filtered_data.append(row_dict)

        if len(filtered_data) != 1:
            raise ValueError("The length of the collection must be 1.")
        else:
            print("Single Records Found!")

        user_info = filtered_data[0]

        page = browser.goto("https://foreupsoftware.com/index.php/booking/19347#/login")
        tp_login(user_info, page=page)
        print('Logged In')
        element = page.locator("css=div.account-passes")
        browser.screenshot(element)

        # page.click("button:text('Start')")

    finally:
        # A place for teardown and cleanups. (Playwright handles browser closing)
        print("Automation finished!")


def download_file(url: str, *, target_dir: Path, target_filename: str) -> Path:
    """
    Downloads a file from the given URL into a custom folder & name.

    Args:
        url: The target URL from which we'll download the file.
        target_dir: The destination directory in which we'll place the file.
        target_filename: The local file name inside which the content gets saved.

    Returns:
        Path: A Path object pointing to the downloaded file.
    """
    # Obtain the content of the file hosted online.
    response = requests.get(url)
    response.raise_for_status()  # this will raise an exception if the request fails
    # Write the content of the request response to the target file.
    target_dir.mkdir(exist_ok=True)
    local_file = target_dir / target_filename
    local_file.write_bytes(response.content)
    return local_file


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

    for field, key in field_data_map.items():
        page.fill(f"//input[@name='{field}']", str(row[key]))
    
    # page.click("input:text('login_button')")
    page.click("input[type='submit'][name='login_button']")
