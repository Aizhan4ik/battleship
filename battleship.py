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
        
def is_valid_position(board, positions):
    for x, y in positions:
        if not (0 <= x < 7 and 0 <= y < 7):  
            return False
        if board[x][y] != ".":  
            return False
    
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 7 and 0 <= ny < 7 and board[nx][ny] == "S":
                    return False
    return True
