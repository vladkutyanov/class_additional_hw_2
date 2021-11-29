import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):
    @property
    @abstractmethod
    def exp(self):
        pass

    @classmethod
    @abstractmethod
    def inc_exp(cls, exp_size):
        pass


class Pokemon(AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self.exp = self.exp()

    def to_str(self):
        return f'{self.name}/{self.poketype}'

    def exp(self):
        return 0

    def inc_exp(self, exp_size):
        self.exp += exp_size


class Digimon(AnimeMon):
    def __init__(self, name: str):
        self.name = name
        self.exp = self.exp()

    def exp(self):
        return 0

    def inc_exp(self, exp_size):
        self.exp += exp_size*8


def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == '__main__':
    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp)
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    train(bulbasaur)
    print(bulbasaur.exp)
