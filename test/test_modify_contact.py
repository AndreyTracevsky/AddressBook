from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname = "Vasilii"))


def test_modify_contact_middlename(app):
    app.contact.modify_first_contact(Contact(middlename = "Vasilievich"))
    
    
def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Vasilkov"))
    
    
def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(Contact(nickname = "ZverOK"))
    

def test_modify_contact_title(app):
    app.contact.modify_first_contact(Contact(title = "Automated"))
    
    
def test_modify_contact_company(app):
    app.contact.modify_first_contact(Contact(company = "Nike"))


def test_modify_contact_address(app):
    app.contact.modify_first_contact(Contact(address = "M.Tanka 34/1"))


def test_modify_contact_phone_home(app):
    app.contact.modify_first_contact(Contact(phone_home = "80171111111"))
    
    
def test_modify_contact_phone_mobile(app):
    app.contact.modify_first_contact(Contact(phone_mobile = "80442222222"))
    

def test_modify_contact_phone_work(app):
    app.contact.modify_first_contact(Contact(phone_work = "80443333333"))
    
    
def test_modify_contact_email(app):
    app.contact.modify_first_contact(Contact(email = "tester@ya.ru"))
