import random
import os

move = ['papel', 'pedra', 'tesoura']

player_count = 0
empate_count =  0
computer_count = 0

print('=====================')
print('Bem Vindo ao jogo, Pedra, Papel e Tesoura')

def main_print():
    print('=====================')
    print('\nPlacar:')
    print('Você: {}'.format(player_count))
    print('Computador: {}'.format(player_count))
    print('\n')
    print('Escolha seu lance:')
    print('0 - Papel | 1 - Pedra | 2 - Tesoura')

def select_move():
    return random.choice(move)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                print("Favor escolher os valores entre 0 | 1 | 2")
                raise
            return move[player_move]
        except Exception as e:
            print(e)

def select_winner (p_move, c_move):
    global player_count, computer_count, empate_count
    #Player Move como papel e checando quem ganhou
    if p_move == 'papel':
        if c_move == 'pedra':
            player_count += 1
            return 'p'
        
        elif c_move == 'tesoura':
            computer_count += 1
            return 'c'
        
        else:
            empate_count += 1
            return 'd'
    
    #Player Move como pedra e checando quem ganhou
    if p_move == 'pedra':
        if c_move == 'tesoura':
            player_count += 1
            return 'p'
        
        elif c_move == 'papel':
            computer_count += 1
            return 'c'
        
        else:
            empate_count += 1
            return 'd'

    #Player Move como Tesoura e checando quem ganhou
    if p_move == 'tesoura':
        if c_move == 'papel':
            player_count += 1
            return 'p'
        
        elif c_move == 'pedra':
            computer_count += 1
            return 'c'
        
        else:
            empate_count += 1
            return 'd'
            
again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move,computer_move)

    print('')
    print('=====================')
    print('Sua jogada: {}'.format(player_move.upper()))
    print('Jogada do Computador: {}'.format(computer_move.upper()))

    if winner == 'p':
        print('Você venceu!')
    elif winner == 'c':
        print('Você perdeu!')
    else:
        print('Empate!')
    print('=====================')

    while True:
        print('Jogar novamente? 0 - Sim | 1 - Não')
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            again = 0
            break
    
    os.system('cls')