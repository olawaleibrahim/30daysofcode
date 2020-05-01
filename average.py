def get_average(string):
    sum = 0
    new = []
    for i in string.split(' '):
        new.append(int(i))
    for i in new:
        sum = sum + i
    print(f'The average of the numbers is {sum/(len(new))}')
    

get_average('12 34 67')
