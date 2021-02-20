from sql_alchemy import banco

class UserModel(banco.Model):
    __tablename__ = 'usuarios'
    #o sql alchemy irá criar automaticamente o id no banco
    user_id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(40))#limita a 40 characters
    senha = banco.Column(banco.String(40))#limita a 40 characters

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return{
            'user_id': self.user_id,
            'login': self.login
        }

    @classmethod
    def find_user(cls, user_id):
        #select * from players where id_player = $id_player limit 1
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None
    
    def save_user(self):
        banco.session.add(self)
        banco.session.commit()
        #salvou no banco de dados o objeto

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()
