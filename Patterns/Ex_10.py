# n = 5
# p = 65

# for i in range (n):

#     for j in range (i, n):
#         print(" ", end=" ")

#     for j in range (i):
#         print(chr(p), end=" ")
#         p += 1

#     for j in range (i+1):
#         print(chr(p), end=" ")
#         p += 1
    
#     print()




    
n = 5 
p = 1

for i in range(n): 
   
   for j in range(i, n): 
      print(' ', end=' ') 

   for j in range(i):
      print(p, end=' ')
      p+=1

   for j in range(i+1):
      print(p, end=' ')
      p+=1

   print('')