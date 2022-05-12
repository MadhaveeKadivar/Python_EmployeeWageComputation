
'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-12 12:55:01
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-12 4:40:26
    @Title : Employee Wage Computation
'''
# Importing random modules
import random
# Declaring variables
wagePerHour = 20
empWorkHour = empDailyWage = totalMonthWage = empTotalHour = empTotalWorkDays = 0
# Checking that employee is present for full time , part time or absent
def GetWorkHours(check):
    """ 
        Description: 
            This function is calculating workhours based on employee attendence
        Parameter:
            It takes one integer as argument
        Return:
            returns employee work hours for one day 
    """
    if(check == 1):
        empWorkHour = 8 # Employee is present for full time
    elif(check == 2):
        empWorkHour = 4  # Employee is present for part time
    else:
        empWorkHour = 0  # Employee is absent
    return empWorkHour

while(empTotalHour<=100 and empTotalWorkDays<20):
    check = random.randint(0,2)
    empWorkHour = GetWorkHours(check) # Calling function to get work hours
    empDailyWage = empWorkHour * wagePerHour; # Calculating employee daily wage based on work hours
    totalMonthWage += empDailyWage # Adding daily wage to total wages
    empTotalWorkDays += 1
    empTotalHour += empWorkHour
        
if (empTotalHour > 100): # Checking that hours are more than 100 or not
    a = empTotalHour - 100
    empTotalHour -= a
    wage = a * wagePerHour # Calculate extra hours wage
    totalMonthWage -= wage; # Minus extra hours wage from emp total wage
    
print(f"Employee total working days  : {empTotalWorkDays}")
print(f"Employee total working hours  : {empTotalHour}")
print(f"Employee Total Month Wage : {totalMonthWage}")