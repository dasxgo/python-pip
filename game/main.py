# aleatoriedad (import random - random.choice)
import random

options = ( "piedra", "papel", "tijera")

computer_wins = 0
user_wins = 0


rounds = 1

while True:

  print("*" * 10)
  print("ROUND", rounds)
  print("*" * 10)

  print("computer_wins", computer_wins)
  print("user_wins", user_wins)

  user = input("piedra, papel o tijera => ")
  user = user.lower()

  rounds += 1
  
  if not user in options:
    print("esa opcion no es valida")
    continue
  
  computer = random.choice(options) 
  
  print("user =>", user)
  print("computer =>", computer)
  
  if user == computer:
    print("empate")
  elif user == "piedra":
    if computer == "tijera":
      print("piedra gana a tijera")
      print ("user gana")
      user_wins += 1
    else: 
      print("papel gana a piedra")
      print("computer gano")
      computer_wins += 1
  elif user == "papel":
    if computer == "piedra":
      print("papel gana a piedra")
      print("user gano")
      user_wins += 1
    else:
      print("tijera gana a papel")
      print("computer gana")
      computer_wins += 1
  
  elif user == "tijera":
    if computer == "papel":
      print("tijera gana a papel")
      print("user gana")
      user_wins += 1
    else:
      print("piedra gana a tijera")
      print("computer gano")
      computer_wins += 1
  
  if computer_wins == 2:
    print ("El ganador es la computadora")
    break
  if user_wins == 2:
    print ("El ganador es el user")
    break
        
