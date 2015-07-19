# -*- coding: utf-8 -*-
def test_signup_new_account(app):
    assert app.soap.can_login('administrator', 'root')

