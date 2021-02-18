from flask import Flask
from flask_restful import Api
from resources.player import Players, Player

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_database():
    banco.create_all()

api.add_resource(Players, '/players')
api.add_resource(Player, '/players/<string:id_player>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)