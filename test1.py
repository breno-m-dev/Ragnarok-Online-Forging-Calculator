import forge

smith1 = forge.Forge(
    job_lvl=50, anvil="Oridecon", weaponry_lvl = 5, oridec_research = 5,
    smith_skills = 5, dex = 99, luk = 99
    )
print("Testing stone 1.2")
print(smith1.validate_stone_number(1.2 ,1))

print("Testing stone 1")
print(smith1.validate_stone_number(1, 3))

print("Testing stone 3")
print(smith1.validate_stone_number(3, 0))

print("Testing stone 5")
print(smith1.validate_stone_number(1, 2))

print("Testing stone -1")
print(smith1.validate_stone_number(0, 0))

print("Testing stone 5")
print(smith1.validate_weapon(5))

print("Testing stone -1")
print(smith1.validate_weapon(-1))

print(smith1.get_forge_chance(1,0,3))