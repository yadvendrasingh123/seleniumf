
from selenium import webdriver
from selenium.webdriver.support import Select
driver=webdriver.Chrome(executable_path="C:\Program Files\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/from2/index.html?1537702596407")
element=driver.find_element_by_id("RESULT_RadioButton-7")
drp=Select(element)

#select by visible text
drp.select_by_visible_text('morning')

#select by index
drp.select_by_index(2) ##afternoon

#select by value
drp.select_by_value("Radio-2") ## evening

#count number of options
print(len(drp.options))

#capture all the options and print them as output

all_option=drp.options
for option in all_option:
    print(option.text)
