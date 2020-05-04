def gray_code(int1):
    '''Function to return the possible binary length combinations of an integer'''
    try:
        if isinstance(int1, float):
            return TypeError("Input is a float. Function only takes an integer")
        elif isinstance(int1, str):
            return TypeError("Input is a string. Function only takes an integer")
        elif int1 <= 0:
            return []
        elif int1 == 1:
            return ['0', '1']
        ans = gray_code(int1-1)
        return(['0' + i for i in ans] + ['1' + i for i in ans[::-1]])
    except NameError as e:
        print('Enter a valid integer input')


print(gray_code(3))
