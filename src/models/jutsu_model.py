class Jutsu:
    def __init__(
        self, jutsu_name: str, jutsu_element: str, jutsu_class: str, jutsu_damage: int, chakra_spend: int
    ) -> None:
        self.jutsu_name = jutsu_name
        self.jutsu_element = jutsu_element
        self.justu_class = jutsu_class
        self.jutsu_damage = jutsu_damage
        self.chakra_spend = chakra_spend if chakra_spend > 0 else 100


class NormalJutsu(Jutsu):
    jutsu_type = "Normal"

    def __init__(self, jutsu_name, jutsu_element, jutsu_class, jutsu_damage, chakra_spend):
        super().__init__(jutsu_name, jutsu_element, jutsu_class, jutsu_damage, chakra_spend, jutsu_type=self.jutsu_type)


class EspecialJutsu(Jutsu):
    jutsu_type = "Especial"

    def __init__(self, jutsu_name, jutsu_element, jutsu_class, jutsu_damage, chakra_spend):
        super().__init__(jutsu_name, jutsu_element, jutsu_class, jutsu_damage, chakra_spend, jutsu_type=self.jutsu_type)


class BuffJutsu(Jutsu):
    jutsu_type = "Buff"

    def __init__(self, jutsu_name, jutsu_element, jutsu_class, jutsu_damage, chakra_spend):
        super().__init__(jutsu_name, jutsu_element, jutsu_class, jutsu_damage, chakra_spend, jutsu_type=self.jutsu_type)


class DebuffJutsu(Jutsu):
    jutsu_type = "Debuff"

    def __init__(self, jutsu_name, jutsu_element, jutsu_class, jutsu_damage, chakra_spend):
        super().__init__(jutsu_name, jutsu_element, jutsu_class, jutsu_damage, chakra_spend, jutsu_type=self.jutsu_type)
