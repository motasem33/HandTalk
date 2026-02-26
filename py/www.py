class Wizard:
    def __init__(self, fire, icr, lightning):
        self.fire = fire
        self.icr =icr
        self.lightning = lightning

    def cast_spell(self):
        print ( self.fire,"castes a", self.icr, self.lightning, "spell!" )

wizard1 = Wizard("motasem", "fire","100")
wizard2 = Wizard("balsam", "buteful", "200")

print(wizard1.fire, "-", wizard1.icr)
print(wizard2.fire, "-",  wizard2.icr)

wizard1.cast_spell()
wizard2.cast_spell()


   
  