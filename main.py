from src.models.jutsu_model import Jutsu
from src.models.ninja_model import Ninja
from src.models.jounin_model import Jounin

if __name__ == "__main__":

    rasengan = Jutsu("Rasengan", "Vento", "a", 20, -15)

    naruto = Ninja("Naruto", "Uzumaki", "Konoha")
    res = naruto.learn_jutsu(rasengan)
    print(res)

    kakashi_proficiency = {"taijutsu": 7, "ninjutsu": 8, "genjutsu": 4}
    kakashi = Jounin("Kakashi", "Hatake", "Konoha", kakashi_proficiency)

    sasuke = Ninja("Sasuke", "Uchiha", "Konoha")
    res_cast = naruto.cast_jutsu(rasengan, sasuke)
    print(res_cast)

    print(sasuke.__dict__)
    print(naruto.__dict__)