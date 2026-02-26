class Wizard:
    def __init__(self, fire, icr, lightning, ets):
        self.fire = fire
        self.icr =icr
        self.lightning = lightning

    def cast_spell(self):
        print (self.name, "castes a", self.fire, self.icr, self.lightning, self.ets, "spell!" )

wizard1 = Wizard("motasem", "fire","100")
wizard2 = Wizard("balsam", "buteful", "200")

print(wizard1.name, "-", wizard1.element)
print(wizard2.name, "-",  wizard2.element)

wizard1.cast_spell()
wizard2.cast_spell()


   
  