fo=open('new.txt','w')
fo.write('this is new file')
fo=open('new.txt','r')
print(fo.read())
fo.close()
import os
# print(os.listdir())
# print(os.path.isfile('new.txt'))