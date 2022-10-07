from PageObjects.LoginPage import Login
from PageObjects.Dashboard import dashboard
from selenium.webdriver import ActionChains
from PageObjects.EmployementStatusPage import EmpStatus
from Utilities.Logger import logclass
import configparser
config = configparser.ConfigParser()
config.read("Utilities/.properties")

import pytest
@pytest.mark.usefixtures("setup")
class TestAddButton(logclass):
    def test_001(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard(self.driver)
        es = EmpStatus(self.driver)
        log.info("Test Case 001")
        log.info("test started")
        lg.input_username(config.get("credential","correct_username"))
        lg.input_password(config.get("credential","correct_password"))
        lg.click_login()
        log.info("login successfully")
        ActionChains(self.driver).context_click(db.click_admin())
        log.info("click in admin")
        ActionChains(self.driver).context_click(db.click_qualification())
        log.info("Click in qualification")
        # ActionChains(self.driver).context_click(db.click_emp_status())
        # log.info("click in employment status")
        # es.click_addbutton()
        # log.info("add button")
        # es.input_newrequried("SeleniumTest")
        # log.info("input on blank space")
        # es.click_savebutton()
        # log.info("save new contains")
