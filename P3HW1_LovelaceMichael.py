# Debugging Assignment
# Lovelace


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
# chnages int to float as your average will be a float if you use numbers like 88,87,88,87,88,87
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
# add mod_6 into your list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades


low = min(grades)
high = max(grades)
# changes variable name to sum1 as you cannot name a variable a function name like sum()
sum1 = sum(grades)

# here you need to sum the lsit and then divide by the length the list
# avg would be avg = sum(grades) / len(grades)  # do not use 6 as you will revists this problem in the future and we will remove the lowest value
#avg = avg(grades)
avg = sum1 / len(grades)


print('-------------Results--------------')
print('Lowest Grade: ', min(grades))
print('Highest Grade: ', max(grades))
print('Sum of Grades: ', sum1)
print('Average: ', avg)
print('------------------------------------')

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
elif (avg >= 80) and (avg <= 89):
    print('Your grade is: B')
elif (avg >= 70) and (avg <=79):
    print('Your grade is a C')
elif (avg >=60) and (avg <=69):
    print('Your grade is a D')
else:
    print('Your grade is: F') # TO DO: finish this





