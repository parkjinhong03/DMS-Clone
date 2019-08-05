'''
로그인 모듈
'''

from flask import Flask, request, make_response
import os

def login():
    '''
    :parameter: id, pw
    :return: status code
    200 - 로그인 성공
    410 - 아이디 입력 오류
    411 - 비밀번호 입력 오류
    '''
    data = request.form

    id = data['id']
    pw = data['pw']

    if os.path.exists('data/UserLog/'+id) == False:
        return 'wrong id', 410

    with open('data/UserLog/'+id) as f:
        if pw == f.readline():
            resp = make_response('complete')
            resp.set_cookie('user', id)
            return resp, 200

        else:
            return 'wrong password', 411