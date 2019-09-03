from flask import Flask
from flask_restful import Api
from Server.V3.api.routing import user, music, stay, my_stay
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

api.add_resource(user, '/Auth/User')
api.add_resource(music, '/Service/Music')
api.add_resource(stay, '/Service/Stay')
api.add_resource(my_stay, '/Service/Stay/my')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 5000, debug= True)