from player import Player
import os

class Game():
    
    EMPTY_BOARD = "_ | _ | _\n_ | _ | _\n_ | _ | _"
    
    def __init__(self) -> None:
        self.isOn = True
        self.player_1 = Player(input("Player 1, what is your name?\n"), "X")
        self.player_2 = Player(input("Player 2, what is your name?\n"), "O")
        # self.player_1 = Player("P1", "X")
        # self.player_2 = Player("P2", "O")
        self.current_player = self.player_1
        self.placed_marks = [" "] * 9
    
    def draw_board(self):
        os.system('cls')
        board_to_print = self.EMPTY_BOARD
        for mark in self.placed_marks:
            board_to_print = board_to_print.replace("_", mark, 1)
        print(board_to_print)

    def play_turn(self):
        not_valid_input = True
        while not_valid_input:
            location = input(f"{self.current_player.name}, where do you want to place your mark?\n (row, column) eg. '11'\n")
            index = (int(location[0])-1)*3 + int(location[1])-1
            if self.placed_marks[index] == " " and index >= 0 and index <= 8:
                not_valid_input = False
                self.placed_marks[index] = self.current_player.mark
            else:
                print("That is not a valid location! Try again!")
   
    def check_for_win(self):
        mark = self.current_player.mark
        winning_condition = False
        draw = False
        
        # Check Rows
        for row in range(3):
            if all(self.placed_marks[i] == mark for i in range(row*3, row*3+3)):
                winning_condition = True

        # Check Columns
        for col in range(3):
            if all(self.placed_marks[i] == mark for i in range(col, col + 7, 3)):
                winning_condition = True
            
        # Check Diagonal
        if all(self.placed_marks[i] == mark for i in range(0, 9, 4)) or all(self.placed_marks[i] == mark for i in range(2, 7, 2)):
            winning_condition = True
        
        # Check for draw game
        if not " " in self.placed_marks and winning_condition == False:
            draw = True
        
        if winning_condition:
            self.end_game(draw)
        else:
            self.switch_player()

    
    def switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1
    
    def end_game(self, draw):
        print("Game Over!")
        self.draw_board()
        self.isOn = False
        if not draw:
            print(f"Winner is {self.current_player.name}")
        else:
            print("The Game was draw")

        
        