# maak hier de hele enigma machine in python :D
alfabet = "abcdefghijklmnopqrstuvwxyz"

class Rotor:
  def __init__(self, nummer, lettervolgorde, beginstand):
    self.nummer = nummer
    self.beginstand = beginstand
    self.lettervolgorde = lettervolgorde


#Rotor 1 wordt aangemaakt met de class. Nummer van rotor, beginwaarde = het alfabet, beginwaarde kan worden ingevoerd. Dus hier met beginwaarde 2 , 0, 0
rotor1 = Rotor(1, alfabet,  0)
rotor2 = Rotor(2, alfabet,  0)
rotor3 = Rotor(3, alfabet,  0)