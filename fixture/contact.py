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
        self.change_contact_form_value("firstname", contact.firstname)
        self.change_contact_form_value("middlename", contact.middlename)
        self.change_contact_form_value("lastname", contact.lastname)
        self.change_contact_form_value("nickname", contact.nickname)
        self.change_contact_form_value("title", contact.title)
        self.change_contact_form_value("company", contact.company)
        self.change_contact_form_value("address", contact.address)
        self.change_contact_form_value("home", contact.phone_home)
        self.change_contact_form_value("mobile", contact.phone_mobile)
        self.change_contact_form_value("work", contact.phone_work)
        self.change_contact_form_value("email", contact.email)

    def change_contact_form_value(self, field_firstname, text):
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