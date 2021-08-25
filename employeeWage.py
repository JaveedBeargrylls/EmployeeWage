'''
@Author: Javeed
@Date: 2021-08-25
@Last Modified by: Javeed
@Last Modified time: 2021-08-25 22:14:09
@Title : Calculate Daily Employee Wage 
'''
import random
class EmployeeWage:

    def emply_wage_presence():
        """
        Description:
            Function description to Calculate the Daily Employee Wage 
        Return:
            Wage of an Employee per day
        """
        print ("\nWelcome to the Employee Wage Computation\n")

        #instance Variables
        wage_per_hour = 20
        working_hours_in_day = 8
        employee = 1

        # Used RANDOM for Attendance
        precence = random.randint(0,1)
            #print (precence)
        if (precence == 0):
            wage = wage_per_hour*working_hours_in_day*employee
            print ("Employee is present")
            print ("Wage = ",wage)
        else:
            employee = 0
            wage = wage_per_hour*working_hours_in_day*employee
            print ("Employee is Absent today")
        
if __name__ == '__main__':
    EmployeeWage.emply_wage_presence()