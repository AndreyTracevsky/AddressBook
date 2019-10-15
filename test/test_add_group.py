# -*- coding: utf-8 -*-
from model.group import Group
from fixture.appication import Application
import pytest



@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.create_group(Group(name = "QA1", header = "Testers", footer = "ORPO"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username = "admin", password = "secret")
    app.create_group(Group(name = "", header = "", footer = ""))
    app.session.logout()

