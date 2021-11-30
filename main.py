import curses       # Used to style the terminal which will allow us to make the game more interactive
from curses import wrapper      # Makes sure that everything we do on the terminal will be back to the way it was after our program is over

def start_screen(stdscr):       # Creating the start screen for the game
    stdscr.clear()      # To remove all the default writing from the terminal
    stdscr.addstr("Welcome to the Typing Speed Game!")      # Pretty much a print statement that will print a default message onto the terminal, with the pair colour
    stdscr.addstr("\nPress any key to start...")
    stdscr.refresh()
    stdscr.getkey()     # To get input from the user, we use it here so that early on if we run it then it will print 'Hello' and then instantly close, now it has to wait for user input before closing

def main(stdscr):       # The parameter 'stdscr' is the standard output which will put a screen over the terminal which will allow us to write on to it
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

wrapper(main)