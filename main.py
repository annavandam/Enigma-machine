alfabet = "abcdefghijklmnopqrstuvwxyz"
VertaaldeTekst = []

steckerbrett = { "a" : "z",
                 "z" : "a",
                 "b" : "i",
                 "i" : "b",
                 "g" : "f",
                 "f" : "g"}



#De class van de rotoren, hiervan worden later drie objecten gemaakt omdat er drie rotoren zijn.
class Rotor:
  def __init__(self, nummer, lettervolgorde, stand):
    self.nummer = nummer
    self.stand = stand
    self.lettervolgorde = lettervolgorde

#Functie die een rotor een aantal keer laat draaien.
def RotorDraai(draaiingen, rotor):
  rotor = (rotor.lettervolgorde[-draaiingen:] + rotor.lettervolgorde)[0: 26]
  return rotor


def LetterDoorRotoren(InputLetter):
  if alfabet.find(InputLetter) == -1:
    return InputLetter
  #Gaat door rotor 1, 2 & 3.
  InputLetter = rotor1.lettervolgorde[alfabet.index(InputLetter)]
  InputLetter = rotor2.lettervolgorde[alfabet.index(InputLetter)]
  InputLetter = rotor3.lettervolgorde[alfabet.index(InputLetter)]
  #Alfabet omkeren.
  InputLetter = alfabet[::-1][alfabet.index(InputLetter)]
  #Opnieuw door de rotoren maar nu vanaf de andere kant benaderd.
  InputLetter = alfabet[rotor3.lettervolgorde.index(InputLetter)]
  InputLetter = alfabet[rotor2.lettervolgorde.index(InputLetter)]
  InputLetter = alfabet[rotor3.lettervolgorde.index(InputLetter)]

  #Rotor 1 draait één tikje.
  rotor1.lettervolgorde = RotorDraai(1, rotor1)
  rotor1.stand += 1

  #Als rotor 1 een volledige draai heeft gemaakt, draait rotor 2 één tikje.
  if rotor1.stand % 26 == 0:
    rotor1.stand = 0
    rotor2.lettervolgorde = RotorDraai(1, rotor2)
    rotor2.stand += 1
    #Als rotor 2 een volledige draai heeft gemaakt, draait rotor 3 één tikje.
    if rotor2.stand % 26 == 0:
      rotor2.stand = 0
      rotor3.lettervolgorde = RotorDraai(1, rotor3)
      rotor3.stand += 1
  return InputLetter


#De rotoren worden hier aangemaakt.
rotor1 = Rotor(1, alfabet,  0)
rotor2 = Rotor(2, alfabet,  0)
rotor3 = Rotor(3, alfabet,  0)

#Hier wordt de gebruiker begeleid om de beginwaarden van de rotoren in te voeren en om de om te zetten tekst in te voeren. Verkeerde input wordt gemeld. Hierna kan de gebruiker zonder problemen de goede input invoeren.
print("Voer de standen van de rotoren in.")
while True:
  print("Stand rotor 1:")
  try:
   rotor1.stand = int(input())
   break
  except:
    print("Hier kunt u alleen getallen invoeren.")
while True:
  print("Stand rotor 2:")
  try:
   rotor2.stand = int(input())
   break
  except:
    print("Hier kunt u alleen getallen invoeren.")
while True:
  print("Stand rotor 3:")
  try:
   rotor3.stand = int(input())
   break
  except:
    print("Hier kunt u alleen getallen invoeren.")

print("Voer de tekst in die u wilt encrypten/decrypten.")
#De tekst input die het moet worden gecodeerd. 
TeVertalenString = input()

#De TeVertalenString wordt een list.
TeVertalenLijst = [char for char in TeVertalenString.lower()]

#De rotoren worden gedraaid naar hun standbeginstand
rotor1.lettervolgorde = RotorDraai(rotor1.stand, rotor1)
rotor2.lettervolgorde = RotorDraai(rotor2.stand, rotor2)
rotor3.lettervolgorde = RotorDraai(rotor3.stand, rotor3)

#Hier gaan de letters daadwerkelijk door de rotoren:
#Per letter wordt dit doorlopen.
for x in TeVertalenLijst:
  if x in steckerbrett:
    x = steckerbrett[x]
  x = LetterDoorRotoren(x)
  if x in steckerbrett:
    x = steckerbrett[x]
  VertaaldeTekst.append(x)


#Printen van de gecodeerde tekst
print("\nDit is de omgezette tekst:")
print("".join(VertaaldeTekst))
