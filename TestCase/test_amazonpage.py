
from PageObjects.Dashboard import dashboard
from selenium.webdriver import ActionChains
from Utilities.Logger import logclass
import configparser

config = configparser.ConfigParser()
config.read("Utilities/.properties")

import pytest
@pytest.mark.usefixtures("setup")
class TestAmazonpage(logclass):
    def test_001(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("amazon logo start")
        db.click_amazon_logo()
        log.info("your select address")
        db.click_address()

    def test_002(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("all dropdown menu")
        db.click_allbox()
        log.info("select categories")
        db.click_categories()
        log.info("input field")
        db.input_search("Mobile")
        log.info("search the categories")
        db.search_button()

    def test_003(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("select the language")
        db.click_language()
        db.click_telgu()

    def test_004(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("previous icon")
        db.click_icon_status()
        db.click_next_icon_status()

    def test_005(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("hover in sign button")
        ActionChains(self.driver).move_to_element(db.hover_signin()).perform()
        log.info("clicked in return orders")
        ActionChains(self.driver).context_click(db.click_retuensorders()).perform()

    def test_006(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("add to cart")
        db.click_addtocart()


    def test_007(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("dropdown menubar")
        db.click_all_menubar()
        log.info("clicked alexa echo")
        db.click_Alexa_echo()
        log.info("clicked all new echo 4g ")
        db.click_all_newecho()


    def test_008(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        db.click_sell_status()

    def test_009(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("clicked the bestseller button")
        db.click_bestseller()
        log.info("clicked the mobile ")
        db.click_mobile()
        log.info("clicked customer service button")
        db.click_customerservice()
        log.info("clicked books ")
        db.click_books_status()

    def test_010(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("clicked the todays deals button")
        db.click_todaydeals_status()
        log.info("clicked electronic button")
        db.click_electronic_status()
        log.info("clicked fashion button")
        db.click_fashion_status()
        log.info("clicked kids button")
        db.click_kids()
        log.info("hover on prime button")
        ActionChains(self.driver).move_to_element(db.hover_prime()).perform()
        log.info("prime button")
        db.click_prime()
        db = dashboard(self.driver)
        log.info("clicked new release")
        db.click_newrelease()

    def test_011(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("homekitchen button")
        db.click_homekitchen_status()


    def test_012(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("amazon pay button")
        db.click_amazonpay()
        log.info("computers button")
        db.click_computers_status()
    #
    def test_013(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("clicked to coupons")
        db.click_coupons()

    def test_014(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("sign in option")
        # self.driver.execute_script("window.scrollBy(0,5600)")
        db.click_signin()

    def test_015(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("about section")
        db.click_aboutus()
        log.info("carrier section")
        db.click_carrier()

    def test_016(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("press release")
        db.click_pressreleasef()

    def test_017(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("amazon care section ")
        db.click_Amazoncare()
        log.info("gift smile section")
        db.click_gift_a_smile()

    def test_018(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("amazon science")
        db.click_AmozonScience()

    def test_019(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("facbook section")
        db.click_Facbook()

    def test_020(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("Twitter section")
        db.click_Twitter()

    def test_021(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("Instagram")
        db.click_Instagram()

    def test_022(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        db.click_sellAmozon()
        log.info("amazon acceletor")
        db.click_AmazonAccelertor()
        log.info("global selling")
        db.click_globingselling_status()

    def test_023(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("affilate")
        db.click_Affiliate()

    def test_024(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("your product")
        db.click_yourproduct()

    def test_025(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("amazon merchant")
        db.click_Amazonmerchant()

    def test_026(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("covid 19")
        db.click_covid19()
        log.info("your account")
        db.click_yourAccount()
        log.info("returns center")
        db.click_Returns_center()

    def test_027(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("purchase protection")
        db.click_purchase_protection_status()

    def test_028(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("app download ")
        db.click_Appdownload()
        log.info(" amazon assitant")
        db.click_Assistant_download()

    def test_029(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        log.info("help section")
        db.click_help()
    def test_030(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        db.click_mobile()