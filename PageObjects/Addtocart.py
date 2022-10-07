
class addtocart:
    def __init__(self,driver):
        self.driver = driver
        self.button_mobile_xpath = "//a[contains(text(),'Mobiles')]"
        self.button_computer_xpath = "//span[normalize-space()='Computer Peripherals']"
        self.image_mouse_xpath = "//img[@alt='HP X1000 Wired USB Mouse with 3 Handy Buttons, Fast-Moving Scroll Wheel and Optical Sensor works on most Surfa']"

        self.item_quantity_xpath = "//select[@id='quantity']"
        self.share_xpath = "//i[@class='ssf-share-trigger']"
        self.button_addcart_xpath = "//input[@id='add-to-cart-button']"
        self.image_productpage_xpath = "//img[@class='sc-product-image celwidget']"
        self.button_dropdwonbox_xpath = "//select[@id='searchDropdownBox']"
        self.select_mobileapp_categories_xpath = "//option[contains(text(),'Apps & Games')]"
        self.input_searchtab_xpath = "//input[@id='twotabsearchtextbox']"
        self.search_navbar_xpath = "//input[@id='nav-search-submit-button']"
        self.hover_accountlist_xpath = "//span[normalize-space()='Account & Lists']"
        self.new_customer_start_xpath = "//a[normalize-space()='Start here.']"
        self.textbox_name_xpath = "//input[@id='ap_customer_name']"
        self.textbox_mobile_number_xpath = "//input[@id='ap_phone_number']"
        self.textbox_email_xpath = "//input[@id='ap_email']"
        self.textbox_password_xpath = "//input[@id='ap_password']"
        self.button_continue_xpath = "//input[@id='continue']"
        self.button_todaysdeals_xpath = "//a[@href='/deals?ref_=nav_cs_gb']"
        self.button_electronics_xpath = "//a[contains(text(),'Electronics')]"
        self.button_fashion_xpath = "//a[contains(text(),'Fashion')]"
        self.fashion_kids_xpath = "//span[normalize-space()='Kids']"
        self.button_bags_xpath = "//li[@id='sobe_d_b_1_6']//img[@alt='Backpacks']"
        self.button_nav_all_xpath = "//i[@class='hm-icon nav-sprite']"
        self.dropdownmen_fashion_xpath = "//ul[@class='hmenu hmenu-visible']//li[17]//a[1]"
        self.dropdownmen_tshirtpolos_xpath = "//a[normalize-space()='T-shirts & Polos']"
        self.dropdown_xpath = "//ul[@class='hmenu hmenu-visible']"
        self.size_xpath = "//span[@dir='auto'][normalize-space()='L']"
        self.dropdown_bestselling_xpath = "//span[@class='a-dropdown-prompt']"
        self.button_price_xpath = "//a[@id='s-result-sort-select_2']"
        self.input_field_xpath = "//input[@id='twotabsearchtextbox']"
        self.button_search_xpath = "//input[@id='nav-search-submit-button']"
        self.checkbox_xpath = "//li[@id='p_n_feature_nineteen_browse-bin/11301357031']"

        self.button_sidebar_xpath = "//i[@class='a-icon a-icon-next-rounded']"
        self.image_topbrands_click_xpath = "//img[@alt='wa top brands']"
        self.button_location_xpath = "//a[@id='nav-global-location-popover-link']"
        self.input_pincode_xpath = "//input[@id='GLUXZipUpdateInput']"
        self.button_apply_xpath = "//input[@aria-labelledby='GLUXZipUpdate-announce']"
        self.btton_fashion1_xpath = "//a[normalize-space()='Fashion']"
        self.salesanddeals_xpath = "//span[normalize-space()='Sales & Deals']"
        self.shop_image_xpath = "//li[@id='sobe_d_b_3_1']//img[@alt='Shop now']"
        self.sell_xpath = "//a[normalize-space()='Sell']"
        self.button_selling_xpath = "//a[normalize-space()='Start Selling Now']"
        self.button_bestseller_xpath = "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']"
        self.product_image_xpath = "//img[@alt='Mi Step Out 12 L Mini Backpack (Small Size, Dark Blue, Water Repellant)']"
        self.share_image_xpath = "//i[@title='Share']"
        self.sharebyemail_xpath = "//span[@class='email-label']"
        self.review_rating_xpath ="//div[@id='averageCustomerReviews']//span[@id='acrCustomerReviewText']"
        self.buttonwrite_review_xpath = "//a[@id='a-autoid-29-announce']"
        self.checkbox1_button_xpath = "//div[@class='a-column a-span12 apb-browse-left-nav apb-browse-col-pad-right a-span-last']//div[2]//ul[1]//li[1]//span[1]//a[1]//div[1]//label[1]//i[1]"
        self.checkbox2_button_xpath = "//li[@id='p_90/6741118031']//i[@class='a-icon a-icon-checkbox']"

        self.productimage_xpath = "//div[@class='_bGlmZ_content_2rsXy']//div[1]//div[1]//a[2]//div[1]//div[1]//img[1]"
        self.button_buy_xpath = "//input[@id='buy-now-button']"
        self.price_xpath = "//td[normalize-space()='Deal Price:']"


    def click_mobile(self):
            return self.driver.find_element_by_xpath(self.button_mobile_xpath).click()

    def click_quantity(self):
        return self.driver.find_element_by_xpath( self.item_quantity_xpath).send_keys(3)

    def click_share(self):
        return self.driver.find_element_by_xpath(self.share_xpath).click()

    def click_addcart(self):
         return self.driver.find_element_by_xpath(self.button_addcart_xpath).click()

    def click_product(self):
        return self.driver.find_element_by_xpath(self.image_productpage_xpath ).click()

    def click_allbox(self):
        return self.driver.find_element_by_xpath(self.button_dropdwonbox_xpath).click()

    def click_categories(self):
        return self.driver.find_element_by_xpath(self.select_mobileapp_categories_xpath).click()

    def input_search(self, Mobile):
        return self.driver.find_element_by_xpath(self.input_searchtab_xpath).send_keys(Mobile)

    def search_button(self):
        return self.driver.find_element_by_xpath(self.search_navbar_xpath).click()

    def hover_sign_button(self):
        return self.driver.find_element_by_xpath( self.hover_accountlist_xpath)

    def click_start_here(self):
        return self.driver.find_element_by_xpath(self.new_customer_start_xpath).click()

    def input_name(self,Yadvendra):
        return self.driver.find_element_by_xpath(self.textbox_name_xpath ).send_keys(Yadvendra)
    def input_mobile(self,Mobile):
        return self.driver.find_element_by_xpath(self.textbox_mobile_number_xpath ).send_keys(Mobile)

    def input_email(self,Email):
        return self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(Email)


    def input_password(self,Password):
        return self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(Password)

    def click_submit(self):
        return self.driver.find_element_by_xpath(self.button_continue_xpath ).click()

    def click_todaydeals_status(self):
        return self.driver.find_element_by_xpath(self.button_todaysdeals_xpath).click()


    def click_electronic_status(self):
        return self.driver.find_element_by_xpath(self.button_electronics_xpath).click()


    def click_fashion_status(self):
        return self.driver.find_element_by_xpath(self.button_fashion_xpath).click()


    def click_kids(self):
        return self.driver.find_element_by_xpath(self.fashion_kids_xpath).click()

    def click_bags(self):
        return self.driver.find_element_by_xpath(self.button_bags_xpath).click()


    def click_all_nav(self):
        return self.driver.find_element_by_xpath(self.button_nav_all_xpath ).click()

    def click_men_fashion_status(self):
        return self.driver.find_element_by_xpath(self.dropdownmen_fashion_xpath).click()

    def click_tshirtpolos(self):
        return self.driver.find_element_by_xpath( self.dropdownmen_tshirtpolos_xpath).click()

    def click_dropdown(self):
        return self.driver.find_element_by_xpath(self.dropdown_xpath ).click()

    def click_size(self):
        return self.driver.find_element_by_xpath(self.size_xpath).click()

    def click_bestselling(self):
        return self.driver.find_element_by_xpath(self.dropdown_bestselling_xpath).click()

    def click_price_status(self):
        return self.driver.find_element_by_xpath(self.button_price_xpath).click()

    def click_inputfield(self,Shirt):
        return self.driver.find_element_by_xpath(self.input_field_xpath).send_keys(Shirt)

    def click_searchbutton(self):
        return self.driver.find_element_by_xpath(self.button_search_xpath).click()


    def click_checkbox(self):
        return self.driver.find_element_by_xpath(self.checkbox_xpath).click()

    def click_right_sidebar(self):
        return self.driver.find_element_by_xpath(self.button_sidebar_xpath).click()

    def click_topbrands_image(self):
        return self.driver.find_element_by_xpath(self.image_topbrands_click_xpath).click()

    def click_location_status(self):
        return self.driver.find_element_by_xpath(self.button_location_xpath).click()

    def input_pincode_status(self,Pincode):
        return self.driver.find_element_by_xpath(self.input_pincode_xpath).send_keys(Pincode)

    def click_apply(self):
        return self.driver.find_element_by_xpath(self.button_apply_xpath).click()

    def click_fashion1(self):
        return self.driver.find_element_by_xpath(self.btton_fashion1_xpath).click()

    def click_salesdeal_status(self):
        return self.driver.find_element_by_xpath(self.salesanddeals_xpath).click()

    def click_shopnow(self):
        return self.driver.find_element_by_xpath(self.shop_image_xpath).click()

    def click_sell(self):
        return self.driver.find_element_by_xpath(  self.sell_xpath).click()
    def click_startselling(self):
        return self.driver.find_element_by_xpath( self.button_selling_xpath).click()

    def click_computer(self):
        return self.driver.find_element_by_xpath(self.button_computer_xpath ).click()

    def click_mouseimage(self):
        return self.driver.find_element_by_xpath(self.image_mouse_xpath).click()

    def click_bestseller(self):
        return self.driver.find_element_by_xpath(self.button_bestseller_xpath ).click()

    def click_productimage(self):
        return self.driver.find_element_by_xpath(self.product_image_xpath).click()

    def click_share1(self):
        return self.driver.find_element_by_xpath(self.share_image_xpath).click()

    def click_sharetoemail(self):
        return self.driver.find_element_by_xpath( self.sharebyemail_xpath).click()

    def click_reviewrating(self):
        return self.driver.find_element_by_xpath(self.review_rating_xpath).click()

    def click_writereview(self):
        return self.driver.find_element_by_xpath(self.buttonwrite_review_xpath).click()

    def click_checkbox1(self):
        return self.driver.find_element_by_xpath(self.checkbox1_button_xpath).click()


    def click_checkbox2(self):
        return self.driver.find_element_by_xpath(self.checkbox2_button_xpath).click()

    def click_productimage1(self):
        return self.driver.find_element_by_xpath(self.productimage_xpath).click()

    def click_buybutton(self):
        return self.driver.find_element_by_xpath(self.button_buy_xpath).click()

    def pricemsg(self):
        return self.driver.find_element_by_xpath(self.price_xpath)









