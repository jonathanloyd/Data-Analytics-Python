#Author: Jonathan Loyd
#Description: Python3 Creating a Football Game Simulator
#CSE590-59 Project 1

from random import randint

def down(successprct, yardrange):
    """Simulate a down in football via random numbers"""
    success_check = randint(1,100)
    if success_check > successprct:
        return 0
    else:
        return randint(min(yardrange), max(yardrange))

def drive(yards_to_TD, successprct, yardrange):
    """Simulate a football drive and return points scored and the field position"""
    points_scored = 0
    field_position = 0
    for _ in range(1, 5):
        yards_to_TD -= down(successprct, yardrange)
        if yards_to_TD <= 0:
            field_position = 80
            point_luck = randint(1,100)
            if point_luck > 10:
                points_scored = 7
            else:
                points_scored = 6
            break
    if points_scored == 0:
        field_position = 100 - yards_to_TD
    return (points_scored, field_position)


def drive_depicted(yards_to_TD, successprct, yardrange):
    """Depict a drive with ASCII art"""
    points_scored = 0
    field_position = 0
    print_list = list("O")
    for two_yds in range(1,51):
        if two_yds == round(50- (yards_to_TD/2)) and yards_to_TD > 0:
            print_list.append(">")
        elif two_yds % 50 == 0:
            print_list.append("X")
        elif two_yds % 5 == 0:
            print_list.append("|")
        else:
            print_list.append("-")
    print("".join(print_list), end="\t")
    print(f"1st Down, {yards_to_TD} Yds to Go")
    for _ in range(1, 5):
        yards_to_TD -= down(successprct, yardrange)
        print_list = list("O")
        for two_yds in range(1,51):
            if two_yds == round(50- (yards_to_TD/2)) and yards_to_TD > 0 and _ == 4:
                print_list.append("Q")
            elif two_yds == round(50- (yards_to_TD/2)) and yards_to_TD > 0:
                print_list.append(">")
            elif two_yds % 50 == 0 and yards_to_TD <= 0:
                print_list.append("T")
            elif two_yds % 50 == 0:
                print_list.append("X")
            elif two_yds % 5 == 0:
                print_list.append("|")
            else:
                print_list.append("-")
        print("".join(print_list), end="\t")
        if _ == 1 and yards_to_TD > 0:
            print(f"2nd Down, {yards_to_TD} Yds to Go")
        elif _ == 2 and yards_to_TD > 0:
            print(f"3rd Down, {yards_to_TD} Yds to Go")
        elif _ == 3 and yards_to_TD > 0:
            print(f"4th Down, {yards_to_TD} Yds to Go")
        elif _ == 4 and yards_to_TD > 0:
            print(f"Turnover, {yards_to_TD} Yds to Go")
        else:
            print("TD Scored!", end=' ')

        if yards_to_TD <= 0:
            field_position = 80
            point_luck = randint(1,100)
            if point_luck > 10:
                points_scored = 7
                print("Xtra Pt Made")
            else:
                points_scored = 6
                print("No Xtra Pt")
            break
    if points_scored == 0:
        field_position = 100 - yards_to_TD
    return (points_scored, field_position)

def simulategame(num_drives, prctT1, yrangeT1, prctT2, yrangeT2):
    """Simulate a football game by running a number of drives"""
    T1_score = 0
    T2_score = 0
    yards_to_TD = 80
    if num_drives >= 1:
        for _ in range(1, num_drives):
            incr_score, yards_to_TD = drive(yards_to_TD, prctT1, yrangeT1)
            T1_score += incr_score
            incr_score, yards_to_TD = drive(yards_to_TD, prctT2, yrangeT2)
            T2_score += incr_score
    return (T1_score, T2_score)
