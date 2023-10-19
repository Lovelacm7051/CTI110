   # This program calculates and displays travel expenses   

   # 10/19/2023

   # CTI-110 P2HW1 - Travel

   # Michael Lovelace

print('This program calculates and displays travel expenses')
user_budget = float(input('Enter Budget: '))
user_destination = input('Enter your travel destination: ')
user_gas = float(input('How much do you think you will spend on gas? '))
user_hotel = float(input('Approximately, how much will you need for accomodation/hotel? '))
user_food = float(input('Last, how much do you need for food? '))       
print('------------Travel Expenses------------')
print('Location:           ', user_destination)
print('Initial Budget:     ', '$', user_budget)
print('Fuel:               ', '$', user_gas)
print('Accomodation:       ', '$', user_hotel)
print('Food:               ', '$', user_food)
print('---------------------------------------')

print('Remaining Balance:  ', '$', user_budget - user_gas - user_hotel - user_food)




