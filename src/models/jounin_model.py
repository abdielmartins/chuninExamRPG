from .ninja_model import Ninja


class Jounin(Ninja):
    def __init__(self, name: str, clan: str, village: str, proficiency: dict) -> None:
        super().__init__(name, clan, village)
        self.ninja_level = "Jounin"
        self.proficiency = proficiency
        self.is_in_mission = False

    def list_best_proficiency(self) -> str:
        best_proficiency = max(self.proficiency, key=lambda key: self.proficiency[key])
        return f"{self.name} demonstra maior proficiência em {best_proficiency}"

    def start_mission(self) -> str:
        if self.is_in_mission:
            return f"O ninja {self.name} {self.clan} já está em uma missão"
        else:
            self.is_in_mission = True
            return f"O ninja {self.name} {self.clan} saiu em missão"

    def return_from_mission(self) -> str:
        if self.is_in_mission:
            self.is_in_mission = False
            return f"O ninja {self.name} {self.clan} retornou em segurança da missão"
        else:
            return f"O ninja {self.name} {self.clan} não está em nenhuma missão no momento"