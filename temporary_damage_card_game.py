from card_game import CardGame
from creature import Creature


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
        marker =  defender.health - attacker.attack 
        if(marker <= 0 ):
            defender.health = marker
