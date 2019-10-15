# -*- coding: utf-8 -*-
from fixture.appication import Application
import pytest
from model.contact import Contact

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname = "Andrey", midlename = "Vladimirovich", lastname = "Tracevskij", nickname = "Zverun",
                        title = "QA", company = "Adani", address = "Novodvorskij s/s 116", phone_home = "80172234522", phone_mobile = "8044777777", phone_work = "2222222", email = "test@ya.ru"))
    app.logout()


def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname = "", midlename = "", lastname = "", nickname = "", title = "", company = "", address = "", phone_home = "", phone_mobile = "", phone_work = "", email = ""))
    app.logout()