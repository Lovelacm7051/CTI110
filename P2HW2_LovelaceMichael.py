# Debugging Assignment
# Lovelace


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
sum1 = sum(grades)
avg = sum1 / len(grades)


print('-------------Results--------------')
print('Lowest Grade: ', min(grades))
print('Highest Grade: ', max(grades))
print('Sum of Grades: ', sum1)
print('Average: ', avg)
print('------------------------------------')




