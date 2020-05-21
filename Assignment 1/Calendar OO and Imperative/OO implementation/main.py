from appointment import *



def main():
    a = Appointment()
    w = Week()

    x = input('Please use the following functions.\n -----------------\nadd\nremove\nprint\nhelp\nday\nend\n')
    while x !='end':
        if x == 'add':
            d = input('Please enter the day you wish to schedule your appointment\n').title()
            start_time = input('Please enter the start of your appointment in the following format HH:MM\n')
            end_time = input('Please enter the end of your appointment in the following format HH:MM\n')
            if a.add_app(start_time, end_time ,d) == False:
                print('You have supplied incorrect data please type add again to schedule an appointment')
            else:

                print('You have added a new appointment!')
        elif x == 'print':
            print('---Here is your week---')

            w.week_str()


        elif x == 'day':
            n = input('Please enter the day you would like to see\n').title()
            print('Here are the appointments you have for %s' % n, w.week[n])
        elif x == 'remove':
            da = input('Please enter the day\n').title()
            h = input('Please enter the times you want to remove in the following format HH:MM-HH:MM\n')

            if a.rem(h, da) == False:
                print('You have supplied incorrect data and/or that appointment does not exist please type remove again to retry or print to see your week')
            else:

                pass
        elif x == 'help':
            print('Please use the following functions.\n -----------------\nadd\nremove\nprint\nhelp\nday\nend\n')




        x = input()

if __name__ == "__main__": main()
