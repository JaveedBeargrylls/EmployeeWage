'''
@Author: Javeed
@Date: 2021-08-25
@Last Modified by: Javeed
@Last Modified time: 2021-08-25 21:14:08
@Title : Random presence of employee 
'''
import random
class EmployeeWage:
    def emply_wage_presence():
        """
        Description:
            Function description to print the Attendance of Employee using random function 
        Return:
            The precence of Employee either absent or present
        """
        print ("\nWelcome to the Employee Wage Computation\n")

        # Used RANDOM for Attendance
        precence = random.randint(0,1)
        try:
            #print (precence)
            if precence == 0:
                print ("Employee is Present")
            else :
                print ("Employee is absent")
        except:
            print(" Error in Precence Check ")
        
if __name__ == '__main__':
    EmployeeWage.emply_wage_presence()