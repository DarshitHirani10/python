# Exercise 11: Print all prime numbers within a range
start=int(input('Enter a start: '))
end=int(input('Enter a end: '))
fct=True
for i in range(start,end+1):
    fct=True
    for j in range(2,i//2+1):
        if i%j==0:
            fct=False
            break
    if fct!=False:
        print(i)