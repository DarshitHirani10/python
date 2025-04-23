with open("new.txt", "r") as fo:
    # reading the first line
    first_line = fo.readline()
    print(first_line)
    print(fo.read(7))
    for last_line in fo:
        pass
    # printing the last line
    print(last_line)
    print(fo.read(12))