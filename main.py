alfabet = "abcdefghijklmnopqrstuvwxyz"
VertaaldeTekst = []
rotoren = []
steckerbrett = {}

class Enigma:
  def __init__(self, rotoren, steckerbrett):
   self.rotoren = rotoren
   self.steckerbrett = steckerbrett

#Functie die een rotor een aantal keer laat draaien.
def RotorDraai(draaiingen, rotor):
  rotor = (rotor[-draaiingen:] + rotor)[0: 26]
  return rotor

def LetterDoorRotoren(InputLetter):
  if alfabet.find(InputLetter) == -1:
    return InputLetter
  #Gaat door rotor 1, 2 & 3.
  for n in enigma.rotoren:
    InputLetter = n[0][alfabet.index(InputLetter)]

  #Alfabet omkeren.
  InputLetter = alfabet[::-1][alfabet.index(InputLetter)]

  #Opnieuw door de rotoren maar nu vanaf de andere kant benaderd.
  InputLetter = alfabet[enigma.rotoren[2][0].index(InputLetter)]
  InputLetter = alfabet[enigma.rotoren[1][0].index(InputLetter)]
  InputLetter = alfabet[enigma.rotoren[0][0].index(InputLetter)]
  #Rotor 1 draait één tikje.
  enigma.rotoren[0][0] = RotorDraai(1, rotoren[0][0])
  enigma.rotoren[0][1] += 1

  #Als rotor 1 een volledige draai heeft gemaakt, draait rotor 2 één tikje.
  if enigma.rotoren[0][1] % 26 == 0:
    enigma.rotoren[0][1] = 0
    enigma.rotoren[1][0] = RotorDraai(1, rotoren[1][0])
    enigma.rotoren[1][1] += 1
    #Als rotor 2 een volledige draai heeft gemaakt, draait rotor 3 één tikje.
    if enigma.rotoren[1][1] % 26 == 0:
      enigma.rotoren[1][1] = 0
      enigma.rotoren[2][0] = RotorDraai(1, rotoren[2][0])
      enigma.rrotoren[2][1] += 1
  return InputLetter

#Hier wordt de gebruiker begeleid om de beginwaarden van de rotoren in te voeren en om de om te zetten tekst in te voeren. Verkeerde input wordt gemeld. Hierna kan de gebruiker zonder problemen de goede input invoeren.

def SteckerbrettInstellen():
  print("Voer de tien koppels van het stekkerbed in.")
  for x in range(10):
    while True:
      print("Koppel {}:".format(x+1))
      try:
        koppel = str(input())
        steckerbrett[koppel[0]] = koppel[1]
        steckerbrett[koppel[1]] = koppel[0]
        break
      except: 
        print("Hier kunt u alleen twee letters invoeren")


def RotorenInstellen():
  print("Voer de standen van de rotoren in.")
  for x in range(3):
    while True:
      print("Stand rotor {}:".format(x+1))
      try:
       rotoren.append([alfabet,int(input())])
       break
      except:
        print("Hier kunt u alleen getallen invoeren.")

#START PROGRAMMA

while True:
  TeVertalenLijst = []
  rotoren = []
  steckerbrett = {}
  VertaaldeTekst = []


  DeInput = input("Wilt u het steckerbrett gebruiken? Ja of Nee ")
  if (DeInput == "JA" or DeInput == "ja" or DeInput == "Ja"):
    SteckerbrettInstellen()
  
  RotorenInstellen()

  print("Voer de tekst in die u wilt encrypten/decrypten.")
  #De tekst input die het moet worden gecodeerd. 
  TeVertalenString = input()
  #De TeVertalenString wordt een list.
  TeVertalenLijst = [char for char in TeVertalenString.lower()]

  enigma = Enigma(rotoren, steckerbrett)

  #De rotoren worden gedraaid naar hun standbeginstand
  for n in rotoren:
    n[0] = RotorDraai(n[1], n[0])

  #Hier gaan de letters daadwerkelijk door de rotoren en steckerbrett.
  #Per letter wordt dit doorlopen.

  for x in TeVertalenLijst:
    #Door steckerbrett
    if x in enigma.steckerbrett:
      x = enigma.steckerbrett[x]

    #Door rotoren
    x = LetterDoorRotoren(x)

    #Door steckerbrett
    if x in enigma.steckerbrett:
      x = enigma.steckerbrett[x]

    VertaaldeTekst.append(x)

  #Printen van de gecodeerde tekst
  print("\nDit is de omgezette tekst:")
  print("".join(VertaaldeTekst))
  print("\nWilt u nog een keer?")
  
  while True:
    if input("Wilt u nog een keer? Ja of Nee") == "ja" or input("Wilt u nog een keer? Ja of Nee") == "JA" or input("Wilt u nog een keer? Ja of Nee") == "Ja":
      break
