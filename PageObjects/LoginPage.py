class Login:
    def __init__(self,driver):
        self.driver = driver
        self.textbox_username_xpath = "//input[@id='ap_email']"
        self.textbox_password_xpath = "//input[@id='ap_password']"
        self.button_login_xpath = "//input[@id='signInSubmit']"
        # self.text_invalidmsg_xpath = "//div[@role='alert']"
        self.input_search2_xpath = "//input[@id='twotabsearchtextbox']"
        self.search_button_xpath = "//input[@id='nav-search-submit-button']"
        self.continue_button_xpath = "//input[@id='continue']"






    def input_username(self,Username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(Username)

    def input_password(self,Password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(Password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    #
    # def invalid_msg(self):
    #     return self.driver.find_element_by_xpath(self.text_invalidmsg_xpath).text

    def click_inputsearch2(self,Inputfield):
        return self.driver.find_element_by_xpath(self.input_search2_xpath).send_keys(Inputfield)


    def click_searchbutton(self):
        return self.driver.find_element_by_xpath(self.search_button_xpath).click()

    def click_continue(self):
        return self.driver.find_element_by_xpath(self.continue_button_xpath).click()

