from stockfish import Stockfish
import time
stockfish = Stockfish(path=r"G:\Users\Ashutosh\Downloads\Compressed\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2\stockfish14.exe")

def user_input():
    move = input(">> ")
    return move
    
def main():
    print(stockfish.get_board_visual())
    game_end = False
    while not game_end:
        user_move = user_input()
        if stockfish.is_move_correct(user_move):
            stockfish.make_moves_from_current_position([user_move])
            print(stockfish.get_board_visual())
            print("----------------------------------------")
            time.sleep(1)
            ai_move = stockfish.get_best_move()
            stockfish.make_moves_from_current_position([ai_move])
            print(stockfish.get_board_visual())
            print("++++++++++++++++++++++++++++++++++++++++")
            eva = stockfish.get_evaluation()
            if eva["value"] == 0:
                game_end = True
            print(eva)
            print("++++++++++++++++++++++++++++++++++++++++")
        else:
            print("Wrong move try again!!")
            print(stockfish.get_board_visual())
            continue
    print("Game over!!!")
if __name__ == "__main__":
    main()
