import random

def inicio(tx_center):
  
  print('')
  print(' '*int(tx_center-25)+'*************************************************')
  print(' '*int(tx_center-23)+'Bienvenido al juego de piedra, papel o tijera')
  print(' '*int(tx_center-25)+'*************************************************')
  print('')

  usuario = input('¿Cual es tu nombre? ==> ').title() # Pedir nombre al usuario
  print('')
  print(f'Hola {usuario}, ¡¡Buena suerte!!')
  print('')
  num_rounds = input('¿Cuantas partidas quieres jugar? ==> ') # Pedir numero de rounds
  num_rounds = int(num_rounds)
  print('')
  
  return usuario, num_rounds
  
def choose_options():
  opciones = ('piedra', 'papel', 'tijera')
 
  while True:  # Continuar pidiendo una opción hasta que el usuario ingrese una válida
    user_option = input('Elije ¿piedra, papel o tijera? ==> ') # Pedir al usuario que ingrese su opción
    user_option = user_option.lower()
    
    if user_option not in opciones: # Verificar si la opción del usuario es válida
      print(f'Al parecer te equivocaste "{user_option}" no es una opción :´( intenta de nuevo')
    
    else:
      break
  
  computer_option = random.choice(opciones)
  
  print("")
  print(f'La computadora elige ==> {computer_option}')
  print("")
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins, usuario, tx_center):
  if user_option == computer_option: 
    print('')
    print(' '*int(tx_center-7-len(usuario)/2)+'..Empataste '+usuario+'..')
    print('')
  elif user_option == 'piedra' and computer_option == 'tijera':
    print(f'{user_option} gana a {computer_option}')
    print('')
    print(' '*int(tx_center-6-len(usuario)/2)+'¡Ganaste '+usuario+'! :)')
    print('')
    user_wins += 1   
  elif user_option == 'piedra' and computer_option == 'papel':
    print(f'{computer_option} gana a {user_option}')
    print('')
    print(' '*int(tx_center-7-len(usuario)/2)+'¡Perdiste '+usuario+'! :(')
    print('')
    computer_wins += 1
  elif user_option == 'papel' and computer_option == 'piedra':
    print(f'{user_option} gana a {computer_option}')
    print('')
    print(' '*int(tx_center-6-len(usuario)/2)+'¡Ganaste '+usuario+'! :)')
    print('')
    user_wins += 1
  elif user_option == 'papel' and computer_option == 'tijera':
    print(f'{computer_option} gana a {user_option}')
    print('')
    print(' '*int(tx_center-7-len(usuario)/2)+'¡Perdiste '+usuario+'! :(')
    print('')
    computer_wins += 1
  elif user_option == 'tijera' and computer_option == 'papel':
    print(f'{user_option} gana a {computer_option}')
    print('')
    print(' '*int(tx_center-6-len(usuario)/2)+'¡Ganaste '+usuario+'! :)')
    print('')
    user_wins += 1
  elif user_option == 'tijera' and computer_option == 'piedra':
    print(f'{computer_option} gana a {user_option}')
    print('')
    print(' '*int(tx_center-7-len(usuario)/2)+'¡Perdiste '+usuario+'! :(')
    print('')
    computer_wins += 1
  return user_wins, computer_wins

def run_game():
  tx_center = 40
  usuario, num_rounds = inicio(tx_center)
  rounds = 1
  user_wins = 0
  computer_wins = 0
      
  while True:
       
    print('')
    print('*' * 11)
    print('  Round', rounds)
    print('*' * 11)
    print('')
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins, usuario, tx_center)
    result = check_winner(user_wins, computer_wins, usuario, num_rounds, tx_center)
    
    if result:
      break

    rounds += 1

def check_winner(user_wins, computer_wins, usuario, num_rounds, tx_center):
  
  print(' '*int(tx_center-7)+'El marcador es:')
  print('')
  print(' '*int(tx_center-1-len(usuario)/2)+usuario+'= '+str(user_wins))
  print(' '*int(tx_center-1)+'Vs')
  print(' '*int(tx_center-7)+'Computadora= '+str(computer_wins))
  
  if computer_wins == num_rounds:
    print('')
    print(' '*int(tx_center-19)+'***************************************')
    print(' '*int(tx_center-19)+'*  Lo siento... ¡Te gané la partida!  *')
    print(' '*int(tx_center-19)+'***************************************')
    return True
    
  if user_wins == num_rounds:
    print("  ")
    print(' '*int(tx_center-17-len(usuario)/2)+'**********************************'+'*'*len(usuario))
    print(' '*int(tx_center-17-len(usuario)/2)+'*  '+usuario+' ¡Bien! !Ganaste la partida!  *')
    print(' '*int(tx_center-17-len(usuario)/2)+'**********************************'+'*'*len(usuario))
    return True
    
run_game()