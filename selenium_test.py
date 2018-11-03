from selenium import webdriver

def test_home():
    browser = webdriver.Chrome()

    browser.get("http://162.246.157.103:8000/")
    name = browser.find_element_by_xpath("//*[@id='name']")
    about = browser.find_element_by_xpath("//*[@id='about']")
    education = browser.find_element_by_xpath("//*[@id='education']")
    skills = browser.find_element_by_xpath("//*[@id='skills']")
    work = browser.find_element_by_xpath("//*[@id='work']")
    contact = browser.find_element_by_xpath("//*[@id='contact']")

    assert name!= None
    assert about != None
    assert education != None
    assert skills != None
    assert work != None
    assert contact != None



