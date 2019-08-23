'''
기상 음악 취소 모듈
'''

from Server.V2.DB_func.connect import connect
from Server.V2.DB_func.service.exist_music import exist_music
from Server.V2.api.cookie_decorator import login_required
from flask import Flask, request, make_response
import os


@login_required
def music_delete():
    '''
    :parameter: X
    :return: status code
    403 로그인 상태 아님
    410 전에 신청해둔 음악이 없음.
    200 기상 음악 신청 취소 완료
    '''

    my_name = request.cookies.get('user')

    con, cur = connect()

    if exist_music(con, cur, my_name) == False:
        return "전에 신청해둔 음악이 없습니다.", 410

    sql = f'DELETE FROM music WHERE user_id="{my_name}"'

    cur.execute(sql)

    con.commit()
    con.close()

    return "기상 음악 취소 완료!", 200