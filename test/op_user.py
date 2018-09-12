#! /usr/bin/env python
# coding: utf-8

from ldap_user import LDAPConfig

__author__ = '鹛桑够'

LDAPConfig.create("ldap.conf", admin_user="root", admin_password="geneac2018")
l_user = LDAPConfig.load("ldap.conf")
t_user = "zh_test3"
d_r = l_user.delete_user(t_user)
print(d_r)
l_user.add_user(t_user)
l_user.set_password(t_user, "12345678")
e_r = l_user.expire_user(t_user)
print(e_r)
l_user.unlock_user(t_user)
# l_user.ldap_com.bind_s("cn=zh_test3,ou=People,dc=gene,dc=ac", "12345678")
# l_user.ldap_com.bind_s("cn=zh_test3,ou=People,dc=gene,dc=ac", "123457")
# l_user.ldap_com.bind_s("cn=zh_test3,ou=People,dc=gene,dc=ac", "123456")
print l_user.exist("suser", "pwdPolicySubentry", "pwdAccountLockedTime", "pwdFailureTime", "pwdHistory", "pwdReset")
# l_user.set_password("suser", "12345678")
# l_user.unlock_user("suser")
print l_user.login2("suser", "12345678")