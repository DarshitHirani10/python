with open('new.txt','a') as fo:
    fo.write('\nappend new line')
with open('new.txt','r+') as fo:
    print(fo.read())
    fo.write('add new content')