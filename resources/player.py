from flask_restful import Resource, reqparse
from models.player import PlayerModel


class Players(Resource):
    def get(self):
        return {'players': [player.json() for player in PlayerModel.query.all()]}


class Player(Resource):
    #definindo construtor é usado quando chama o parseargs
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank")
    argumentos.add_argument('kd', type=float, required=True, help="The field 'kd' cannot be left blank")
    argumentos.add_argument('last_played_map', type=str)
    argumentos.add_argument('last_match_kills', type=str)

    def get(self, id_player):
        player = PlayerModel.get_player(id_player)
        if player:
            return player.json()
        return{'message': 'Player not found.'}, 404

    def post(self, id_player):
        if PlayerModel.get_player(id_player):
            return {"message": "Player id '{}' already exists."\
            .format(id_player)}, 400#bad request
        #traz os argumentos do corpo da requisição
        dados = Player.argumentos.parse_args()
        #isso é um objeto python
        player = PlayerModel(id_player, **dados)
        try:
            player.save_player()
        except:
            return {'message': 'An internal error ocurred trying to save player.'}, 500 #internal server error
        #faz o parse do objeto para formato json
        return player.json()

    def put(self, id_player):   
        dados = Player.argumentos.parse_args()
        player_found = PlayerModel.get_player(id_player)
        if player_found:
            player_found.update_player(**dados)
            player_found.save_player()
            return player_found.json(), 200 #ok
        player = PlayerModel(id_player, **dados)
        try:
            player.save_player()
        except:
            return {'message': 'An internal error ocurred trying to save player.'}, 500 #internal server error
        return player.json(), 201 #created

    def delete(self, id_player):
        player_found = PlayerModel.get_player(id_player)
        if player_found:
            try:
                player_found.delete_player()
            except:
                return {'message': 'An internal error ocurred trying to save player.'}, 500 #internal server error
            return {'message': 'Player deleted'}
        return {'message': 'Player not found'}
