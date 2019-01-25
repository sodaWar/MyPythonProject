from unittest import TestCase
import random
import time


class TestSolver(TestCase):
    def test(self):
        pass

    def finger_guess(self):
        while 1:
            s = int(random.randint(1,3))
            if s == 1:
                ind = "stone"
            elif s == 2:
                ind = "rock"
            elif s == 3:
                ind = "paper"
            m = raw_input('enter stone rock paper,enter"end"to end the game:')
            blist = ["stone", "rock", "paper"]
            if (m not in blist) and (m != 'end'):
                print "you entered is wrong !"
            elif (m not in blist) and (m == 'end'):
                print "\n exit ing..."
                time.sleep(1)
                break
            elif m == ind:
                print "the computer give:" + ind + ",the draw!"
            elif (m == 'stone' and ind == 'rock') or (m == 'rock' and ind == 'paper') or (
                            m == 'paper' and ind == 'stone'):
                print "the computer give:" + ind + ",you win!"
            elif (m == 'stone' and ind == 'paper') or (m == 'rock' and ind == 'stone') or (
                            m == 'paper' and ind == 'rock'):
                print "the computer give:" + ind + ",you defeate!"

if __name__ == "__main__":
    TestSolver.finger_guess()
