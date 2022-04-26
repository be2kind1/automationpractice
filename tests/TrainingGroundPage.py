import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class test_TrainingGroundPage(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.automationpractice.com'
        pass
    def go(self):
        self.driver.get(self.url)


    def add_into_email(self, text):
        wait = WebDriverWait(self.driver, 10)

        inpt = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
        inpt.clear()
        inpt.send_keys(text)
        return None
    def add_into_email_create(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = wait.until(EC.element_to_be_clickable((By.ID, 'email_create')))
        inpt.clear()
        inpt.send_keys(text)
        return None

    def get_input_text(self):
        wait = WebDriverWait(self.driver, 10)
        inpt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/h1')))
        elem_text = inpt.get_attribute('value')
        return elem_text


    def click_button_1(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')))
        button.click()
        return None


    def click_button_0(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.ID, 'SubmitLogin')))
        button.click()
        return None

    def go_to_store(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]/a')))
        button.click()
        return None

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/ul/li[2]/div/div[2]/div[2]/a[1]/span')))
        button.click()
        return None
    def add_to_cart2(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[3]/div/div/div[5]')))
        button.click()
        return None
    def go_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a')))
        button.click()
        return None
    def rem_from_cart(self):
        button = self.driver.find_element_by_class_name('icon-trash')
        button.click()
        return None
    def alerts(self):
        wait = WebDriverWait(self.driver, 10)
        alerts = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p')))

    def check_out1(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')))
        button.click()
        return None
    def check_out2(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="center_column"]/form/p/button/span')))
        button.click()
        return None
    def check_box(self):
        wait = WebDriverWait(self.driver, 10)
        button = self.driver.find_element_by_xpath('//*[@id="uniform-cgv"]')
        button.click()
        return None
    #Payment by credit card
    def check_out3(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/p/button')))
        button.click()
        return None
    #Payment by check
    def check_out3_1(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')))
        button.click()
        return None
    def check_out4(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a/span')))
        button.click()
        return None
    def reg_me(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitAccount"]')))
        button.click()
        return None

    def check_out5(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart_navigation"]/button')))
        button.click()
        return None
    def add_into_firstname(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="customer_firstname"]')))
        inpt.clear()
        inpt.send_keys(text)
        return None
    def add_into_lastname(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="customer_lastname"]')))
        inpt.clear()
        inpt.send_keys(text)
        return None
    def add_into_day(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = self.driver.find_element_by_xpath('//*[@id="days"]')
        inpt.send_keys(text)

        return None
    def add_into_month(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = self.driver.find_element_by_xpath('//*[@id="months"]')
        inpt.send_keys(text)
        return None
    def add_into_year(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = self.driver.find_element_by_xpath('//*[@id="years"]')
        inpt.send_keys(text)
        return None
    def select_gender(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_gender1"]')))
        button.click()
        return None
    def add_into_adress(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="address1"]')))
        inpt.clear()
        inpt.send_keys(text)
        return None
    def add_into_city(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="city"]')))
        inpt.clear()
        inpt.send_keys(text)
        return None
    def add_into_state(self, text):
        wait = WebDriverWait(self.driver, 10)
        button = self.driver.find_element_by_xpath('//*[@id="id_state"]/option[3]')
        button.click()
        return None
    def add_into_post(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="postcode"]')))
        inpt.send_keys(text)
        return None
    def add_into_mobile(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="phone_mobile"]')))
        inpt.clear()
        inpt.send_keys(text)
        return None
    def submit_account(self, text):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitAccount"]')))
        button.click()
        return None

    def add_into_pass(self, text):
        wait = WebDriverWait(self.driver, 10)
        inpt = wait.until(EC.element_to_be_clickable((By.ID, 'passwd')))
        inpt.clear()
        inpt.send_keys(text)
        return None

    def create_user(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SubmitCreate"]/span/i')))
        button.click()
        return None

