import os

from Controller import Controller
from sys import argv  #käsurealt lugemiseks

class Hangman:

    def __init__(self):
        Controller(db_name).main()


if __name__ == '__main__':
    db_name = None
    if len(argv) == 2: # kontrollime, kas on antud kaasa
        if os.path.exists(argv[1]):
            db_name = argv[1]  # new database name from command  Line
    Hangman()
