# import random
# import string

# pass_len = 12
# charvalues = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range (pass_len):
#     password += (random.choice(charvalues))

# print("Your Random Password Is: ", password)

#-----------------------------------------------------------------------------------------

import random
import string

pass_len = 12
charvalues = string.ascii_letters + string.digits + string.punctuation

# list comprehension [function for i in range(n)]

password = ".".join([random.choice(charvalues) for i in range(pass_len)])

print("Your Random Password Is: ", password)