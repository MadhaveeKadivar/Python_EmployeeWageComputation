
'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-12 12:55:01
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-12 1:30:30
    @Title : Employee Wage Computation
'''
# Importing random modules
import random
# Declaring variables
wagePerHour = 20
empWorkHour = 0
empDailyWage = 0
# Checking that employee is present or absent
check = random.randint(0,1)
if(check == 1):
    print("Employee is Present")
    empWorkHour = 8
else:
    print("Employee is Absent")
    empWorkHour = 0
# Calculating employee daily wage  
empDailyWage = empWorkHour*wagePerHour
print(f"Employee Daily wage is : {empDailyWage}")
