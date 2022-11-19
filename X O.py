import os
import platform

def clear():
       if platform.system() == "Windows": os.system('cls')
       if platform.system() == "Darwin" or platform.system() == "Linux": os.system('clear')
              
def main_menu():
       while True:
              clear()
              user = input("Welcome to my Tic-Tac-Toe Game!\n\tPress 1 to Play!\n\tPress Q to quit!\n")
              if user == "1":
                     break
              elif user == "q":
                     quit()
              else:
                     continue

lst = [["-", "-", "-",],
       ["-", "-", "-",],
       ["-", "-", "-",]]


def board_printer():
       clear()
       i = 1
       for x in lst: #Board Printer
              print(i, end="")
              i += 1
              print(x)

def turn_x():
       while True:
              
              move = input("What is your next move?\n (Line):(Row)\n")
              if lst[int(move[0])-1][int(move[2])-1] == "-":
                     lst[int(move[0])-1][int(move[2])-1] = "x"
                     return True
              else:
                     print("This spot was already taken.")
              
def turn_o():
       while True:
              
              move = input("What is your next move?\n(Line):(Row)\n")
              if lst[int(move[0])-1][int(move[2])-1] == "-":
                     lst[int(move[0])-1][int(move[2])-1] = "o"
                     return True
              else:
                     print("This spot was already taken.")  

def game_status():
       i = 0
       counter = 0
       while i < len(lst):  #Draw Checker
              if "-" not in lst[i]:
                     counter += 1

              if counter == 3:
                     return "draw"

              i += 1

       for i in lst: #Line Win Checker
              if i == ["x", "x", "x"]:
                     return "x"
              if i == ["o", "o", "o"]:
                     return "o"
       
       i = 0
       while i < 3: #Vertical Win Checker
              if lst[0][i] == "x" and lst[1][i] == "x" and lst[2][i] == "x": return "x"
              if lst[0][i] == "o" and lst[1][i] == "o" and lst[2][i] == "o": return "o"
              i += 1
       
       #ONLY 4 OUTCOMES: Diagonal Win Checker
       if lst[0][0] == "x" and lst[1][1] == "x" and lst[2][2] == "x": return "x"
       if lst[0][2] == "x" and lst[1][1] == "x" and lst[2][0] == "x": return "x"
       if lst[0][0] == "o" and lst[1][1] == "o" and lst[2][2] == "o": return "o"
       if lst[0][2] == "o" and lst[1][1] == "o" and lst[2][0] == "o": return "o"

def game():
       while True:
              while True:
                     valid_play = False
                     board_printer()
                     valid_play = turn_x()
                     if valid_play == True:
                            break
              
              result = game_status()
              if result == "x" or result == "o" or result == "draw":
                     break

              while True:
                     valid_play = False
                     board_printer()
                     valid_play = turn_o()
                     if valid_play == True:
                            break
              

              result = game_status()
              if result == "x" or result == "o" or result == "draw":
                     break
       
       if result == "x" or result == "o":
                     clear()
                     board_printer()
                     print("%s is the winner!\nRestart the program to start again." % result)
       if result == "draw":
                     clear()
                     board_printer()
                     print("Nobody Wins! It's a draw!\nRestart the program to start again")
   
main_menu()
game()
