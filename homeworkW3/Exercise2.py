N = float(input('Enter scores: \n'))

def evaluate(a):
    
    if (a >= 9.0):
        return "Rank A"
    if (a >= 7.0):
        return "Rank B"
    if (a >= 5.0):
        return "Rank C"
    return "Rank F"

print(evaluate(N))