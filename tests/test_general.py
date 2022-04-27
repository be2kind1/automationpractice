import unittest
from TrainingGroundPage import test_TrainingGroundPage
username = "v.jakushw23ewkin@gmail.com"
password = "enot123"

from selenium import webdriver
class Test1(unittest.TestCase):
    # Registration with given config
    def test0_reg(self):
        browser = webdriver.Chrome()
        Test_page = test_TrainingGroundPage(driver=browser)
        Test_page.go()
        Test_page.click_button_1()

        Test_page.add_into_email_create(username)

        Test_page.create_user()
        browser.implicitly_wait(30)
        Test_page.add_into_firstname('Viktor')
        Test_page.add_into_pass(password)
        Test_page.add_into_lastname('jakuskin')
        Test_page.add_into_day('5')
        Test_page.select_gender()
        Test_page.add_into_year('1989')
        Test_page.add_into_month('July')
        Test_page.add_into_mobile('+37060286782')
        Test_page.add_into_post('99502')
        Test_page.add_into_city('Klaipeda')
        Test_page.add_into_state('Alaska')
        Test_page.add_into_adress('Os.Krakowiakow/Krakow')
        Test_page.reg_me()
        browser.close()
        print("User registered")

#Login
    def test1_JustLogin(self):
        browser = webdriver.Chrome()
        Test_page = test_TrainingGroundPage(driver=browser)
        Test_page.go()
        Test_page.click_button_1()
        Test_page.add_into_email(username)
        Test_page.add_into_pass(password)
        Test_page.click_button_0()
        txt_from_input = Test_page.get_input_text()

        assert browser.current_url == "http://automationpractice.com/index.php?controller=my-account"
        welcome = browser.find_element_by_xpath('//*[@id="center_column"]/p').text
        assert welcome == "Welcome to your account. Here you can manage all of your personal information and orders."
        if welcome == "Welcome to your account. Here you can manage all of your personal information and orders.":
            assert(True)
        else:
            assert(False)

        print("We logged on.")
#Add to cart
    def test2_AddToCart(self):
        browser = webdriver.Chrome()
        Test_page = test_TrainingGroundPage(driver=browser)
        Test_page.go()
        Test_page.click_button_1()
        Test_page.add_into_email(username)
        Test_page.add_into_pass(password)
        Test_page.click_button_0()
        assert browser.current_url == "http://automationpractice.com/index.php?controller=my-account"
        welcome = browser.find_element_by_xpath('//*[@id="center_column"]/p').text
        assert welcome == "Welcome to your account. Here you can manage all of your personal information and orders."
        if welcome == "Welcome to your account. Here you can manage all of your personal information and orders.":
            assert(True)

        else:
            assert(False)
        Test_page.go_to_store()
        Test_page.add_to_cart()
        Test_page.go_to_store()
        Test_page.go_to_cart()
        print("Test add to cart passed")
#Remove from Cart
    def test3_RemoveFromCart(self):
        browser = webdriver.Chrome()
        Test_page = test_TrainingGroundPage(driver=browser)
        Test_page.go()
        Test_page.click_button_1()
        Test_page.add_into_email(username)
        Test_page.add_into_pass(password)
        Test_page.click_button_0()
        Test_page.go_to_store()
        Test_page.add_to_cart()
        Test_page.add_to_cart()
        Test_page.go_to_cart()
        browser.implicitly_wait(30)
        Test_page.rem_from_cart()
        print("add/remove from cart Test passed")
#Payment via Wire method
    def test4_WirePayment(self):
        browser = webdriver.Chrome()
        Test_page = test_TrainingGroundPage(driver=browser)
        Test_page.go()
        Test_page.click_button_1()
        Test_page.add_into_email(username)
        Test_page.add_into_pass(password)
        Test_page.click_button_0()
        assert browser.current_url == "http://automationpractice.com/index.php?controller=my-account"
        welcome = browser.find_element_by_xpath('//*[@id="center_column"]/p').text
        assert welcome == "Welcome to your account. Here you can manage all of your personal information and orders."
        if welcome == "Welcome to your account. Here you can manage all of your personal information and orders.":
            assert(True)
        else:
            assert(False)
        Test_page.go_to_store()
        Test_page.add_to_cart()

        Test_page.go_to_store()
        Test_page.go_to_cart()
        Test_page.check_out1()
        Test_page.check_out2()
        Test_page.check_box()

        Test_page.check_out3()
        Test_page.check_out3_1()
        Test_page.check_out5()
        print("Wire payment method Test successfully passed")

#Payment via Card method
    def test5_CardPayment(self):
        browser = webdriver.Chrome()
        Test_page = test_TrainingGroundPage(driver=browser)
        Test_page.go()
        Test_page.click_button_1()
        Test_page.add_into_email(username)
        Test_page.add_into_pass(password)
        Test_page.click_button_0()
        assert browser.current_url == "http://automationpractice.com/index.php?controller=my-account"
        welcome = browser.find_element_by_xpath('//*[@id="center_column"]/p').text
        assert welcome == "Welcome to your account. Here you can manage all of your personal information and orders."
        if welcome == "Welcome to your account. Here you can manage all of your personal information and orders.":
            assert(True)
        else:
            assert(False)
        Test_page.go_to_store()
        Test_page.add_to_cart()
        Test_page.go_to_store()
        Test_page.go_to_cart()
        Test_page.check_out1()
        Test_page.check_out2()
        Test_page.check_box()
        Test_page.check_out3()
        Test_page.check_out4()


        print("Payment by check method test successfully passed")
