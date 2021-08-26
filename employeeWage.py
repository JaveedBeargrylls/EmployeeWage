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
working_days = 20
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
                Function description to Calculate the Monthly Wage
            Return:
                Wage of an Employee per Month
            """
            #switcher

            #Variables
            working_hours = 20
            emply_wage = 0
            total = 0
            count = 0
            f_time = 0
            p_time = 0
            #wage = 0
            
            #Calculation
            for i in range (working_days):
                check = random.randint(1,3)
                wage = switch_statement(check)
                if (wage == 8):
                    #print ("Full-Time Employee wage per day")
                    emply_wage = wage*working_hours
                    f_time = f_time + 1
                elif ( wage == 4):
                    # print ("Part-Time Employee wage per day")
                    emply_wage = wage*working_hours
                    p_time = p_time + 1
                else:
                    # print("Employe is Absent")
                    count = count + 1 # count to know the Absent days of an employee
                total = total + emply_wage
            print ("Total Working days is :",working_days)
            print ("Employee worked for full time :",f_time,"days")
            print ("Employee worked for part time :",p_time,"days")
            print ("Employee is absent for ",count,"days")
            print ("Monthly wage of an Employee : ",total,"$")

if __name__ == '__main__':
    emply_wage_presence()