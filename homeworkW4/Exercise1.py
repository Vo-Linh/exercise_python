from math import sqrt

def quadratic_equation_2(a, b, c):
    '''
    aX^2 + bX + c = 0
    '''
    if (a == 0):
        if (b == 0):
            print("The equation has no solution")
        else:    
            return -c/b

    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        return x1, x2
    elif delta == 0:
        x = -b/(2*a)
        return x

    print('The equation has no solution')


x1, x2 = quadratic_equation_2(3, 4, -7)

print(x1, x2)