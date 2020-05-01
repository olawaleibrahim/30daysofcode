def get_average(string):
    try:
        sum = 0
        sum_list = []
        for i in string.split():
            sum_list.append(int(i))
        for i in sum_list:
            sum = sum + i
        print(f'The average of the numbers is {sum/(len(sum_list))}')
    except SyntaxError:
        print('Wrap inputs in parenthesis')
    except ValueError:
        print(sum_list)
        print('Enter a valid string of numbers only')


get_average('34 3 45')
