from PageObjects.LoginPage import Login
from PageObjects.Dashboard import dashboard
from selenium.webdriver import ActionChains
from PageObjects.EmployementStatusPage import EmpStatus
import pytest
from Utilities.Logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/.properties")

@pytest.mark.usefixtures("setup")
class TestLogin(logclass):
    def test_001(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard(self.driver)
        log.info("Test Case 001")
        log.info("test case starting")
        lg.input_username(config.get("credential", "correct_username"))
        log.info("Enter username")
        lg.input_password(config.get("credential", "correct_password"))
        log.info("Enter password")
        lg.click_login()
        log.info("Clicked login")
        if 'Reports' in db.reports_msg():
            assert True
            log.info("Test is pass")
        else:
            self.driver.save_screenshot('Screenshots\\TestLogin_001.png')
            log.critical("Test is fail")
            assert False

    def test_002(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("Test case 002")
        log.info("Second test start")
        lg.input_username(config.get("credential", "Incorrect_username"))
        log.info("Incorrect username")
        lg.input_password(config.get("credential", "correct_password"))
        log.info("Password are correct")
        lg.click_login()
        log.info("Clicked login")

        if 'Invalid credentials' in lg.invalid_msg():
            assert True
            log.info("its pass")
        else:
            self.driver.save_screenshot('Screenshots\\TestLogin_001.png')
            log.critical("its fail")
            assert False

    def test_003(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        log.info("Test case 003")
        log.info("Third case start")
        lg.input_username(config.get("credential", "correct_username"))
        log.info("correct username")
        lg.input_password(config.get("credential", "Incorrect_password"))
        log.info("Password are Incorrect")
        lg.click_login()
        log.info("Clicked login")

        if 'Invalid credentials' in lg.invalid_msg():
            assert True
            log.info("its pass")
        else:
            self.driver.save_screenshot('Screenshots\\TestLogin_001.png')
            log.critical("its fail")
            assert False


    def test_004(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard(self.driver)
        es = EmpStatus(self.driver)
        log.info("Test Case 001")
        log.info("test started")
        lg.input_username(config.get("credential", "correct_username"))
        lg.input_password(config.get("credential", "correct_password"))
        lg.click_login()
        log.info("login successfully")
        ActionChains(self.driver).context_click(db.click_admin())
        log.info("click in admin")
        ActionChains(self.driver).context_click(db.click_job())
        log.info("Click in job")
        ActionChains(self.driver).context_click(db.click_emp_status())
        log.info("click in employment status")
        es.click_addbutton()
        log.info("add button")
        es.input_newrequried("Selenium6")
        log.info("input on blank space")
        es.click_savebutton()
        log.info("new employee")
