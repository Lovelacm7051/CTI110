mileage = float(input())
cost = float(input())

cost_20 = 20 / mileage * cost
cost_75 = 75 / mileage * cost
cost_500 = 500 / mileage * cost

print (f'{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}')
