"""
ENGR 221 - Lab 6
Author: Kenneth Tabilas
Date: October 189, 2024
"""

import random  
import time

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)

def rwsteps(start, low, hi):
    """ rwsteps models a random walker which
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
          
        rwsteps returns the # of steps taken 
        when the walker reaches an edge
    """
    walkway = "_"*(hi-low)    # create a walkway of underscores
    S = (start-low)           # this is our sleepwalker's location, start-low

    walkway = walkway[:S] + "S" + walkway[S:]  # put our sleepwalker, "S", there

    walkway = " " + walkway + " "              # surround with spaces, for now...

    print(walkway, "    ", start, low, hi)     # print everything to keep track...
    time.sleep(0.05)

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        return 0
    
    else:
        newstart = start + rs()                # takes one step, from start to newstart
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses for the rest!

def rwstepsLoop(start, low, hi):
    steps = 0 
    current_position = start 
    while low < current_position < hi:
        # Create and print the walkway before each step
        walkway = "_" * (hi - low)
        S = (current_position - low)
        walkway = walkway[:S] + "S" + walkway[S:]
        walkway = " " + walkway + " "
        print(walkway, "  ", current_position, low, hi)

        current_position += rs()
        steps += 1

    # Print final state when the walker reaches an edge
    walkway = "_" * (hi - low)
    if current_position <= low:
        walkway = "S" + walkway[1:]  # Walker is at the low boundary
    elif current_position >= hi:
        walkway = walkway[:(hi - low)] + "S"  # Walker is at the high boundary
    walkway = " " + walkway + " "
    print(walkway, "  ", current_position, low, hi)

    return steps


if __name__ == '__main__':
  print(rwstepsLoop(5, 0, 10))  # Expected: some random number of steps
print(rwstepsLoop(0, 0, 10))  # Expected: 0 steps (already at the boundary)
print(rwstepsLoop(10, 0, 10))  # Expected: 0 steps (already at the boundary)
 