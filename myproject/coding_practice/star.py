line_length = 4

for x in range(1, line_length*2, 2):
    print( (" "*((line_length*2-1-x)//2)) + ("*"*x))

for y in range(line_length*2-3, 0, -2):
    print(" "*((line_length*2-1-y)//2)+ ("*"*y))
