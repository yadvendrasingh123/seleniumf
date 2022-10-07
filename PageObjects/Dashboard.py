
class dashboard:
    def __init__(self,driver):
        self.driver = driver
        self.nav_logo_amazon_xpath = "//a[@id='nav-logo-sprites']"
        self.select_address_xpath = "//span[@id='glow-ingress-line2']"
        self.button_dropdwonbox_xpath = "//select[@id='searchDropdownBox']"
        self.select_mobileapp_categories_xpath = "//option[contains(text(),'Apps & Games')]"
        self.input_searchtab_xpath = "//input[@id='twotabsearchtextbox']"
        self.search_navbar_xpath = "//input[@id='nav-search-submit-button']"
        self.select_languagebutton_xpath = "//span[@class='icp-nav-language']"
        self.select_telgulang_xpath = "//body/div[@id='a-page']/div[contains(@class,'a-row')]"
        self.hover_signin_button_xpath = "//span[normalize-space()='Account & Lists']"
        self.button_returns_orders_xpath = "//*[@id='nav-orders']"
        self.button_add_cart_xpath = "//span[normalize-space()='Cart']"
        self.previous_icon_xpath = "//i[@class='a-icon a-icon-previous-rounded']"
        self.click_next_icon_xpath = "//i[@class='a-icon a-icon-next-rounded']"
        self.button_menu_xpath = "//i[@class='hm-icon nav-sprite']"
        self.button_echo_alexa_xpath = "//div[normalize-space()='Echo & Alexa']"
        self.button_sell_xpath = "//a[normalize-space()='Sell']"
        self.select_all_new_echo_xpath = "//a[normalize-space()='All-new Echo Dot (4th Gen)']"
        self.button_bestseller_xpath = "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']"
        self.button_mobile_xpath = "//a[contains(text(),'Mobiles')]"
        self.button_books_xpath = "//a[normalize-space()='Books']"
        self.button_customer_service_xpath = "//a[normalize-space()='Customer Service']"
        self.button_todaysdeals_xpath = "//a[@href='/deals?ref_=nav_cs_gb']"
        self.button_electronics_xpath = "//a[contains(text(),'Electronics')]"
        self.button_fashion_xpath = "//a[contains(text(),'Fashion')]"
        self.fashion_kids_xpath = "//span[normalize-space()='Kids']"
        self.hoverbutton_prime_xpath = "//span[normalize-space()='Prime']"
        self.button_prime_dropdown_xpath = "//a[@id='nav-link-amazonprime']"
        self.button_newrelease_xpath = "//a[normalize-space()='New Releases']"
        self.button_home_kitchen_xpath = "//a[normalize-space()='Home & Kitchen']"
        self.button_shoppingmadeeasy_xpath = "//a[@aria-label='Amazon App']"
        self.button_amazonpay_status_xpath = "//a[normalize-space()='Amazon Pay']"
        self.button_computers_xpath = "//a[normalize-space()='Computers']"
        self.button_coupon_xpath = "//a[normalize-space()='Coupons']"
        self.button_sidebar_xpath = "//i[@class='a-icon a-icon-next-rounded']"
        self.button_signin_xpath = "//a[@class='action-button']"
        self.aboutus_status_xpath = "//a[normalize-space()='About Us']"
        self.carrier_xpath = "//a[normalize-space()='Careers']"
        self.button_pressreleases_footer_xpath = "//a[normalize-space()='Press Releases']"
        self.button_amazon_cares_xpath = "//a[normalize-space()='Amazon Cares']"
        self.button_GiftAsmile_xpath = "//a[normalize-space()='Gift a Smile']"
        self.button_AmozonScience_xpath = "//a[normalize-space()='Amazon Science']"
        self.button_Facbook_xpath = "//a[normalize-space()='Facebook']"
        self.button_Twitter_xpath = "//a[normalize-space()='Twitter']"
        self.button_Instagram_xpath = "//a[normalize-space()='Instagram']"
        self.button_SellonAmazon_xpath = "//a[normalize-space()='Sell on Amazon']"
        self.button_AmazonAccelerator_xpath = "//a[normalize-space()='Sell under Amazon Accelerator']"
        self.button_Amaozon_globing_selling_xpath = "//a[normalize-space()='Amazon Global Selling']"
        self.button_Becomean_Affiliate_xpath = "//a[normalize-space()='Become an Affiliate']"
        self.button_fulfilmentby_amazon_xpath = "//a[normalize-space()='Fulfilment by Amazon']"
        self.button_Adverties_your_product_xpath = "//a[normalize-space()='Advertise Your Products']"
        self.button_Amozonpay_merrchants_xpath = "//a[normalize-space()='Amazon Pay on Merchants']"
        self.button_covid19_xpath = "//a[normalize-space()='COVID-19 and Amazon']"
        self.button_YourAccount_xpath = "//a[@class='nav_a'][normalize-space()='Your Account']"
        self.button_Returns_center_xpath = "//a[normalize-space()='Returns Centre']"
        self.button_Purchase_protection_xpath = "//a[normalize-space()='100% Purchase Protection']"
        self.button_App_download_xpath = "//a[normalize-space()='Amazon App Download']"
        self.button_Assistant_download_xpath = "//a[normalize-space()='Amazon Assistant Download']"
        self.button_help_xpath = "//a[normalize-space()='Help']"


    def click_amazon_logo(self):
           return self.driver.find_element_by_xpath(self.nav_logo_amazon_xpath).click()

    def click_address(self):
          return self.driver.find_element_by_xpath( self.select_address_xpath).click()

    def click_allbox(self):
            return self.driver.find_element_by_xpath(self.button_dropdwonbox_xpath).click()

    def click_categories(self):
            return self.driver.find_element_by_xpath(self.select_mobileapp_categories_xpath).click()

    def input_search(self,Mobile):
        return self.driver.find_element_by_xpath( self.input_searchtab_xpath).send_keys(Mobile)

    def search_button(self):
        return self.driver.find_element_by_xpath(self.search_navbar_xpath).click()

    def click_language(self):
        return self.driver.find_element_by_xpath( self.select_languagebutton_xpath).click()

    def click_telgu(self):
        return self.driver.find_element_by_xpath(self.select_telgulang_xpath).click()

    def hover_signin(self):
        return self.driver.find_element_by_xpath( self.hover_signin_button_xpath)

    def click_retuensorders(self,):
        return self.driver.find_element_by_xpath(self.button_returns_orders_xpath).click()

    def click_addtocart(self):
        return self.driver.find_element_by_xpath( self.button_add_cart_xpath).click()

    def click_icon_status(self):
        return self.driver.find_element_by_xpath(self.previous_icon_xpath).click()

    def click_next_icon_status(self):
        return self.driver.find_element_by_xpath(self.click_next_icon_xpath).click()



    def click_all_menubar(self):
        return self.driver.find_element_by_xpath(self.button_menu_xpath).click()

    def click_Alexa_echo(self):
        return self.driver.find_element_by_xpath(self.button_echo_alexa_xpath).click()

    def click_all_newecho(self):
        return self.driver.find_element_by_xpath(self.select_all_new_echo_xpath).click()

    def click_sell_status(self):
        return self.driver.find_element_by_xpath(self.button_sell_xpath).click()


    def click_bestseller(self):
        return self.driver.find_element_by_xpath(self.button_bestseller_xpath).click()

    def click_mobile(self):
        return self.driver.find_element_by_xpath(self.button_mobile_xpath).click()

    def click_books_status(self):
        return self.driver.find_element_by_xpath(self.button_books_xpath).click()

    def click_customerservice(self):
        return self.driver.find_element_by_xpath(self.button_customer_service_xpath).click()

    def click_todaydeals_status(self):
        return self.driver.find_element_by_xpath(self.button_todaysdeals_xpath).click()

    def click_electronic_status(self):
        return self.driver.find_element_by_xpath(self.button_electronics_xpath ).click()

    def click_fashion_status(self):
        return self.driver.find_element_by_xpath(self.button_fashion_xpath).click()

    def click_kids(self):
        return self.driver.find_element_by_xpath(self.fashion_kids_xpath).click()


    def hover_prime(self):
        return self.driver.find_element_by_xpath(self.hoverbutton_prime_xpath)


    def click_prime(self):
        return self.driver.find_element_by_xpath(self.button_prime_dropdown_xpath).click()

    def click_newrelease(self):
        return self.driver.find_element_by_xpath( self.button_newrelease_xpath).click()

    def click_homekitchen_status(self):
        return self.driver.find_element_by_xpath(self.button_home_kitchen_xpath ).click()

    def click_shopping_easy(self):
        return self.driver.find_element_by_xpath( self.button_shoppingmadeeasy_xpath).click()


    def click_amazonpay(self):
        return self.driver.find_element_by_xpath(self.button_amazonpay_status_xpath).click()

    def click_computers_status(self):
        return self.driver.find_element_by_xpath(self.button_computers_xpath).click()

    def click_coupons(self):
        return self.driver.find_element_by_xpath(self.button_coupon_xpath).click()

    def click_sidebar(self):
        return self.driver.find_element_by_xpath(self.button_sidebar_xpath).click()

    def click_signin(self):
        return self.driver.find_element_by_xpath(self.button_signin_xpath).click()


    def click_aboutus(self):
        return self.driver.find_element_by_xpath(self.aboutus_status_xpath).click()

    def click_carrier(self):
        return self.driver.find_element_by_xpath(self.carrier_xpath).click()

    def click_pressreleasef(self):
        return self.driver.find_element_by_xpath( self.button_pressreleases_footer_xpath).click()
    #
    def click_Amazoncare(self):
        return self.driver.find_element_by_xpath(self.button_amazon_cares_xpath).click()
    #
    def click_gift_a_smile(self):
        return self.driver.find_element_by_xpath(self.button_GiftAsmile_xpath).click()
    #
    def click_AmozonScience(self):
       return self.driver.find_element_by_xpath(self.button_AmozonScience_xpath).click()

    def click_Facbook(self):
        return self.driver.find_element_by_xpath( self.button_Facbook_xpath ).click()

    def click_Twitter(self):
        return self.driver.find_element_by_xpath(self.button_Twitter_xpath).click()

    def click_Instagram(self):
        return self.driver.find_element_by_xpath(self.button_Instagram_xpath).click()
    def click_sellAmozon(self):
        return self.driver.find_element_by_xpath(self.button_SellonAmazon_xpath).click()

    def click_AmazonAccelertor(self):
        return self.driver.find_element_by_xpath(self.button_AmazonAccelerator_xpath).click()

    def click_globingselling_status(self):
        return self.driver.find_element_by_xpath(self.button_Amaozon_globing_selling_xpath).click()



    def click_Affiliate(self):
        return self.driver.find_element_by_xpath(self.button_Becomean_Affiliate_xpath).click()
    def click_fulfilment(self):
        return self.driver.find_element_by_xpath(self.button_fulfilmentby_amazon_xpath).click()

    def click_yourproduct(self):
        return self.driver.find_element_by_xpath(self.button_Adverties_your_product_xpath).click()

    def click_Amazonmerchant(self):
        return self.driver.find_element_by_xpath( self.button_Amozonpay_merrchants_xpath).click()


    def click_covid19(self):
        return self.driver.find_element_by_xpath(self.button_covid19_xpath).click()

    def click_yourAccount(self):
        return self.driver.find_element_by_xpath(self.button_YourAccount_xpath).click()

    def click_Returns_center(self):
        return self.driver.find_element_by_xpath (self.button_Returns_center_xpath).click()

    def click_purchase_protection_status(self):
        return self.driver.find_element_by_xpath(self.button_Purchase_protection_xpath).click()


    def click_Appdownload(self):
        return self.driver.find_element_by_xpath( self.button_App_download_xpath).click()


    def click_Assistant_download(self):
        return self.driver.find_element_by_xpath(self.button_Assistant_download_xpath).click()



    def click_help(self):
        return self.driver.find_element_by_xpath(self.button_help_xpath).click()

    def click_mmobile(self):
        return self.driver.find_element_by_xpath(self.button_mmobile_xpath).click()


























