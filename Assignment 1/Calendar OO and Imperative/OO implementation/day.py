from week import *

class Day:

    def __init__(self, day = ''):
        self.day = day
        self.w = Week()



    def valid_day(self, s):

        if s in self.w.week:
            return True


p1 = Day()
p1.valid_day('Monday')
