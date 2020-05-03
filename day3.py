''' Function to take a integer and returns its string equivalent '''


def itos(int1):
    if type(int1) == str:
        print(f'Enter an integer, {int1} is a string.')
    else:
        if isinstance(int1, float):
            raise ValueError('Input an integer not a float')
        elif isinstance(int1, int):
            print(f"'{int1}'")


# Example
itos(78)  # calling the function

''' Function to take a string of floats and return its integer equivalent '''


def stof(strg):
    if isinstance(strg, int) or isinstance(strg, float):
        print(f'Enter a string of float, {strg} is not a string')
    else:
        print(strg)


# Example
stof('45.67')  # calling the function

''' Function to take a float and return its string equivalent '''


def ftos(input):
    if isinstance(input, int) or isinstance(input, str):
        print(f'Enter a float, {input} is not a float')
    else:
        print(f"'{input}'")


# Example
ftos(78.89)  # calling the function

''' Function to take a string of float and return its float equivalent '''


def stof(strg):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if isinstance(strg, int) or isinstance(strg, float):
        print(f'Enter a string of float, {strg} is not a string')
    else:
        if '.' not in strg:
            sum1 = 0
            for i in alphabets:
                if i in strg:
                    sum1 = sum1 + 1
            if sum1 >= 1:
                print(f'Input is not a float, contains letters')
            else:
                raise ValueError('This is an integer string')
        else:
            print(strg)

stof('45.67')
