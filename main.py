alfabet = "abcdefghijklmnopqrstuvwxyz"
VertaaldeTekst = []

#class Enigma:
#  def __init__(self, rotoren, steckerbrett):
#    self.rotoren = rotoren
#    self.steckerbrett = steckerbrett

#Functie die een rotor een aantal keer laat draaien.
def RotorDraai(draaiingen, rotor):
  rotor = (rotor[-draaiingen:] + rotor)[0: 26]
  return rotor

def LetterDoorRotoren(InputLetter):
  if alfabet.find(InputLetter) == -1:
    return InputLetter
  #Gaat door rotor 1, 2 & 3.
  InputLetter = rotoren[0][0][alfabet.index(InputLetter)]
  InputLetter = rotoren[1][0][alfabet.index(InputLetter)]
  InputLetter = rotoren[2][0][alfabet.index(InputLetter)]
  #Alfabet omkeren.
  InputLetter = alfabet[::-1][alfabet.index(InputLetter)]
  #Opnieuw door de rotoren maar nu vanaf de andere kant benaderd.
  InputLetter = alfabet[rotoren[2][0].index(InputLetter)]
  InputLetter = alfabet[rotoren[1][0].index(InputLetter)]
  InputLetter = alfabet[rotoren[0][0].index(InputLetter)]
  #Rotor 1 draait één tikje.
  rotoren[0][0] = RotorDraai(1, rotoren[0][0])
  rotoren[0][1] += 1

  #Als rotor 1 een volledige draai heeft gemaakt, draait rotor 2 één tikje.
  if rotoren[0][1] % 26 == 0:
    rotoren[0][1] = 0
    rotoren[1][0] = RotorDraai(1, rotoren[1][0])
    rotoren[1][1] += 1
    #Als rotor 2 een volledige draai heeft gemaakt, draait rotor 3 één tikje.
    if rotoren[1][1] % 26 == 0:
      rotoren[1][1] = 0
      rotoren[2][0] = RotorDraai(1, rotoren[2][0])
      rotoren[2][1] += 1
  return InputLetter

rotoren = []

#Hier wordt de gebruiker begeleid om de beginwaarden van de rotoren in te voeren en om de om te zetten tekst in te voeren. Verkeerde input wordt gemeld. Hierna kan de gebruiker zonder problemen de goede input invoeren.


steckerbrett = {}

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

print("Voer de standen van de rotoren in.")
for x in range(3):
  while True:
    print("Stand rotor {}:".format(x+1))
    try:
     rotoren.append([alfabet,int(input())])
     break
    except:
      print("Hier kunt u alleen getallen invoeren.")


 
print("Voer de tekst in die u wilt encrypten/decrypten.")
#De tekst input die het moet worden gecodeerd. 
TeVertalenString = input()

#De TeVertalenString wordt een list.
TeVertalenLijst = [char for char in TeVertalenString.lower()]

#De rotoren worden gedraaid naar hun standbeginstand
#for n in rotoren:
#  n[0] = RotorDraai(n[1], n[0])
rotoren[0][0] = RotorDraai(rotoren[0][1], rotoren[0][0])
rotoren[1][0] = RotorDraai(rotoren[1][1], rotoren[1][0])
rotoren[2][0] = RotorDraai(rotoren[2][1], rotoren[2][0])

#Hier gaan de letters daadwerkelijk door de rotoren en steckerbrett.
#Per letter wordt dit doorlopen.
for x in TeVertalenLijst:
  #Door steckerbrett
  if x in steckerbrett:
    x = steckerbrett[x]

  #Door rotoren
  x = LetterDoorRotoren(x)

  #Door steckerbrett
  if x in steckerbrett:
    x = steckerbrett[x]
    
  VertaaldeTekst.append(x)

#Printen van de gecodeerde tekst
print("\nDit is de omgezette tekst:")
print("".join(VertaaldeTekst))
