import os
os.umask(0)
with open(os.open('permit.txt',os.O_CREAT|os.O_WRONLY,0o777),'w') as fo:
    fo.write('permit approve')