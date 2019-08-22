from flask import request
from functools import wraps


def login_required(func):
    @wraps(func)
    def index():
        if 'user' not in request.cookies:
            return "로그인을 먼저 해주세요", 403
        return func()

    return index