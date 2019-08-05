'''
회원가입 모듈
'''

from flask import Flask, request
import os


def signup():
    '''
    :parameter: id, pw, pw_check
    :return: status_code
    200 - 완료
    410 - 이미 존재하는 아이디
    411 - 비밀번호와 비밀번호 확인 값이 다름
    '''
    data = request.form

    id = data['id']
    pw = data['pw']
    pw_check = data['pw_check']

    if os.path.exists('data/UserLog/'+id):
        return '아이디가 이미 존재합니다.', 410

    if pw != pw_check:
        return '비밀번호와 비밀번호 확인이 서로 같지 않습니다.', 411

    with open('data/UserLog/'+id, 'w') as f:
        f.write(pw)

    return '회원가입 성공!', 200
