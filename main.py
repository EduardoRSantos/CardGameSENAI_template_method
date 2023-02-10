from creature import Creature
from permanent_damage_card_game import PermanentDamageCardGame
from temporary_damage_card_game import TemporaryDamageCardGame

# Case permanent_damage_card_game
creature_elf = Creature("Elf", 2, 2)
creature_orc = Creature("Orc", 2, 2)

# Case temporary_damage_card_game
creature_anao = Creature("Anao", 2, 2)
creature_bruxo = Creature("Bruxo", 1, 3)


creatures: list[Creature] = []

creatures.append(creature_elf)
creatures.append(creature_orc)
creatures.append(creature_anao)
creatures.append(creature_bruxo)

permanent_damage_card_game = PermanentDamageCardGame(creatures)
primeiro_round = permanent_damage_card_game.combat(creature_elf, creature_orc)
print(primeiro_round.name)
segundo_round = permanent_damage_card_game.combat(creature_elf, creature_orc)
print(segundo_round.name)
print("-="*30)
temporary_damage_card_game = TemporaryDamageCardGame(creatures)

primeiro_round = temporary_damage_card_game.combat(creature_anao, creature_bruxo)
print(primeiro_round.name)
