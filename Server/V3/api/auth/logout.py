'''
로그아웃 모듈
'''

from Server.V2.api.cookie_decorator import login_required
from flask import make_response


@login_required
def logout():
    '''
    :parameter: X
    :return: status code
    200 - 로그아웃 성공
    410 - 로그인 상태가 아님
    '''

    resp = make_response('로그아웃 완료!')
    resp.set_cookie('user', '', expires=0)

    return resp, 200


