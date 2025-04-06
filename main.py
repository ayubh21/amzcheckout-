import time
import os
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from  dotenv import dotenv_values, load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'
driver = webdriver.Chrome()
load_dotenv()

def main():
   print("loading page ...")
   init_page()
   print("attempting to log in...")
   login()

def init_page():
    driver.get(url)
def login():
    try:
        is_email_passed = enter_email()
        if is_email_passed:
            click_continue()
        time.sleep(10)
        is_password_passed = enter_password()
        if is_password_passed:
            click_continue()
            time.sleep(10)
        is_homepage_loaded()
        print("log in successful")
    except NoSuchElementException:
        print("element could not be found")

def  wait_page_load(element_id):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,element_id)))
        return True
    except TimeoutException:
        print("Timed out waiting for page to load.")
        return False
def enter_email():
    is_email_found = wait_page_load("ap_email")
    if is_email_found:
        email_input = driver.find_element(By.ID, "ap_email")
        email_input.send_keys(os.getenv("AMZ_EMAIL"))
        return True
    return False

def  enter_password():
    is_password_found= wait_page_load("ap_password")
    if is_password_found:
        password_input = driver.find_element(By.ID, "ap_password")
        password_input.send_keys(os.getenv("AMZ_PASSWORD"))
        return True

def click_continue():
    driver.find_element(By.CLASS_NAME, "a-button-input").click()

def is_homepage_loaded():
    wait_page_load("nav-logo-sprites")

main()

