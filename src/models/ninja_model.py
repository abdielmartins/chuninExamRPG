from __future__ import annotations
from .jutsu_model import Jutsu


class Ninja:
    @staticmethod
    def check_health(ninja_to_check: Ninja) -> bool:
        if ninja_to_check.health_pool < 0:
            ninja_to_check.health_pool = 0
            ninja_to_check.concious = False

        return ninja_to_check.concious

    def __init__(self, name: str, clan: str, village: str, ninja_level: str = "Unranked") -> None:
        self.name = name
        self.clan = clan
        self.village = village
        self.ninja_level = ninja_level
        self.jutsu_list = []
        self.health_pool = 100
        self.chakra_pool = 100
        self.concious = True

    def learn_jutsu(self, jutsu: Jutsu) -> str:
        self.jutsu_list.append(jutsu)
        return f"O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {jutsu.jutsu_name}"

    def cast_jutsu(self, jutsu: Jutsu, adversary: Ninja) -> bool:
        if not Ninja.check_health(adversary):
            return False
        if jutsu in self.jutsu_list and jutsu.chakra_spend <= self.chakra_pool and self.chakra_pool != 0:
            self.chakra_pool -= jutsu.chakra_spend
            adversary.health_pool -= jutsu.jutsu_damage
            return True
        return False
