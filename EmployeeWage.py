'''
    @Author: Madhavee Kadivar
    @Date: 2022-05-12 12:55:01
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-05-13 1:01:19
    @Title : Employee Wage Computation
'''
# Importing random modules
import random
import logging

# Logging
logging.basicConfig(filename = 'file.log',format = '%(asctime)s | %(levelname)s | %(lineno)d: %(message)s')
logger = logging.getLogger("root_logger")
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
log_format = '%(message)s'
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)

#Declaring variables
wagePerHour = 20
empWorkHour = empDailyWage = totalMonthWage = empTotalHour = empTotalWorkDays = 0
dict = {}
day = 1
# Checking that employee is present for full time , part time or absent
def get_work_hours(check):
    """ 
        Description: 
            This function is calculating workhours based on employee attendence
        Parameter:
            It takes one integer as argument
        Return:
            returns employee work hours for one day 
    """
    if(check == 1):
        result = random.randint(0,1)
        if(result == 0):
            logger.debug("Employee is Present for Part time")
            empWorkHour = 4
        else:
            logger.debug("Employee is Present for Full time")
            empWorkHour = 8
    else:
        logger.debug("Employee is Absent")
        empWorkHour = 0
    return empWorkHour

while(empTotalHour<=100 and empTotalWorkDays<20):
    check = random.randint(0,1)
    empWorkHour = get_work_hours(check) # Calling function to get work hours
    if(empWorkHour == 8 or empWorkHour == 4):
        empTotalWorkDays += 1
    empDailyWage = empWorkHour * wagePerHour; # Calculating employee daily wage based on work hours
    totalMonthWage += empDailyWage # Adding daily wage to total wages
    empTotalHour += empWorkHour
    dict[day] = empDailyWage 
    day +=1  
if (empTotalHour > 100): # Checking that hours are more than 100 or not
    a = empTotalHour - 100
    empTotalHour -= a
    wage = a * wagePerHour # Calculate extra hours wage
    totalMonthWage -= wage; # Minus extra hours wage from emp total wage

print(" Day  : DailyWage")
for i in sorted (dict) : # sorting dictionary by key
    logger.info(f"Day {i} : {dict[i]}")
logger.info(f"Employee total working days  : {empTotalWorkDays}")
logger.info(f"Employee total working hours  : {empTotalHour}")
logger.info(f"Employee Total Month Wage : {totalMonthWage}\n\n")
