import os

folder = r'R:\programs\file handling\\'
count = 1

for file_name in os.listdir(folder):
    source = folder + file_name

    destination = folder + "p" + str(count) + ".py"

    os.rename(source, destination)
    count += 1
print('All Files Renamed')

print('New Names are')
# verify the result
res = os.listdir(folder)
print(res)