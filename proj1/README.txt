Jonathan Loyd
CSE590-59

No optional components were completed for the implementation of this homework.
The functions all reside in hw1.py, and hw1test.py is a script used to
test the functionality of all of the functions in hw1.py. To test them, simply
run 'python3 hw1test.py' in the directory where the files are located.

The down function checks if a random integer from 1 to 100 is greater than
successprct. If the random number is greater, 0 is returned, otherwise a random
integer from the minimum yardrange to the maximum is returned.
The drive function will run a down up to 4 times by decrementing yards_to_TD by
the return value of the down function. If yards_to_TD is less than or equal to 0
yards_to_TD is reset to 80, and a chance at an extra point is given. If a point
is scored (a touchdown) then the break function stops the loop. If no point
is scored, then the field position is reset using 100 - yards_to_TD.
The drive_depicted function does the same thing as drive, but it tries to
replicate the ASCII art given as an example. It does this by building a string
to later join and print out to the user based on yards_to_TD. It then prints
out a little message for the down and yards to go, a touchdown, or if there is
a turnover. It also prints out if an extra point was made.
The simulategame function simulates a football game and will check if the
number of drives is at least 1. If it is, then in the range of 1 to the chosen
number, the score and yards_to_TD will be adjusted based on the return values
from the drive function for Team 1, then Team 2, and this is repeated until then
number of drives has been hit, and then the function returns the score of Team 1
and Team 2.
