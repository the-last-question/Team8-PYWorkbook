import random

def passwordGenerate():
  randomLenght = random.randint(7,10)
  password = ''

  for x in range (randomLenght):
    randomChar = random.randint(33,126)
    password = password + chr(randomChar)

  print(password)

passwordGenerate()