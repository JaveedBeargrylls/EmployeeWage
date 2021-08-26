'''
@Author: Javeed
@Date: 2021-08-26
@Last Modified by: Javeed
@Last Modified time: 2021-08-26 16:41:26
@Title : Calculate Employee Wage using Switche case
'''
import random

#global variables
wage_per_hour = 20
full_time = 2
part_time = 1
wage = 0
def switch_statement(check):
    """
Description:
     Function to Switch case
Parameter:
      check is to get the random number of working_hours in emply_wage_presence function
Return:
       returning the check variable
"""
    return{
                1: 8,
                2: 4,
                0: 0,
            }.get(check)

def emply_wage_presence():
            """
            Description:
                Function description to Calculate the Daily Employee Wage F/P time
            Return:
                Wage of an Employee per day
            """
            #switcher

            #Variables
            working_hours = 20
            #wage = 0
            
            #Random selection for Full_time & Part_time
            check = random.randint(1,3)
            wage = switch_statement(check)
            if (wage == 8):
                print ("Full-Time Employee wage per day")
            elif ( wage == 4):
                print ("Part-Time Employee wage per day")
            else:
                print("Employe is Absent")
            try:
                total = wage * working_hours
                print ("Wage of an Employee :",total," $")
                #checking the Exceptions
                if wage == 0:
                    print (wage+'$')
            except:
                print ("Error employee is absent & wage is 0 ")

if __name__ == '__main__':
    emply_wage_presence()