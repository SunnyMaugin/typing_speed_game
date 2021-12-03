import curses       # Used to style the terminal which will allow us to make the game more interactive
from curses import wrapper      # Makes sure that everything we do on the terminal will be back to the way it was after our program is over
import time

def start_screen(stdscr):       # Creating the start screen for the game
    stdscr.clear()      # To remove all the default writing from the terminal
    stdscr.addstr("Welcome to the Typing Speed Game!")      # Pretty much a print statement that will print a default message onto the terminal, with the pair colour
    stdscr.addstr("\nPress any key to start...")
    stdscr.addstr("\n\n\nUse [ESC] to exit at any time")
    stdscr.refresh()
    stdscr.getkey()     # To get input from the user, we use it here so that early on if we run it then it will print 'Hello' and then instantly close, now it has to wait for user input before closing

def display_text(stdscr, target, current, wpm=0):
        stdscr.addstr(target)
        stdscr.addstr(1, 0, f"WPM: {wpm}")      # Displaying our wpm
    
        for i, char in enumerate(current):       # This is going to get each element in the list as well as its position then overlay it with the target text, we are also setting our current text to green
            correct_char = target[i]        # This just means if the letter typed is equal to the premade sentance letter then make it green if its not equal/same then make it red
            color = curses.color_pair(1)
            if char != correct_char:        
                color = curses.color_pair(2)
            stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):       # This is going to be our game concept where we get the user to type our given sentance
    target_text = "This is the test run for the game please try it out!"
    current_text = []
    wpm = 0
    start_time = time.time()        # This will start timing whenever the while loop starts looping until its ends
    stdscr.nodelay(True)        # Keeps the WPM going and doesnt get blocked by the 'getkey' method which has to wait until a user types a key

    while True:     # Here we are saying that while the user is typing, append(add) that key onto the screen using the color pair stated
        time_elapsed = max(time.time() - start_time, 1)     # Calculating the wpm
        wpm = round(len(current_text) / (time_elapsed / 60) / 5)

        stdscr.clear()      # This clear method is needed here because otherwise all the perious data we had on screen would be duplicated over and over
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:        # To make sure this line will not give us an error when the user does not enter a key
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:      # Making sure the user can exit the program so, if the key 'escape'(27 is its ASCII representation) is pressed then break out of the loop
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):      # If backspace is clicked by the user then remove a charater from the list, we do this because before we were entering ACTUAL backspace not its use/purpose
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):       # The parameter 'stdscr' is the standard output which will put a screen over the terminal which will allow us to write on to it
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        stdscr.addstr("You completed the text! Press any key play again or [ESC] to exit")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)