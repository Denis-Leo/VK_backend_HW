import unittest
from TicTacGame import TicTacGame


class TestTicTacGame(unittest.TestCase):

    def setUp(self):
        self.tictac = TicTacGame()

    def test_check_winner_none(self):
        self.assertEqual(self.tictac.check_winner(), None)

    def test_game_step11(self):
        self.assertEqual(self.tictac.game_step('1 1', show = False), 
        [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    def test_game_step33(self):
        self.assertEqual(self.tictac.game_step('3 3'), 
        [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', 'x']])

    def test_validate_text(self):
        self.assertEqual(self.tictac.game_step('textt',show = False), False)


    def test_validate_uncorrect_coord(self):
        self.assertEqual(self.tictac.game_step('1 5',show = False), False)
        self.assertEqual(self.tictac.game_step('5 1',show = False), False)      
        self.assertEqual(self.tictac.game_step('100 55',show = False), False) 
        self.assertEqual(self.tictac.game_step('-1 1',show = False), False) 
        self.assertEqual(self.tictac.game_step('0 1',show = False), False) 

    def test_validate_more2numdrs(self):
        self.assertEqual(self.tictac.game_step('1 1 2',show = False), False)
        self.assertEqual(self.tictac.game_step('2 2 1',show = False), False)      

    def test_validate_backspase(self):
        self.assertEqual(self.tictac.game_step('1    1', show = False), 
        [['x', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']])        

    def test_validate_backspase2(self):
        self.assertEqual(self.tictac.game_step('  1    1  ', show = False),
        [['x', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']])

    def test_game1_winner_x(self):
        self.assertEqual(self.tictac.game_step('1 1', show = False), 
        [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
        self.assertEqual(self.tictac.game_step('1 2', show = False),
        [['x', 'o', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
        self.assertEqual(self.tictac.game_step('2 1', show = False),
        [['x', 'o', ' '], ['x', ' ', ' '], [' ', ' ', ' ']])
        self.assertEqual(self.tictac.game_step('2 2', show = False),
        [['x', 'o', ' '], ['x', 'o', ' '], [' ', ' ', ' ']])
        self.assertEqual(self.tictac.check_winner(), None)
        self.assertEqual(self.tictac.game_step('3 1', show = False), 
        [['x', 'o', ' '], ['x', 'o', ' '], ['x', ' ', ' ']])
        self.assertEqual(self.tictac.check_winner(), 'x')

    def test_game2_winner_o(self):
        self.assertEqual(self.tictac.game_step('1 1', show = False), 
        [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.game_step('1 2', show = False), 
        [['x', 'o', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])              
        self.assertEqual(self.tictac.game_step('2 1', show = False), 
        [['x', 'o', ' '], ['x', ' ', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.game_step('2 2', show = False), 
        [['x', 'o', ' '], ['x', 'o', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.check_winner(), None)
        self.assertEqual(self.tictac.game_step('3 3', show = False), 
        [['x', 'o', ' '], ['x', 'o', ' '], [' ', ' ', 'x']])        
        self.assertEqual(self.tictac.game_step('3 2', show = False), 
        [['x', 'o', ' '], ['x', 'o', ' '], [' ', 'o', 'x']])        
        self.assertEqual(self.tictac.check_winner(), 'o')       

    def test_game3_winner_o(self):
        self.assertEqual(self.tictac.game_step('1 1', show = False), 
        [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.game_step('1 2', show = False), 
        [['x', 'o', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])              
        self.assertEqual(self.tictac.game_step('2 1', show = False), 
        [['x', 'o', ' '], ['x', ' ', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.game_step('2 2', show = False), 
        [['x', 'o', ' '], ['x', 'o', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.check_winner(), None)
        self.assertEqual(self.tictac.game_step('3 3', show = False), 
        [['x', 'o', ' '], ['x', 'o', ' '], [' ', ' ', 'x']])        
        self.assertEqual(self.tictac.game_step('1 3', show = False), 
        [['x', 'o', 'o'], ['x', 'o', ' '], [' ', ' ', 'x']])        
        self.assertEqual(self.tictac.game_step('3 2', show = False), 
        [['x', 'o', 'o'], ['x', 'o', ' '], [' ', 'x', 'x']])  
        self.assertEqual(self.tictac.game_step('3 1', show = False), 
        [['x', 'o', 'o'], ['x', 'o', ' '], ['o', 'x', 'x']])  
        self.assertEqual(self.tictac.game_step('2 3', show = False), 
        [['x', 'o', 'o'], ['x', 'o', 'x'], ['o', 'x', 'x']]) 
        self.assertEqual(self.tictac.check_winner(), 'o')       
   
    def test_game3_not_winner(self):
        self.assertEqual(self.tictac.game_step('1 1', show = False), 
        [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.game_step('1 2', show = False), 
        [['x', 'o', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])              
        self.assertEqual(self.tictac.game_step('2 1', show = False), 
        [['x', 'o', ' '], ['x', ' ', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.game_step('2 2', show = False), 
        [['x', 'o', ' '], ['x', 'o', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.check_winner(), None)
        self.assertEqual(self.tictac.game_step('3 3', show = False), 
        [['x', 'o', ' '], ['x', 'o', ' '], [' ', ' ', 'x']])        
        self.assertEqual(self.tictac.game_step('3 1', show = False), 
        [['x', 'o', ' '], ['x', 'o', ' '], ['o', ' ', 'x']])        
        self.assertEqual(self.tictac.game_step('1 3', show = False), 
        [['x', 'o', 'x'], ['x', 'o', ' '], ['o', ' ', 'x']])  
        self.assertEqual(self.tictac.game_step('2 3', show = False), 
        [['x', 'o', 'x'], ['x', 'o', 'o'], ['o', ' ', 'x']])  
        self.assertEqual(self.tictac.game_step('3 2', show = False), 
        [['x', 'o', 'x'], ['x', 'o', 'o'], ['o', 'x', 'x']]) 
        self.assertEqual(self.tictac.check_winner(), 'x and o')       
        self.assertEqual(self.tictac.game_step('3 2', show = False), False)           

    def test_more_one_time_to_one_cell(self):
        self.assertEqual(self.tictac.game_step('1 1', show = False), 
        [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])        
        self.assertEqual(self.tictac.game_step('1 2', show = False), 
        [['x', 'o', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])              
        self.assertEqual(self.tictac.game_step('1 1', show = False), False)
        self.assertEqual(self.tictac.game_step('1 2', show = False), False)

    def test_game_step(self):
        self.assertEqual(self.tictac.game_step('1 1'), 
        [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])


if __name__ == "__main__":
    unittest.main()
