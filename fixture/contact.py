class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.firstname)
        self.type("middlename", contact.middlename)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("title", contact.title)
        self.type("company", contact.company)
        self.type("address", contact.address)
        self.type("home", contact.phone_home)
        self.type("mobile", contact.phone_mobile)
        self.type("work", contact.phone_work)
        self.type("email", contact.email)


    def type(self, field_firstname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/group.php")

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@type='button' and @value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.return_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_list()
        # open modification form
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        # fill form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_contact_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()