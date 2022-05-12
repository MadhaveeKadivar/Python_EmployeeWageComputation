
'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-12 12:55:01
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-12 4:00:00
    @Title : Employee Wage Computation
'''
# Importing random modules
import random
# Declaring variables
wagePerHour = 20
empWorkHour = 0
empDailyWage = 0
totalMonthWage = 0
# Checking that employee is present for full time , part time or absent
for day in range(20):
    check = random.randint(0,2)
    if(check == 1):
        print("Employee is Present for Full time")
        empWorkHour = 8
    elif(check == 2):
        print("Employee is Present for Part time")
        empWorkHour = 4
    else:
        print("Employee is Absent")
        empWorkHour = 0
    empDailyWage = empWorkHour * wagePerHour; # Calculating employee daily wage based on work hours
    totalMonthWage += empDailyWage # Adding daily wage to total wages
print(f"Employee total month wage for 20 days is : {totalMonthWage}")