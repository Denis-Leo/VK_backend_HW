
import numpy as np

class TicTacGame:
    '''Игра в крестики- нолики
        первым ходит кт остаит крестик   '''
    def __init__(self):
#       self.board = [[0,0,0],[0,0,0][0,0,0]]   
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]   
        self.step = 0
        

    def show_board(self):
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
        
    def instruction_game(self):
        print(''' Вас приветсвует игра Крестики-нолики!
        Выберите режим игры:
        1 - два человека 
        2 - человек крестик и компьютер
        3 - компьютер и человек нолик
        4 - два компьютера
        ''')

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


    @staticmethod
    def __call_to_str(call):
        if call == 0 :
            return ' '
        if call == 1:
            return 'x'
        if call == 2:
            return 'o'
        return None


    def validate_input(self, text):
        if not ' ' in text:
            print('Координаты нужно вводить через пробел')
            return False
        if not len(text.split()) == 2:
            print('Координаты должны быть ровно две') 
            return False   

        x,y = text.split()

        if not (x.isdigit() and y.isdigit()):
            print('Координаты должны быть числами')
            return False

        x,y = int(x),int(y)  

        if not ((type(x),type(y)) == (int,int) and (1<=x<=3) and (1<=y<=3)):
            print('Координаты должны быть целыми числами 1,2,3 ')
            return False
        if not self.board[x-1][y-1] == ' ':
            print('Выбранная ячейка уже занята')    
            return False


        return True



    def start_game(self):
        self.instruction_game()

        while self.check_winner() == None:
            if self.step % 2 == 1:
                input_text = input('\n Поставить крестик в позицию:')
            else:
                input_text = input('\n Поставить нолик в позицию:')

            if self.validate_input(input_text):

                x,y = input_text.split()
                x,y = int(x)-1,int(y)-1
                print(x,y)

                if self.step % 2 == 1:
                    self.board[x][y] = 'x'
                else:
                    self.board[x][y] = 'o'
                self.show_board()
                self.step += 1
        winner = self.check_winner()
        if winner == 'x': print('Победил игрок крестик')
        if winner == 'o': print('Победил игрок нолик')   
        if winner == '-': print('Игра закончилась в ничью')

    def check_winner(self):
        troika_list = []
        for i in self.board:
            print(''.join(i))
            troika_list.append(''.join(i))
        for i in np.transpose(self.board):
            print(''.join(i))
            troika_list.append(''.join(i))
        troika_list.append(self.board[0][0] +self.board[1][1]+self.board[2][2] )
        troika_list.append(self.board[0][2] +self.board[1][1]+self.board[2][0] )
        
        for  i in troika_list:
            if i[0]!= ' ' and i[0]*3 == i:
                return i[0]

        if self.step >=9:
            return '-'
        return None

if __name__ == '__main__':
	game = TicTacGame()
	game.start_game()


#
#board_pattern = '''
#     {} | {} | {}
#    ___|___|____
#       |   | 
#     {} | {} | {}
#   ____|___|____
#       |   |
#     {} | {} | {}  
#'''
#
#
#board_pattern = '''
#     0 | x | 0
#    ___|___|____
#       |   | 
#     0 | x | 0
#   ____|___|____
#       |   |
#     x | x | 0  
#'''
#
#
#
#board_pattern = f'''
#     {a[0][0]]} | {a[0][1]} | {a[0][2]}
#    ___|___|____
#       |   | 
#     {a[1][0]} | {a[1][1]} | {a[1][2]}
#   ____|___|____
#       |   |
#     {a[2][0]} | {a[2][1]} | {a[2][2]}  
#'''
#

#board_pattern = '''
#      1   2   3  
# 1    0 | x | 0
#     ___|___|____
#        |   | 
# 2    0 | x | 0
#   _ ___|___|____
#        |   |
# 3    x | x | 0  
#'''
