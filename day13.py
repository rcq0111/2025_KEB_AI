from pandas.core.indexes.multi import names_compat


class Pokemon:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print("walk..")
    def attack(self, target_Pokemon):
        print(f"{self.name} attack!!{target_Pokemon.name}")

class Pikachu(Pokemon):
    pass

class Agumon:
    def __init__(self, name):
        self.name = name

agumon = Agumon('아구몬')
pikachu = Pikachu('피카츄')
pikachu.attack(agumon)
