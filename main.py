from selenium import webdriver
from time import sleep
from secrets import account,pw,after_login_url, url

class OgameBot: 
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome('./chromedriver')
        self.username = username
        self.driver.get(url)
        self.driver.find_element_by_xpath('//a[contains(text(), "x")]').click()
        sleep(2)
        self.elem = self.driver.find_element_by_xpath('//div[@id="loginRegisterTabs"]/ul/li').click()
        self.driver.find_element_by_xpath('//input[@name="email"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(pw)
        sleep(3)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//span[contains(text(), "Play")]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//button[@type="button"]/span[contains(text(), "Play")]').click()    
        sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(after_login_url)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0] )
        sleep(5)

OgameBot(account,pw)


