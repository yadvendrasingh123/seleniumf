import time
from PageObjects.LoginPage import Login
from PageObjects.Addtocart import addtocart
from selenium.webdriver import ActionChains
from Utilities.Logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/.properties")

import pytest

@pytest.mark.usefixtures("setup")
class TestAmazonpage(logclass):
    def test_01(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        log.info("search mobile")
        ad.click_mobile()
        log.info("click computer peripherals device")
        ad.click_computer()
        log.info("mouse image")
        ad.click_mouseimage()
        log.info("click quantity")
        ad.click_quantity()
        log.info("add to addcart")
        ad.click_addcart()



    def test_02(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        log.info("all dropdown menu")
        ad.click_allbox()
        log.info("select categories")
        ad.click_categories()
        log.info("input field")
        ad.input_search("Mobile")
        log.info("search the categories")
        ad.search_button()


    def test_03(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        log.info("hover in sign button")
        ActionChains(self.driver).move_to_element(ad.hover_sign_button()).perform()
        ad.click_start_here()
        ad.input_name("Yadvendra")
        ad.input_mobile(config.get("credential","correct_mobile"))
        ad.input_email(config.get("credential","correct_email"))
        ad.input_password(config.get("credential","correct_password"))
        ad.click_submit()

    def test_04(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        log.info("clicked the todays deals button")
        ad.click_todaydeals_status()
        log.info("clicked electronic button")
        ad.click_electronic_status()
        log.info("clicked fashion button")
        ad.click_fashion_status()
        log.info("clicked kids button")
        ad.click_kids()
        log.info("kids t-shirt")
        ad.click_bags()

    def test_05(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        ad.click_all_nav()
        log.info("dropdown")
        ad.click_dropdown()
        log.info("men fashion")
        ad.click_men_fashion_status()
        log.info("click tshirt")
        ad.click_tshirtpolos()
        time.sleep(2)
        log.info("t-shirt L size")
        ad.click_size()
        log.info("click best selling")
        ad.click_bestselling()
        log.info("price high to low")
        ad.click_price_status()

    def test_06(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        log.info("input field")
        ad.click_inputfield("shirt")
        log.info("search button")
        ad.click_searchbutton()


    def test_07(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        ad.click_right_sidebar()

    def test_08(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        log.info("clicked location")
        ad.click_location_status()
        log.info("pincode location")
        ad.input_pincode_status(config.get("credential","correct_pincode"))
        log.info("apply location")
        time.sleep(3)
        ad.click_apply()
    #
    def test_09(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        ad.click_fashion1()
        ad.click_salesdeal_status()
        ad.click_shopnow()


    def test_10(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        ad = addtocart(self.driver)
        ad.click_sell()
        ad.click_startselling()
        lg.input_username(config.get("credential", "correct_username"))
        log.info("Enter username")
        lg.input_password(config.get("credential", "correct_password1"))
        log.info("Enter password")
        lg.click_login()
        log.info("Clicked login")


    def test_11(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        ad= addtocart(self.driver)
        log.info("clicked bestseller")
        ad.click_bestseller()
        log.info("clicked product image")
        ad.click_productimage()
        log.info("share the link of product")
        ad.click_share1()
        log.info("clicked email button")
        ad.click_sharetoemail()

    def test_12(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        ad = addtocart(self.driver)
        log.info("clicked bestseller")
        ad.click_bestseller()
        log.info("clicked product image")
        ad.click_productimage()
        log.info("review rating")
        ad.click_reviewrating()
        # self.driver.execute_script("window.scrollBy(0,7560)")
        log.info("write the review section")
        ad.click_writereview()

    def test_13(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        ad = addtocart(self.driver)
        ad.click_mobile()
        log.info("click computer peripherals device")
        ad.click_checkbox1()
        log.info("click checkbox")
        ad.click_checkbox2()

    def test_14(self):
        log = self.getthelogs()
        ad = addtocart(self.driver)
        lg = Login(self.driver)
        log.info("search mobile")
        ad.click_mobile()
        log.info("click computer peripherals device")
        ad.click_computer()
        log.info("mouse image")
        ad.click_mouseimage()
        log.info("click quantity")
        ad.click_quantity()
        log.info("add to addcart")
        ad.click_buybutton()
        lg.input_username(config.get("credential", "correct_email1"))
        lg.click_continue()
        time.sleep(2)
        lg.input_password(config.get("credential", "correct_password2"))
        lg.click_continue()

    def test_15(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        ad = addtocart(self.driver)
        lg.click_inputsearch2(config.get("credential", "correct_inputfield"))
        lg.click_searchbutton()
        ad.click_productimage1()
        if 'Deal Price' in ad.pricemsg():
            assert True
            print("it is present")
        else:
            assert False


