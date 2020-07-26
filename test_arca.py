from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

def setUp(driver):
    url = "https://demodirectory.com/profile/login.php"
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]")))
    except:
        print("nao encontrou o elemento")


def later(driver):
    try:
        assert driver.current_url == "https://demodirectory.com/profile/add.php?"
        validation = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/p").text 
        if validation.find("Captcha validation failed") != -1:
            print("True phrase Captcha")
        else:
            print("False phrase Captcha")
        if validation.find("Please enter a valid e-mail.") != -1:
            print("True phrase email")
        else:
            print("False phrase email")
        if validation.find("Please enter a password with a minimum of 4 characters") != -1:
            print("True phrase password")
        else:
            print("False phrase password")
    except:
        print("campo nao preenchido")
        window = driver.current_url
        if window != "https://demodirectory.com/profile/add.php?":
            print("false URL")
        else:
            print("true URL")
        

def test_SignUp():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("username").send_keys("vitor@gmail.com")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    time.sleep(5)
    later(driver)

def test_offName():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click()
    later(driver)

def test_off_last():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_email():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)
    
def test_off_password():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_checkbox():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_name_last():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_name_email():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_name_senha():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_name_checkbox():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_css_selector(".form-button").click()
    later(driver) 

def test_off_last_email():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_last_password():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_last_checkbox():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_css_selector(".form-button").click()
    later(driver) 

def test_off_email_password():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click()
    later(driver)

def test_off_email_checkbox():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_name_last_email():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_name_last_password():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_name_last_checkbox():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("username").send_keys("vitor@hotmail.com")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_css_selector(".form-button").click()
    later(driver)

def test_off_last_email_password():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_last_email_check():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("password").send_keys("teste_vitor4")
    driver.find_element_by_css_selector(".form-button").click()
    later(driver) 

def test_off_email_password_check():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_css_selector(".form-button").click()
    later(driver)

def test_incomplete_password_email():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("username").send_keys("teste@teste")
    driver.find_element_by_id("password").send_keys("tes")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click()
    later(driver) 

def test_incomplete_password():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("username").send_keys("teste@htomail.com")
    driver.find_element_by_id("password").send_keys("tes")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click()
    later(driver) 

def test_invalid_email():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_id("first_name").send_keys("teste_vitor")
    driver.find_element_by_id("last_name").send_keys("teste_vitor2")
    driver.find_element_by_id("username").send_keys("teste@teste")
    driver.find_element_by_id("password").send_keys("teste")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_off_all():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_css_selector(".form-button").click() 
    later(driver)

def test_click_links():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_link_text("Terms of Service").click()
    driver.find_element_by_link_text("Privacy Policy").click()
    driver.find_element_by_css_selector(".not-member").click()
    window = driver.current_url
    if window != "https://demodirectory.com/profile/add.php?":
        print("false URL")
    else:
        print("true URL")

def test_getTermsOfUse():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_link_text("Terms of Service").click()
    time.sleep(5)
    driver.switch_to_window(driver.window_handles[1])
    window = driver.current_url
    if window != "https://demodirectory.com/profile/add.php?":
        print("false URL")
    else:
        print("true URL")

def test_getPrivacyPolicy():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_link_text("Privacy Policy").click()
    time.sleep(5)
    driver.switch_to_window(driver.window_handles[1])
    window = driver.current_url
    if window != "https://demodirectory.com/profile/add.php?":
        print("false URL")
    else:
        print("true URL")

def test_back_window():
    driver = webdriver.Firefox()
    setUp(driver)
    driver.find_element_by_css_selector(".not-member").click() 
    window = driver.current_url
    if window != "https://demodirectory.com/profile/add.php?":
        print("false URL")
    else:
        print("true URL")
    

def tearDown(self):         
    self.driver.quit()
        
