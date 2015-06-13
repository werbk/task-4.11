# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class forsevascript(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_forsevascript(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("admin")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        ActionChains(wd).double_click(wd.find_element_by_xpath("//table[@id='maintable']//td[.='felixfelixfelixfelix']")).perform()
        ActionChains(wd).double_click(wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[3]")).perform()
        ActionChains(wd).double_click(wd.find_element_by_xpath("//table[@id='maintable']//td[.='felixfelixfelixfelix']")).perform()
        ActionChains(wd).double_click(wd.find_element_by_xpath("//table[@id='maintable']//td[.='felixfelixfelixfelix']")).perform()
        wd.find_element_by_xpath("//table[@id='maintable']//td[.='felixfelixfelixfelix']").click()
        ActionChains(wd).double_click(wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[3]")).perform()
        if not wd.find_element_by_id("107").is_selected():
            wd.find_element_by_id("107").click()
        ActionChains(wd).double_click(wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[6]")).perform()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
