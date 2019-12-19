from model.contact import Contact


def test_modify_contact_firstname(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(firstname = "Vasilii"))
    app.session.logout()


def test_modify_contact_middlename(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(middlename = "Vasilievich"))
    app.session.logout()
    
    
def test_modify_contact_lastname(app):
    app.session.login(username = "admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="Vasilkov"))
    app.session.logout()
    
    
def test_modify_contact_nickname(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(nickname = "ZverOK"))
    app.session.logout()
    

def test_modify_contact_title(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(title = "Automated"))
    app.session.logout()
    
    
def test_modify_contact_company(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(company = "Nike"))
    app.session.logout()


def test_modify_contact_address(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(address = "M.Tanka 34/1"))
    app.session.logout()


def test_modify_contact_phone_home(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(phone_home = "80171111111"))
    app.session.logout()
    
    
def test_modify_contact_phone_mobile(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(phone_mobile = "80442222222"))
    app.session.logout()
    

def test_modify_contact_phone_work(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(phone_work = "80443333333"))
    app.session.logout()
    
    
def test_modify_contact_email(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first_contact(Contact(email = "tester@ya.ru"))
    app.session.logout()
