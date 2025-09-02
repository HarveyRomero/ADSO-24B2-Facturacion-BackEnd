from flask import Flask
from flask_controller import FlaskControllerRegister
from src.models import Base, engine
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

register_controllers = FlaskControllerRegister(app)
register_controllers.register_package('src.controllers')

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)



