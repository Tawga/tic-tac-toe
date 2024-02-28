from game import Game

def play_game():
    game = Game()
    while game.isOn:
        game.draw_board()
        game.play_turn()
        game.check_for_win()
    
if __name__ == '__main__':
    play_game()