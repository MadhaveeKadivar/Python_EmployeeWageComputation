
'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-12 12:55:01
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-12 6:10:49
    @Title : Employee Wage Computation
'''
# Importing random modules
import random

# Declaring variables
wagePerHour = 20
empWorkHour = empDailyWage = totalMonthWage = empTotalHour = empTotalWorkDays = 0
# Checking that employee is present for full time , part time or absent
def PresentForFullTime():
    """ 
        Description: 
            This function is set employee work hours as 8 for full time presence of employee
        Parameter:
            None
        Return:
            Nothing
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
            Nothing
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
            Nothing
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
while(empTotalHour<=100 and empTotalWorkDays<20):
    check = random.randint(0,2)
    result = SwitchCase(check) # Calling function for cases
    empDailyWage = result * wagePerHour; # Calculating employee daily wage based on work hours
    totalMonthWage += empDailyWage # Adding daily wage to total wages
    empTotalWorkDays += 1
    empTotalHour += result
    
if (empTotalHour > 100): # Checking that hours are more than 100 or not
    a = empTotalHour - 100
    empTotalHour -= a
    wage = a * wagePerHour # Calculate extra hours wage
    totalMonthWage -= wage; # Minus extra hours wage from emp total wage
    
print(f"Employee total working days  : {empTotalWorkDays}")
print(f"Employee total working hours  : {empTotalHour}")
print(f"Employee Total Month Wage : {totalMonthWage}")
