import random
import os

class ticTacToe:
    def __init__(self) :
        self.reset()


    def print_board(self):
        print("")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])
        

    def reset(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def check_win_or_draw(self):
        dict_win = {}
        for i in ["X", "O"]:
            #horizontais
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            #verticais
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i)
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            #Diagonal
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][1] == self.board[2][0] == i) or dict_win[i]

        if dict_win["X"]:
            self.done = "x"
            print("X Venceu!")
            return 1
        elif dict_win["O"]:
            self.done = "o"
            print("O Venceu")
            return 1

        c = 0
        for i in range(3):
            for j in range(3):
               if self.board[i][j] != " ":
                   c += 1
                   break
               
        if c == 0:
            self.done = "d"
            print("Empate")
            return

    def get_player_move(self):
        invalid_move = True

        while invalid_move:
            try:
                print("Digite a linha do seu próximo lance:")
                x = int(input())

                print("Digite a coluna do seu próximo lance:")
                y = int (input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print ("Coordenadas Inválidas")

                if self.board[x][y] != " ":
                    print("Posição já preenchida.")
                    continue

            except Exception as e:
                print(e)
                continue
            
            invalid_move = False

        self.board[x][y] = "X"

    def make_move(self):
        list_moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_moves.append((i, j))
                
        if len(list_moves) > 0:
            x, y = random.choice(list_moves)
            self.board[x][y] = "O"

    def get_player2_move(self):
        invalid_move = True

        while invalid_move:
            try:
                print("Player 2 - Digite a linha do seu próximo lance:")
                x = int(input())

                print("Player 2 - Digite a coluna do seu próximo lance:")
                y = int (input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print ("Coordenadas Inválidas")

                if self.board[x][y] != " ":
                    print("Posição já preenchida.")
                    continue

            except Exception as e:
                print(e)
                continue
            
            invalid_move = False

        self.board[x][y] = "O"



tic_tac_toe = ticTacToe()
tic_tac_toe.print_board()
next = 0

while next == 0:
    print("Digite 1 - Jogar Solo | 2 - Multiplayer")
    escolha = int(input())
    if escolha == 1:
        os.system("cls")
        tic_tac_toe.print_board()
        while tic_tac_toe.done == "":
            tic_tac_toe.get_player_move()
            tic_tac_toe.make_move()
            os.system("cls")
            tic_tac_toe.print_board()
            tic_tac_toe.check_win_or_draw()

        print("Digite 1 para sair do jogo ou qualquer tecla para jogar novamente.")

        next = int (input())

        if next == 1:
            break
        else:
            tic_tac_toe.reset()
            next = 0

    elif escolha == 2:
        os.system("cls")
        tic_tac_toe.print_board()
        while tic_tac_toe.done == "":
            tic_tac_toe.get_player_move()
            verificar = tic_tac_toe.check_win_or_draw()
            if verificar == 1:
                tic_tac_toe.print_board()
                break  
            os.system("cls")
            tic_tac_toe.print_board()
            tic_tac_toe.get_player2_move()
            os.system("cls")
            tic_tac_toe.print_board()
            tic_tac_toe.check_win_or_draw()

        print("Digite 1 para sair do jogo ou qualquer tecla para jogar novamente.")

        next = int (input())

        if next == 1:
            break
        else:
            tic_tac_toe.reset()
            next = 0
