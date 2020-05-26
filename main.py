alfabet = "abcdefghijklmnopqrstuvwxyz"

#De class van de rotoren, hiervan worden later drie objecten gemaakt omdat er drie rotoren zijn.
class Rotor:
  def __init__(self, nummer, lettervolgorde, beginstand):
    self.nummer = nummer
    self.beginstand = beginstand
    self.lettervolgorde = lettervolgorde

#De rotoren worden hier aangemaakt.
rotor1 = Rotor(1, alfabet,  0)
rotor2 = Rotor(2, alfabet,  0)
rotor3 = Rotor(3, alfabet,  0)

#Hier wordt de gebruiker begeleid om de beginwaarden van de rotoren in te voeren en om de om te zetten tekst in te voeren. Verkeerde input wordt gemeld. Hierna kan de gebruiker zonder problemen de goede input invoeren.
print("Voer de beginstanden van de rotoren in.")
while True:
  print("Stand rotor 1:")
  try:
   rotor1.beginstand = int(input())
   break
  except:
    print("Hier kunt u alleen getallen invoeren.")
while True:
  print("Stand rotor 2:")
  try:
   rotor2.beginstand = int(input())
   break
  except:
    print("Hier kunt u alleen getallen invoeren.")
while True:
  print("Stand rotor 3:")
  try:
   rotor3.beginstand = int(input())
   break
  except:
    print("Hier kunt u alleen getallen invoeren.")

print("Voer de tekst in die u wilt omzetten.")
#De tekst input die het moet worden gecodeerd. 
TeVertalenString = input()

#De TeVertalenString wordt een list.
TeVertalenLijst = [char for char in TeVertalenString.lower()]

#Functie die een rotor een aantal keer laat draaien.
def RotorDraai(draaiingen, rotor):
  rotor = (rotor.lettervolgorde[-draaiingen:] + rotor.lettervolgorde)[0: 26]
  return rotor

#De rotoren worden gedraaid naar hun beginstand
rotor1.lettervolgorde = RotorDraai(rotor1.beginstand, rotor1)
rotor2.lettervolgorde = RotorDraai(rotor2.beginstand, rotor2)
rotor3.lettervolgorde = RotorDraai(rotor3.beginstand, rotor3)
