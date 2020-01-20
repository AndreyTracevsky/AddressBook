from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname = "Vasilii"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_middlename(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename = "Vasilievich"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_lastname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="Vasilkov"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_nickname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(nickname = "ZverOK"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_title(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(title = "Automated"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_company(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(company = "Nike"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_address(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(address = "M.Tanka 34/1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_phone_home(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(phone_home = "80171111111"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_phone_mobile(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(phone_mobile = "80442222222"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_phone_work(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(phone_work = "80443333333"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_email(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(email = "tester@ya.ru"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
