
import random


def choose_options():
  options = ('piedra', 'papel', 'tijera') #Opciones elegibles
  user_option = input('piedra, papel o tijera => ') #Opciones del usuario
  user_option = user_option.lower() #Convierte a minúscula la opción del usuario para validar correctamente la opción elegida con la que existe en la base de datos osea options

  if not user_option in options:#Cuando la opción no es válida
    print('esa opción no es válida') 
    return None, None

    #continue

  computer_option = random.choice(options) #Genera de forma aleatoria una opción para la computadora, con la librería random
  
  print('User option =>', user_option) #Imprime lo que el usuario eligió
  print('Computer option =>', computer_option) #Imprime lo que la computadora eligió 
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('¡Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('¡User ganó!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('¡Computer ganó!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option== 'piedra':
      print('papel gana a piedra')
      print('¡User ganó!')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('¡Computer ganó!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('¡User ganó!')
      user_wins += 1
    else:
      print('¡Computer ganó!')
      computer_wins += 1
  return user_wins, computer_wins


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  
  while True:
  
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    
    print('computer_wins: ', computer_wins)
    print('user_wins: ', user_wins)
    rounds += 1
    
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    

    if computer_wins == 2:
      print('El rotundo ganador es la computadora')
      break
  
    if user_wins == 2:
      print('El rotundo ganador es el usuario')
      break
    
    rounds += 1

run_game()


  
