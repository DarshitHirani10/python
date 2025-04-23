def calc_avg(a, b, c):
    sum = a+b+c
    avg = sum/3
    return avg

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

avg_n = calc_avg(a, b, c)
print(avg_n)