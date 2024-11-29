import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    board = []
    for i in range(7): 
        board.append(["." for _ in range(7)])
    return board

def display_board(board):
    print("  1 2 3 4 5 6 7")
    print("  -------------")
    for i in range(7):
        print(chr(65 + i), " ".join(board[i]))