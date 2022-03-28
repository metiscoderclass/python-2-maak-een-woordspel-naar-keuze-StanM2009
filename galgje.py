print("===galgje===")
import random
lengte = ""
geraden = []
fout = []

if input("willekeurig woord? ") == "ja": 
  woorden = ["een", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen", "tien"]
  woord = random.choice(woorden)
else: 
  woord = input("welk woord? ").lower()
  for i in range(30):
    print("")
    
for i in range(len(woord)):
  geraden.append("-")
  lengte = lengte + "_"
print(geraden)

def raad(letter):
  index = 0
  i = 0
  while index < len(woord):
    index = woord.find(letter, index)
    if woord.find(letter) != -1 and len(letter) == 1 and not index == -1:
      geraden.pop(index)
      geraden.insert(index, letter)
    else:
      if i == 0:
        fout.append(letter)
      break
    index += 1
    i += 1

def printFout(aantal):
  print("  __________")
  print("  |        |")
  if aantal == 0:
    print("  |")
    print("  |")
    print("  |")
  elif aantal == 1:
    print("  |        0")
    print("  |")
    print("  |")
  elif aantal == 2:
    print("  |       \\0/ ")
    print("  |")
    print("  |")
  elif aantal == 3:
    print("  |       \\0/")
    print("  |        |")
    print("  |")
  elif aantal == 4:
    print("  |       \\0/")
    print("  |        |")
    print("  |        /")
  elif aantal == 5:
    print("  |       \\0/")
    print("  |        |")
    print("  |        /\ ")
  print("__|__")
        
while len(fout) < 5:
  raad(input("welke letter? ").lower())
  print(geraden)
  if "-" not in geraden:
    print("gewonnen!")
    break
  if len(fout) > 0:
    print("fout:" + str(fout))
  printFout(len(fout))
  
print(str(len(fout)) + " keer fout geraden")
