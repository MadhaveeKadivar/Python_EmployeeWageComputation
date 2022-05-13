'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-12 12:55:01
    @Last Modified by: Madhavee Kadivar
<<<<<<< HEAD
    @Last Modified time: 2022-05-12 5:45:30
=======
    @Last Modified time: 2022-05-12 6:00:25
>>>>>>> UC5_EmployeeTotalMonthWage
    @Title : Employee Wage Computation
'''
# Importing random modules
from email.policy import default
import random

# Declaring variables
wagePerHour = 20
empWorkHour = 0
empDailyWage = 0
<<<<<<< HEAD

=======
totalMonthWage =0
>>>>>>> UC5_EmployeeTotalMonthWage
# Checking that employee is present for full time , part time or absent
def PresentForFullTime():
    """ 
        Description: 
            This function is set employee work hours as 8 for full time presence of employee
        Parameter:
            None
        Return:
<<<<<<< HEAD
            Employee Work hours
=======
            Employee Work Hours
>>>>>>> UC5_EmployeeTotalMonthWage
    """
    empWorkHour = 8
    return empWorkHour
def PresentForPartTime():
    """ 
        Description: 
            This function is set employee work hours as 4 for part time presence of employee
        Parameter:
            None
        Return:
<<<<<<< HEAD
            Employee Work hours
=======
            Employee Work Hours
>>>>>>> UC5_EmployeeTotalMonthWage
    """
    empWorkHour = 4
    return empWorkHour
def Absent():
    """ 
        Description: 
            This function is set employee work hours as 0 for absence of employee
        Parameter:
            None
        Return:
<<<<<<< HEAD
            Employee Work hours
=======
            Employee Work Hours
>>>>>>> UC5_EmployeeTotalMonthWage
    """
    empWorkHour = 0
    return empWorkHour
def SwitchCase(check):
    """ 
        Description: 
            This function is used for imlementing switch case for employee attendence
        Parameter:
            This function takes one integer parameter 
        Return:
            It returns function value based on choice
    """
    switch={
       1 : PresentForFullTime(),
       2 : PresentForPartTime(),
       0 : Absent(),
    }
    return switch.get(check,"")
<<<<<<< HEAD
check = random.randint(0,2)
result = SwitchCase(check) # Calling function for cases

# Calculating employee daily wage based on work hours
empDailyWage = result*wagePerHour
print(f"Employee Daily wage is : {empDailyWage}")
=======
for day in range(20):
    check = random.randint(0,2)
    result = SwitchCase(check) # Calling function for cases

    # Calculating employee daily wage based on work hours
    empDailyWage = result*wagePerHour
    totalMonthWage += empDailyWage # Adding daily wage to total wages
print(f"Employee total month wage for 20 days is : {totalMonthWage}")

>>>>>>> UC5_EmployeeTotalMonthWage
