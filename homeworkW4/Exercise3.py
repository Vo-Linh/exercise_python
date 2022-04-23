
def cost(timeUse):
    '''
    timeUse have unit minute
    '''

    x = 25000
    if (timeUse <= 50):
        x += timeUse * 600
        return x 
    if (timeUse <= 200):
        x += (timeUse - 50)* 400 + 50 * 600
        return x
    x += (timeUse - 200) * 200 + 50 * 600 + 150 * 400
    return x

print(cost(2100))