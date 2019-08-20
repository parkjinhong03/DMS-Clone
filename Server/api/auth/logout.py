'''
로그아웃 모듈
'''

from flask import Flask, request, make_response
import os

def logout():
    '''
    :parameter: X
    :return: status code
    200 - 로그아웃 성공
    410 - 로그인 상태가 아님
    '''

    if 'user' not in request.cookies:
        return '로그인을 먼저 해주세요.', 410

    resp = make_response('로그아웃 완료!')
    resp.set_cookie('user', '', expires=0)

    return resp, 200


