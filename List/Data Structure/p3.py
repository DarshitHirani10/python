# Exercise 3: Slice list into 3 equal chunks and reverse each chunk

l1=[12,23,43,21,4,3,7,65,15]
chunk=len(l1)//3
start=0
end=chunk
for i in range(3):
    
    print('chunk list',i+1,l1[start:end])
    print("after reverse it",list(reversed(l1[start:end])))
    start=end
    end+=chunk