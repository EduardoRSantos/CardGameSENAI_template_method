from card_game import CardGame
from creature import Creature


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
        marker =  defender.health - attacker.attack 
        defender.health = marker