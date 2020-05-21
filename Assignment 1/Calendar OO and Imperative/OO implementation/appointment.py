from week import *
from day import *
import re
class Appointment:

    def __init__(self, start_time = 0, end_time= 0):
        self.start_time = start_time
        self.end_time = end_time

        self.d = Day()
        self.w = Week()

    def is_valid_format(self, n):
        valid_form = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')
        return bool(valid_form.match(n))




    def add_app(self, start_time, end_time, d):


        if self.d.valid_day(d) == True and self.is_valid_format(start_time) ==True and self.is_valid_format(end_time) == True:
            st_en = [start_time, end_time]
            return self.w.week[d].append('-'.join(st_en))
        else:
            return False
    def rem(self, start_time_end_time, d):
        if self.d.valid_day(d) == True:
            if start_time_end_time in self.w.week[d]:
                self.w.week[d].remove(start_time_end_time)
                return print('You have removed the following appointment %s' %start_time_end_time)
            else:
                return False
        else:
            return False
