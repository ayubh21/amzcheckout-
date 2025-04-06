import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from  dotenv import dotenv_values, load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'
driver = webdriver.Chrome()


def main():
   print("loading page ...")
   init_page()
   print("attempting to log in...")
   login()
def init_page():
    driver.get(url)
    time.sleep(10)
def login():
    config = dotenv_values(".env")
    for value, index in  config.items():
        match config.keys():
            case "AMZ_EMAIL":
                is_email_found = wait_page_load("email")
                if is_email_found:
                     email_input = driver.find_element(By.NAME, "email")
                     print("hello")
                     print(email_input)
                     email_input.send_keys(value)
            case "AMZ_PASSWORD":
                is_password_found = wait_page_load("password")
                if is_password_found:
                    password_input = driver.find_element(By.NAME, "password")
                    password_input.send_keys(value)
            case _:
                print("failed to send key press, element not found")


# not entering my switch can't recognize key?
def  wait_page_load(name):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, name)))
        return True
    except TimeoutException:
        print("Timed out waiting for page to load.")
        return False


main()

