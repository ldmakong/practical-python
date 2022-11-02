# bounce.py
#
# Exercise 1.5

ball_height = 100 
num_bounce = 0

while num_bounce < 10:
    num_bounce = num_bounce + 1
    ball_height = ball_height*3./5.
    print(round(num_bounce, 4), round(ball_height, 4))

