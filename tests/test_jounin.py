from src.models.jounin_model import Jounin


def test_jounin():
    kakashi_proficiency = {"taijutsu": 7, "ninjutsu": 8, "genjutsu": 4}
    kakashi = Jounin("Kakashi", "Hatake", "Konoha", kakashi_proficiency)

    assert kakashi.__dict__ == {
        "chakra_pool": 100,
        "health_pool": 100,
        "clan": "Hatake",
        "concious": True,
        "is_in_mission": False,
        "jutsu_list": [],
        "name": "Kakashi",
        "ninja_level": "Jounin",
        "proficiency": {"genjutsu": 4, "ninjutsu": 8, "taijutsu": 7},
        "village": "Konoha",
    }

    assert kakashi.list_best_proficiency() == "Kakashi demonstra maior proficiência em ninjutsu"
    assert kakashi.start_mission() == "O ninja Kakashi Hatake saiu em missão"
    assert kakashi.start_mission() == "O ninja Kakashi Hatake já está em uma missão"
    assert kakashi.return_from_mission() == "O ninja Kakashi Hatake retornou em segurança da missão"
    assert kakashi.return_from_mission() == "O ninja Kakashi Hatake não está em nenhuma missão no momento"