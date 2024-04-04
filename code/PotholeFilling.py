"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at the(2,1)
    Post-condition: Karel is at the(2,7)
    """
    for i in range(3):
        go_in()
        put_99_beeper()
        go_out()


def go_in():
    """"
    pre-condition: Karel is at the upper and facing East
    post-condition: Karel is at the pothole facing South
    """
    move()
    for i in range(3):
        turn_left()
    move()


def go_out():
    """
    pre-condition: Karel is in the pothole and facing South
    post-condition: Karel is in the upper and facing North
    """
    for i in range(2):
        turn_left()
    move()
    for i in range(3):
        turn_left()
    move()


def put_99_beeper():
    """
    Karel will put 99 beepers
    """
    for i in range(99):
        put_beeper()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
