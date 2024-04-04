"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """

    while front_is_clear():
        move()
        jump()
    while not front_is_clear():
        jump()

def jump():
    """
    pre-condition:　Karel is on the left side wall,facing East
    post-condition: Karel is on the right side of the wall
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition: Karel is on the left side of thr wall,facing East
    """
    while not front_is_clear():
        turn_left()
        move()
        for i in range(3):
            turn_left()


def cross():
    move()
    for i in range(3):
        turn_left()


def down():
        while front_is_clear():
            move()
        turn_left()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
