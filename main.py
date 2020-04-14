from selenium import webdriver
from time import sleep
from secrets import account,pw,after_login_url, url

class OgameBot(): 
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get(url)
        self.driver.find_element_by_xpath('//a[contains(text(), "x")]').click()
        sleep(2)
        self.elem = self.driver.find_element_by_xpath('//div[@id="loginRegisterTabs"]/ul/li').click()
        self.driver.find_element_by_xpath('//input[@name="email"]').send_keys(account)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(pw)
        sleep(3)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//span[contains(text(), "Play")]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//button[@type="button"]/span[contains(text(), "Play")]').click()    
        sleep(4)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.metal = self.driver.find_element_by_id('resources_metal').get_attribute('innerHTML')
        self.crystal = self.driver.find_element_by_id('resources_crystal').get_attribute('innerHTML')
        self.deuterium = self.driver.find_element_by_id('resources_deuterium').get_attribute('innerHTML')
        self.energy = self.driver.find_element_by_id('resources_energy').get_attribute('innerHTML')
        
        
        
    def go_to_resource(self):
        self.driver.find_element_by_xpath('//span[contains(text(),"Recursos")]').click()
        print(self.metal)
        print(self.crystal)
        print(self.deuterium)
        print(self.energy)
        
                
mybot = OgameBot()


