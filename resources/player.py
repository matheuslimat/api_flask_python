from flask_restful import Resource, reqparse
from models.player import PlayerModel


players_data = [
    {
        'id_player': '045678',
        'name': 'Migor',
        'kd': 1.25,
        'last_played_map': 'Verdansk', #Rebirth Island
        'last_match_kills': 4
    },
    {
        'id_player': '041679',
        'name': 'PanicoBRx7',
        'kd': 1.20,
        'last_played_map': 'Rebirth Island', #Rebirth Island
        'last_match_kills': 7
    }
]

class Players(Resource):
    def get(self):
        return players_data


class Player(Resource):
    #definindo construtor é usado quando chama o parseargs
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('name')
    argumentos.add_argument('kd')
    argumentos.add_argument('last_played_map')
    argumentos.add_argument('last_match_kills')

    def get(self, id_player):
        player = self.get_player(id_player)
        if player:
            return player
        return{'message': 'Player not found.'}, 404

    def post(self, id_player):
        if PlayerModel.get_player(id_player):
            return {"message": "Player id '{}' already exists."\
            .format(id_player)}, 400#bad request
        #traz os argumentos do corpo da requisição
        dados = Player.argumentos.parse_args()
        #isso é um objeto python
        player = PlayerModel(id_player, **dados)
        player.save_player()
        #faz o parse do objeto para formato json
        return player.json()

    def put(self, id_player):   
        dados = Player.argumentos.parse_args()
        new_player_objeto = PlayerModel(id_player, **dados)
        #isso é um parse pra json
        new_player = new_player_objeto.json()
        player = self.get_player(id_player)
        if player:
            player.update(new_player)
            return player, 200 #ok
        players_data.append(new_player)
        return new_player, 201 #created

    def delete(self, id_player):
        global players_data # referencia a variavel global
        players_data = [player for player in players_data if player['id_player'] != id_player]
        return {'message': 'Player deleted'}
