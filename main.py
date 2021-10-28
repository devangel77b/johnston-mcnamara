import PySimpleGUI as sg
import time
from datetime import date
import sys
import os

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

current_date = date.today()

sg.theme('Dark Grey 13')

def hotswap_maker():
    with open("!HOTSWAP.txt", "w") as hotswap:
        hotswap.write("0\n0")
        hotswap.close()

def log_maker(home_score, away_score):
    with open(f"{current_date} - {current_time}.txt", "w") as logs:
        logs.write(f"Game at {current_date} - {current_time}\n")
        logs.write("home:")
        logs.write(str(home_score) + '\n')
        logs.write("away:")
        logs.write(str(away_score) + '\n')
        logs.close()

def score_counter(team):

    readscore = open("!HOTSWAP.txt", "r")
    read_score = readscore.readlines()
    homescore = read_score[0]
    awayscore = read_score[1]
    readscore.close()

    if team =='home':
        newscore = int(homescore) + 1
        print(homescore)
        print(newscore)

        if newscore < 5:
            with open("!HOTSWAP.txt", "w") as hotswap:
                hotswap.write(f"{newscore}\n{awayscore}")
                hotswap.close()
                buttons()
        elif newscore >= 5:
            print(f"game over. Home team wins, {newscore} to {awayscore}.")
            log_maker(newscore,awayscore)
            hotswap_maker()
            sys.exit()

    if team == 'away':
        newscore = int(awayscore) + 1

        if newscore < 5:
            with open("!HOTSWAP.txt", "w") as hotswap:
                hotswap.write(f"{newscore}\n{homescore}")
                hotswap.close()
                buttons()
        elif newscore >= 5:
            print(f"game over. Home team wins, {newscore} to {homescore}.")
            log_maker(homescore, newscore)
            hotswap_maker()
            sys.exit()

def button1():
    print('Button 1')

    score_counter('home')

def button2():
    print('Button 2')

    score_counter('away')

def button3():
    print("button 3")

    print("reseting")
    hotswap_maker()
    print("new game made")
    buttons()

def button4():
    sys.exit()

dispatch_dictionary = {
    '1':button1,
    '2':button2,
    '3':button3,
    'quit':button4,
}

def buttons():
    button = input("what button do you want to press? (1,2,3,quit)\n \n $")

    if button in dispatch_dictionary:
        dispatch_dictionary[button]()
        pass
    else:
        print("Unknown choice", button)
        buttons()


path = os.getcwd()
name = "!HOTSWAP.txt"

for root, dirs, files in os.walk(path):
    if name in files:
        buttons()
        break
    else:
        hotswap_maker()
        buttons()
        break

