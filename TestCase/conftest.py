
import configparser
config = configparser.ConfigParser()
config.read("Utilities/.properties")
import pytest
@pytest.fixture
def setup(request):
    from selenium import webdriver
    import time
    request.cls.driver = webdriver.Chrome(executable_path="Driver/chromedriver.exe")
    request.cls.driver.get(config.get("Url2","base2_url"))

    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(10)
    time.sleep(5)
    yield
    


