'''
@Author: Javeed
@Date: 2021-08-25
@Last Modified by: Javeed
@Last Modified time: 2021-08-25 22:14:09
@Title : Calculate Daily Employee Wage 
'''
import random
class EmployeeWage:
        print ("\nWelcome to the Employee Wage Computation\n")

        def emply_wage_presence():
            """
            Description:
                Function description to Calculate the Daily Employee Wage 
            Return:
                Wage of an Employee per day
            """
            # constant variables
            wage_per_hour = 20
            full_time = 1
            part_time = 2
            
            #Variables
            working_hours = 0
            wage = 0
            
            #Random selection for Full_time & Part_time
            check = random.randint(1,3)

            #Conditions
            if check == full_time:
                print ("Employee worked for Full-Time")
                working_hours = 8
            elif check == part_time:
                print ("Employee worked for Part-Time")
                working_hours = 4
            else:
                print ("Employee is absent")

            #Calculation
            try:
                wage = wage_per_hour *working_hours
                print ("Wage of an Employee :",wage," $")
                #checking the Exceptions
                if wage == 0:
                    print (wage+'$')
            except:
                print ("Error at try method Error: printing of invalid varibles")

if __name__ == '__main__':
    EmployeeWage.emply_wage_presence()