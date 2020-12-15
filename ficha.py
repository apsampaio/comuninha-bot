from tinydb import TinyDB, Query

db = TinyDB('/db/db.json')

class Ficha:
    def __init__(self, nome, HP):
        self.nome = nome
        self.HP = HP

    def health(self):
        print(f"A vida de {self.nome} é {self.HP}.")

    def reduce_hp(self, value):
        self.HP = self.HP - value
        print(f"A vida de {self.nome} foi reduzida para {self.HP}.")
        if self.HP <= 0:
            print(f"{self.nome} mamou!")