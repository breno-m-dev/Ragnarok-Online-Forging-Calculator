

# According to ragnarok online wiki, the following is the formula to
# calculate the forging chance of a weapon

# Success Rate = [
#   50 + (Anvil) + (Weaponry Research Level)
#  + (Oridecon Research Level if Weapon Lv3) + (JobLv × 0.2)
#  + (DEX × 0.1) + (LUK × 0.1) - (Weapon Level) - (Element Stone)
#  - (Star Crumbs)
# ]%

class Anvil:
    NORMAL = 0
    ORIDECON = 3
    GOLDEN = 5
    EMPERIUM = 10
    @staticmethod
    def anvil_bonus(anvil: str) -> int:
        if anvil == "anvil":
             return Anvil.NORMAL
        elif anvil == "golden anvil":
             return Anvil.GOLDEN
        elif anvil == "oridecon anvil":
             return Anvil.ORIDECON
        elif anvil == "emperium anvil":
             return Anvil.EMPERIUM
        else:
             return Anvil.NORMAL
        
class Forge:


    def __init__(self, *,
            job_lvl: int,
            anvil: str,
            weaponry_lvl: int,
            oridec_research: int,
            smith_skills: int,
            dex: int, 
            luk: int 
            ):
        anvil.lower()
        self.bonus = Anvil.anvil_bonus(anvil=anvil)
        self.job_lvl = job_lvl
        self.weaponry_lvl = weaponry_lvl
        self.oridec_research = oridec_research
        self.smith_skills = smith_skills
        self.dex = dex
        self.luk = luk

    def get_forge_chance(self, weapon_lvl: int, n_element: int, n_star: int):
        if(
            self.validate_stone_number(n_element=n_element, n_star=n_star)
            and self.validate_weapon(weapon_lvl)
        ):
            chance = (
                50 + (self.bonus) + (self.weaponry_lvl) 
                + (self.oridec_research) + (self.job_lvl * 0.2) 
                + (self.dex * 0.1) + (self.luk * 0.1) - (weapon_lvl) 
                - (n_element * 20) - (n_star * 15)
            )
            return chance
        else:
             return

    def __private_validate_number(
            self, inferior_limit: int, superior_limit: int,
            test_value: int
            ):
        if (
            test_value > superior_limit
            or test_value < inferior_limit
            or not isinstance(test_value, int)
        ):
            print(f"Value should be an integer from {inferior_limit} to {superior_limit} ")
            return False
        else:
            return True
        
    def validate_weapon(self, weapon_lvl: int):
        MAX_WEAPON_LVL = 4
        MIN_WEAPON_LVL = 1
        if ( self.__private_validate_number(
            MIN_WEAPON_LVL, MAX_WEAPON_LVL, weapon_lvl
            )
        ):
             return True
        else:
            print("Invalid weapon level")
            return False


 
    def validate_stone_number(self, n_element: int, n_star: int):
        MAX_ELEMENT = 1
        MIN_ELEMENT = 0
        MAX_STAR = 3
        MIN_STAR = 0

        if ( 
            self.__private_validate_number(
            MIN_ELEMENT, MAX_ELEMENT, n_element
            )
            and self.__private_validate_number(
            MIN_STAR, MAX_STAR, n_star
            )
            and n_star + n_element <= 3
        ):
             return True
        else:
            print("Invalid elemental and star stones ammount")
            print("Max elemental is 1 and max star is 3, and their sum max is 3")
            return False




# smith1 = Forge(
#     job_lvl=50, anvil="Oridecon", weaponry_lvl = 5, oridec_research = 5,
#     smith_skills = 5, dex = 99, luk = 99
#     )
# print(smith1.validate_stone_number(1.2))