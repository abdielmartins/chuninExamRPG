from src.models.ninja_model import Ninja
from src.models.jutsu_model import Jutsu


def test_ninja():
    naruto = Ninja("Naruto", "Uzumaki", "Konoha")

    assert naruto.__dict__ == {
        "name": "Naruto",
        "ninja_level": "Unranked",
        "clan": "Uzumaki",
        "village": "Konoha",
        "jutsu_list": [],
        "health_pool": 100,
        "chakra_pool": 100,
        "concious": True,
    }

    rasengan = Jutsu("Rasengan", "Vento", "a", 20, -15)

    assert naruto.learn_jutsu(rasengan) == "O ninja Naruto acabou de aprender um novo jutsu: Rasengan"

    sasuke = Ninja("Sasuke", "Uchiha", "Konoha")

    assert naruto.cast_jutsu(rasengan, sasuke) == True
    print(naruto.__dict__)
    assert naruto.cast_jutsu(rasengan, sasuke) == False