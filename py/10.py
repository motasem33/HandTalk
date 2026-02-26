class Player () :
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self):
        print( self.name, "attacks!")

    def take_damage(self, amount):
        self.health -=  amount
        print( self.name, "took", self.amount, "damage.health is naw", self.health)

    def is_alive(self):
        return self.health > 0
        Player1 = Player1 ("Hero", 100, 20)
        Player1.attack()
        Player1.take_damage(50)
        print("is alive?", Player1.is_alive())






