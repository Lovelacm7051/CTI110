   # CTI-110

   # P3HW2 - Salary

   # Mike Lovelace  

   # 10/26/2023

name = input('Enter employee name: ') #first name last name no commas
hours_worked = float(input('Enter number of hours worked: ')) #hours worked as a decimel
pay_rate = float(input('Enter employee pay rate: $')) #employee's hourly pay as a decimel
overtime = float(input('Enter employee overtime: ')) #hours of overtime as a decimel
overtime_pay = pay_rate * 1.50 
reg_hour_pay = hours_worked * pay_rate
gross_pay = overtime_pay + reg_hour_pay

print('------------------------------------')
print('Employee name: ', name)
print('Hours Worked',    'Pay Rate',        'OverTime',       'OverTime Pay',            'RegHour Pay',            'Gross Pay') 
print('-----------------------------------------------------------------------------')
print(f'{hours_worked:<13.2f}{pay_rate:5.2f}{overtime:10.2f} {overtime_pay:10.2f} {reg_hour_pay:7.2f} {gross_pay:8.2f}')
print('_____________________________________________________________________________')
