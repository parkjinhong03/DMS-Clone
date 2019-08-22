'''
회원가입 모듈
'''

from Server.V2.DB_func.connect import connect
from flask import Flask, request
import os
import pymysql


def signup():
    '''
    :parameter: id, pw, pw_check
        :return: status_code
    200 - 완료
    410 - 이미 존재하는 아이디
    411 - 비밀번호와 비밀번호 확인 값이 다름
    '''
    data = request.json

    id = data['id']
    pw = data['pw']
    pw_check = data['pw_check']

    cur, con = connect()

    sql = "create table UserLog("\
          "id bigint(20) unsigned NOT NULL AUTO_INCREMENT,"\
          "user_id text," \
          "user_pw text," \
          "PRIMARY KEY (id)" \
          ");"

    try:
        cur.execute(sql)

    except pymysql.err.InternalError:
        pass

    if pw != pw_check:
        return "pw != pw_check", 411

    sql = f'select EXISTS (select * from userlog where user_id="{id}") as success'

    cur.execute(sql)

    if cur.fetchone()[0] == 1:
        return '이미 존재하는 아이디 입니다.', 400

    sql = f'INSERT INTO UserLog (user_id, user_pw) VALUES("{id}", "{pw}")'
    cur.execute(sql)

    con.commit()
    con.close()

    return '회원가입 성공!', 200
