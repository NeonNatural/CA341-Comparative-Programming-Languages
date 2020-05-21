class Week:

    def __init__(self, week = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday':[], 'Saturday': [], 'Sunday': [],}):

        self.week = week

    def week_str(self):

        for key, value in self.week.items():

                print(key, ', '.join(value))
        return print('-----------------')

    
