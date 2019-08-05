'''
비밀번호 변경 모듈
'''

from flask import Flask, request, make_response
import os

def pw_edit():
    '''
    :parameter: pw, pw_check
    :return: status code
    200 - 비밀번호 변경 완료
    410 - 비밀번호와 비밀번호 확인 값이 다름
    411 - 로그인 상태 아님
    '''

    data = request.form

    pw = data['pw']
    pw_check = data['pw_check']

    if 'user' not in request.cookies:
        return 'login first!', 411

    if pw != pw_check:
        return 'pw and pw_check are different', 410

    user_id = request.cookies.get('user')

    with open('data/UserLog/'+user_id, 'w') as f:
        f.write(pw)

    return 'pw_edit complete', 200