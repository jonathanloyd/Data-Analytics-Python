#Author: Jonathan Loyd
#Description: Python3 Creating a Football Game Simulator (Testing Script)
#CSE590-59 Project 1

import hw1
from random import randint

if __name__ == "__main__":
    for iteration in range(1, 100):
        num_drives = randint(1, 100)
        prctT1 = randint(1, 100)
        yrangeT1 = (randint(1, 100), randint(1, 100))
        prctT2 = randint(1, 100)
        yrangeT2 = (randint(1, 100), randint(1, 100))
        print(hw1.simulategame(num_drives, prctT1, yrangeT1, prctT2, yrangeT2))
    for iteration in range(1, 100):
        yards_to_TD = randint(1, 99)
        successprct = randint(1, 100)
        yardrange = (randint(1, 100), randint(1, 100))
        print(hw1.drive(yards_to_TD, successprct, yardrange))
    for iteration in range(1, 100):
        yards_to_TD = randint(1, 100)
        successprct = randint(1, 100)
        yardrange = (randint(1, 100), randint(1, 100))
        print(hw1.drive_depicted(yards_to_TD, successprct, yardrange))
