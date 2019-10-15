# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_contact_page(wd)
        self.create_contact(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Andrey")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Vladimirovich")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Tracevskij")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Zverun")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("QA")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Adani")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Novodvorskij s/s 116")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("80172234522")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("8044777777")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("2222222")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("test@ya.ru")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("3")
        wd.find_element_by_xpath("//option[@value='3']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("December")
        wd.find_element_by_xpath("//option[@value='December']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1987")
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
