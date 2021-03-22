test_cases = int(input())
for i in range(0, test_cases):
    # input handling
    x_y = input().split()
    a_b = [int(i) for i in x_y]
    a = a_b[0]
    b = a_b[1]
    
    # computation
    cells = a*b
    

print(a_b)