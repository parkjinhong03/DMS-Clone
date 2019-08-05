from flask import Flask

app = Flask(__name__)

from Server.app.api.auth.signup import signup
from Server.app.api.auth.login import login
from Server.app.api.auth.logout import logout
from Server.app.api.auth.pw_edit import pw_edit

app.add_url_rule('/auth/signup',  'signup', signup, methods=['POST'])
app.add_url_rule('/auth/login', 'login', login, methods=['POST'])
app.add_url_rule('/auth/logout', 'logout', logout, methods=['POST'])
app.add_url_rule('/auth/pw_edit', 'pw_edit', pw_edit, methods=['POST'])

if __name__ == '__main__':
    app.run(host= '172.30.1.59', port= 5000, debug= True)