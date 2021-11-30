import curses       # Used to style the terminal which will allow us to make the game more interactive
from curses import wrapper      # Makes sure that everything we do on the terminal will be back to the way it was after our program is over

def start_screen(stdscr):       # Creating the start screen for the game
    stdscr.clear()      # To remove all the default writing from the terminal
    stdscr.addstr("Welcome to the Typing Speed Game!")      # Pretty much a print statement that will print a default message onto the terminal, with the pair colour
    stdscr.addstr("\nPress any key to start...")
    stdscr.refresh()
    stdscr.getkey()     # To get input from the user, we use it here so that early on if we run it then it will print 'Hello' and then instantly close, now it has to wait for user input before closing

def wpm_test(stdscr):       # This is going to be our game concept where we get the user to type our given sentance
    target_text = "random"
    current_text = []

    while True:     # Here we are saying that while the user is typing, append(add) that key onto the screen using the color pair stated
        stdscr.clear()      # This clear method is needed here because otherwise all the perious data we had on screen would be duplicated over and over
        stdscr.addstr(target_text)
    
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:      # Making sure the user can exit the program so, if the key 'escape'(27 is its ASCII representation) is pressed then break out of the loop
            break

        current_text.append(key)


def main(stdscr):       # The parameter 'stdscr' is the standard output which will put a screen over the terminal which will allow us to write on to it
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)