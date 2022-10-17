# from tabnanny import check
import numpy as np

class TicTacGame:
    '''Игра в крестики- нолики
        первым ходит кто стаит крестик   '''
    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.step = 0


    def show_board(self):
        ' Show board for users'
        a = self.board
        board_pattern = f'''
     {a[0][0]} | {a[0][1]} | {a[0][2]}
   ____|___|____
       |   | 
     {a[1][0]} | {a[1][1]} | {a[1][2]}
   ____|___|____
       |   |
     {a[2][0]} | {a[2][1]} | {a[2][2]} '''
        print(board_pattern)
        return self.board

    def instruction_game(self):
        'Show instruction for users'
        print(' Вас приветсвует игра Крестики-нолики!')

        # text_add = '''
        # Выберите режим игры:
        # 1 - два человека
        # 2 - человек крестик и компьютер
        # 3 - компьютер и человек нолик
        # 4 - два компьютера
        # '''

        print(''' Все ячейки поля пронумерованы и имеют две координаты:

                |     |
            1,1 | 1,2 | 1,3
           _____|_____|_____
                |     | 
            2,1 | 2,2 | 2,3
           _____|_____|_____
                |     |
            3,1 | 3,2 | 3,3
                |     |
            При соверешнии хода вписывайте кординаты ячейки через пробел
            Удачной игры =)
        ''')

    def validate_input(self, text, show=True):
        if not ' ' in text:
            if show is True:
                print('Координаты нужно вводить через пробел')
            return False
        if not len(text.split()) == 2:
            if show is True:
                print('Координаты должны быть ровно две')
            return False

        x,y = text.split()

        if not (x.isdigit() and y.isdigit()):
            if show is True:
                print('Координаты должны быть числами')
            return False

        x,y = int(x),int(y)

        if not ((type(x),type(y)) == (int,int) and (1<=x<=3) and (1<=y<=3)):
            if show is True:
                print('Координаты должны быть целыми числами 1,2,3 ')
            return False
        if not self.board[x-1][y-1] == ' ':
            if show is True:
                print('Выбранная ячейка уже занята')
            return False


        return True

    def game_step(self, input_text, show = True):

        if self.validate_input(input_text,show=show):

            x,y = input_text.split()
            x,y = int(x)-1,int(y)-1
            # print(x,y)

            if self.step % 2 == 0:
                self.board[x][y] = 'x'
            else:
                self.board[x][y] = 'o'
            # self.show_board()
            self.step += 1
            return self.board
        else:
            return False


    def start_game(self):
        self.instruction_game()

        while self.check_winner() is None:

            if self.step % 2 == 0:
                input_text = input('\n Поставить крестик в позицию:')
            else:
                input_text = input('\n Поставить нолик в позицию:')

            self.game_step(input_text)
            self.show_board()

        self.winner_print()
        return self.check_winner()

    def check_winner(self):
        troika_list = []
        for i in self.board:
            # print(''.join(i))
            troika_list.append(''.join(i))
        for i in np.transpose(self.board):
            # print(''.join(i))
            troika_list.append(''.join(i))
        troika_list.append(self.board[0][0] +self.board[1][1]+self.board[2][2] )
        troika_list.append(self.board[0][2] +self.board[1][1]+self.board[2][0] )

        for  i in troika_list:
            if i[0]!= ' ' and i[0]*3 == i:
                return i[0]

        if self.step >= 9:
            return 'x and o'
        return None
    def winner_print(self):
        winner = self.check_winner()

        print('''********* ********************* *********
********* ********************* *********''')
        if winner == 'x': print('         Победил игрок крестик')
        if winner == 'o': print('          Победил игрок нолик')
        if winner == 'x and o': print('        Игра закончилась в ничью')
        print('''********* ********************* *********
********* ********************* *********\n''')

if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
