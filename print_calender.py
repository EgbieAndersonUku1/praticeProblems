###############################################################################
# Author: Egbie
#
"""
Problem taking from Data Structures and Algorithms - Rance D. Necaise_1020 book

problem 1:3

Implement a function or methods that accepts a Date
and prints a calendar for the month of the given date. For example, if the
Date passed to the function contained the date 11/5/2007, the function
should print the entire calender for february. If no date is given then it
should default to the current month.

"""
###############################################################################

from datetime import datetime
from time import sleep

class Calender(object):
    """Calender(class). The user inputs a given date and Calender displays
       the date along with month in a calender format
    """
    def __init__(self, year=None, month=None, day=None):
        self._year = year
        self._month = month
        self._day = day
        date = datetime.now()

        # if any default values are None then the current month is used.
        if year != None or month != None or day != None:
            date_obj = date.replace(year=self._year, month=self._month, day=1)
        else:
            date_obj = date.replace(year=date.year, month=date.month, day=1)
            self._year, self._month, self._day = date.year, date.month, 1 # initialise dates
        self._day = date_obj.strftime("%A")      # get what day the first day of the month lands on.
        self.rows = self._make_calender_rows()  # create the rows for the calender.
        self._make_calender()                   # make the calender.

    def is_leap_year(self):
        """Returns True if the year is a leap year"""
        return self.get_year() % 4 == 0 and (self.get_year() % 100 != 0 or \
               self.get_year() % 400 == 0)

    def _month_to_str(self, month):
        """Returns the month in string format"""
        months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
                  7:'July', 8:'August', 9:'September', 10:'October', 11:'November',
                  12:'December'}
        return months.get(int(month))

    def get_month(self, to_str=False):
        """get_month(str) -> returns(int or str)

        If to_str flag is set to False returns an integer that
        represents the month. For example the number '1' would be
        represented by January and the number '12' would be represented
        by December.

        If the to_str flag is set to True returns the
        string representation of the months. Example the number '1'
        would return January.

        :parameters
           - to_str: A flag that represents whether a string should
                     be returned instead of an integer.

        cal = Calender(2016, 1, 5)
        >>> cal.get_month()
        1
        >>> cal.get_month(True)
        January
        """

        return self._month_to_str(self._month) if to_str else self._month

    def get_day(self):
        """return the day"""
        self._day

    def get_year(self):
        """return the year"""
        return self._year

    def get_max_days_in_month(self):
        """returns the maximum day in a month"""
        months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,
                 11:30, 12:31}

        # if the year is leap year and the month is feb then return 29 days
        # else return 28 days
        if self.get_month() == 2 and self.is_leap_year():
            return 29
        return months.get(self._month)

    def _make_calender_rows(self):
        """A private method that creates the rows for the calender"""
        return [['' for i in range(7)] for i in range(5)]

    def get_day_pos(self):
        """get_day_pos(str->optional) -> return(None)

        Returns a number between 0-6 that corresponding to that day.
        0 is sunday and 6 is saturday.

        >>> calender = Calender(2007, 11, 5)
        >>> calender.get_day_pos()
        >>> 4
        """
        days = {"Sun":0, "Mon":1, "Tue":2, "Wed":3, "Thu":4, "Fri":5, "Sat":6}
        return days.get(self._day[:3].title())

    def _make_calender(self):
        """A private function that makes the calender """

        idx = self.get_day_pos() # get the index position for the column
        days, max_days = 1, self.get_max_days_in_month() # max days equal maximum days in the month.

        for row in range(5):
            for col in range(7):
                self.rows[row][idx] = str(days)
                idx += 1
                days += 1
                if idx == 7: # if index equals the end of the column reset index back to 0.
                    idx = 0
                    break
                if days == max_days+1: # if days equal the max days break out of program.
                    break

    def day_to_string(self):
        """day_to_string(void) -> returns(str)
        Takes a day expressed as an integer and returns its string reprsentation.
        """
        return self._day.title()

    def display_calender(self):
        """display_calender(void) -> return(None)

        Display a calender to the output screen.
        """
        print('[+] Displaying calender....')
        sleep(0.1)
        print("\n{} {} {} {}".format('#'*13, self.get_month(True), self.get_year(), '#'*14))
        print("{:>9}{:>7}{:>6}{:>6}{:>6}{:>8}{:>9}".format("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))
        pos = 0
        for row in self.rows:
            for day in row:
                if day == '':
                    print('{:2}'.format(day), end='')
                if len(str(day)) == 1:
                    print("{:>9}".format(day), end='')
                else:
                    print("{:>8}".format(day), end='')
                pos += 1
                if pos == 7:
                    pos = 0
                    print()
