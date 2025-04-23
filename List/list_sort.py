#sorting list items

n = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34] 
 
for i in range(len(n)): 
    for j in range(i + 1, len(n)): 
 
        if (n[i] > n[j]): 
           n[i], n[j] = n[j], n[i] 
 
print (n) 