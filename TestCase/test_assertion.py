import unittest


from selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="D:\\new webdriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleOfWebPage = driver.title
        self.assertEqual("Google", titleOfWebPage,"webpage title is not same")


if __name__ == "__main__":
    unittest.main()

