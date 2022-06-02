
'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-12 12:55:01
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-12 1:49:00
    @Title : Employee Wage Computation
'''
# Importing random modules
import random
# Declaring variables
wagePerHour = 20
empWorkHour = 0
empDailyWage = 0
# Checking that employee is present for full time , part time or absent
check = random.randint(0,2)
if(check == 1):
    result = random.randint(0,1)
    if(result == 0):
        print("Employee is Present for Part time")
        empWorkHour = 4
    else:
        print("Employee is Present for Full time")
        empWorkHour = 8
else:
    print("Employee is Absent")
    empWorkHour = 0
    
# Calculating employee daily wage based on work hours
empDailyWage = empWorkHour*wagePerHour
print(f"Employee Daily wage is : {empDailyWage}")
