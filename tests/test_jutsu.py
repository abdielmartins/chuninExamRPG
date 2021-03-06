from src.models.jutsu_model import Jutsu


def test_jutsu():
    rasengan = Jutsu("Rasengan", "Vento", "a", 20, -15)
    chidori = Jutsu("Chidori", "Relâmpago", "z", 5, 30)

    assert rasengan.__dict__ == {
        "chakra_spend": 100,
        "jutsu_damage": 20,
        "jutsu_level": "A",
        "jutsu_name": "Rasengan",
        "jutsu_type": "Vento",
    }

    assert chidori.__dict__ == {
        "chakra_spend": 30,
        "jutsu_damage": 5,
        "jutsu_level": "Unranked",
        "jutsu_name": "Chidori",
        "jutsu_type": "Relâmpago",
    }