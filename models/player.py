from sql_alchemy import banco

class PlayerModel(banco.Model):
    __tablename__ = 'players'
    id_player = banco.Column(banco.String, primary_key=True)
    name = banco.Column(banco.String(15))#limita a 15 characters
    kd = banco.Column(banco.Float(precision=2))#duas cadas depois da vircula
    last_played_map = banco.Column(banco.String)
    last_match_kills = banco.Column(banco.Integer)

    def __init__(self, id_player, name, kd, last_played_map, last_match_kills):
        self.id_player = id_player
        self.name = name
        self.kd = kd
        self.last_played_map = last_played_map
        self.last_match_kills = last_match_kills

    def json(self):
        return{
            'id_player': self.id_player,
            'name': self.name,
            'kd': self.kd,
            'last_played_map': self.last_played_map,
            'last_match_kills': self.last_match_kills
        }

    def get_player(self, id_player):
        for player in players_data:
            if player['id_player'] == id_player:
                return player
        return None
        