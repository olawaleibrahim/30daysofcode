def termino(strg):
    strg_list = []
    sum = 0
    a = strg.split('()')
    for i in a:
        strg_list.append(i)

    for i in strg_list:
        if i != '':
            sum = sum + 1
    print(sum)


termino('()()()()')
termino(')()())()()(')
