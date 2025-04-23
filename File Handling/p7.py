with open('new.txt', 'r') as fo:
    line = fo.readline()
    while line != '':
        print(line, end='')
        line = fo.readline()