#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib

db = {}
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'sjd') #加盐

register('michael', '123456')
register('bob', 'abc999')
register('alice', 'alice2008')
print(db)

def login(username,password):
    password = password + username + 'sjd'
    if username in db:
        if db[username] == get_md5(password):
            return True
    return False


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')