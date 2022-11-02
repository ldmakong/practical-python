import math
h = 0.11 * 0.001 # one dollar bill thickness in meter
H = 442  # Sears tower height in meter
num_bills = 1
day = 1

while num_bills * h < H:
    print(day, num_bills, num_bills * h)
    day = day + 1
    num_bills = num_bills * 2


duration = 1 + math.log(H/h)/math.log(2)
print('Number of days -- (formula based) : {}'.format(round(duration)))
print('Number of days : ', day)
print('Number of bills : ', num_bills)
print('Final height :', num_bills * h)
