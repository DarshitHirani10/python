while True:
    try:
        number= int(input("enter number: "))
        if 1<= number <= 108:
            break
        print("invalid number, please enter number between 1 to 108")
    except ValueError:
        print("invalid input, please enter a number")
#--------------------------------------------------------------------------------------

window_li = [1]
n = 12
for i in range(1, 10):
    ans = n * i
    if ans <= 108:  
        window_li.append(ans)
    front = ans + 1
    if front <= 108:
        window_li.append(front)

n = 6
for i in range(1,18):
    if i%2 != 0:
        ans1 = n * i
        # print(ans1)
        window_li.append(ans1)

        front1 = ans1 + 1
        # print(front1)
        window_li.append(front1)   
# print(li)

#--------------------------------------------------------------------------------------

middle_li_1 = []
for i in range(2, 99, 12):  
    if i + 9 <= 108:  
        middle_li_1.append((i, i + 9))

middle_li_2 = []
for i in range(5, 105, 12):
    if i + 3 <= 108:
        middle_li_2.append((i, i + 3))

middle_pair = middle_li_1 + middle_li_2
# print(middle_pair)

#--------------------------------------------------------------------------------------

aisle_li_1 = []
for i in range(3, 100, 12):  
    if i + 7 <= 108:  
        aisle_li_1.append((i, i + 7))

aisle_li_2 = []
for i in range(4, 101, 12): 
    if i + 5 <= 108:  
        aisle_li_2.append((i, i + 5))

aisle_pair = aisle_li_1 + aisle_li_2
# print(aisle_pair)

#--------------------------------------------------------------------------------------

if number in window_li:
    index = window_li.index(number)
    if index % 2 == 0:
        pair = window_li[index + 1]
    else:
        pair = window_li[index - 1]
    print("Output: ", pair)
    print("Type: Window seat")

else:
    found = False
    # Middle seat
    for pair in middle_pair:
        if number in pair:
            if number == pair[0]:
                print("Output: ", pair[1])
            else:
                print("Output: ", pair[0])
            print("Type: Middle seat")
            # found = True
            break

    # Aisle seat
    if not found:
        for pair in aisle_pair:
            if number in pair:
                if number == pair[0]:
                    print("Output: ", pair[1])
                else:
                    print("Output: ", pair[0])
                print("Type: Aisle seat")
                # found = True
                break