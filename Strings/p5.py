# Exercise 5: Count all letters, digits, and special symbols from a given string
str=input("Enter a string:")
letter=0
digit=0
symbol=0
for i in str:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
    else:
        symbol+=1
print(f'letter: {letter}, digit: {digit}, symbol: {symbol}')