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
class Testflipkartpage(logclass):
    def test_01(self):
        log = self.getthelogs()
        db = dashboard(self.driver)
        lg = Login(self.driver)
        lg.input_email(config.get("credential", "Incorrect_email"))
        log.info("Enter username")
        lg.input_password(config.get("credential", "Incorrect_password"))
        log.info("Enter password")
        lg.click_login()
        log.info("Clicked login")
        db.flipkart_logo()
        db.explore_plus()
