import json
import time

from selenium import webdriver


def load_cookies_into_selenium(driver, path_to_cookie_file):
    with open(path_to_cookie_file, 'r') as cookies_file:
        cookies = json.load(cookies_file)

    for cookie in cookies:

        if 'expiry' in cookie:
            cookie['expiry'] = int(cookie['expiry'])


        if 'sameSite' in cookie:
            if cookie['sameSite'] not in ["Strict", "Lax", "None"]:
                cookie['sameSite'] = "None"
        else:
            cookie['sameSite'] = "None"


        driver.add_cookie(cookie)


driver = webdriver.Chrome()
driver.get("https://instagram.com/")
load_cookies_into_selenium(driver, "cookies_file_instagram.js")
driver.get("https://instagram.com/")
time.sleep(30)
