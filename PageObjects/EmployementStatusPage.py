class EmpStatus:
    def __init__(self,driver):
        self.driver = driver
        self.button_add_status_xpath = "//button[normalize-space()='Add']"
        self.inputfield_name_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
        self.button_save_xpath = "//button[@type='submit']"



    def click_addbutton(self):
        self.driver.find_element_by_xpath(self.button_add_status_xpath).click()

    def input_newrequried(self,Selenium6):
        self.driver.find_element_by_xpath(self.inputfield_name_xpath).send_keys(Selenium6)


    def click_savebutton(self):
        return self.driver.find_element_by_xpath(self.button_save_xpath).click()


