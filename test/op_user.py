#! /usr/bin/env python
# coding: utf-8

from ldap_user import LDAPConfig

__author__ = '鹛桑够'

LDAPConfig.create("ldap.conf", admin_user="root", admin_password="geneac2018")
l_user = LDAPConfig.load("ldap.conf")
d_r = l_user.delete_user("puser")
print(d_r)
l_user.add_user("puser")
l_user.set_password("puser", "12345678")
e_r = l_user.expire_user("puser")
print(e_r)
l_user.unlock_user("puser")