#length of list

cities = ["rajkot", "ahemdabad", "pune", "mumbai", "chennai", "banglore"]
movies = ["a", "b", "c", "d"]

print(cities[0])

def calc_len(list):
    print(len(list))

calc_len(cities)
calc_len(movies)

#--------------------------------------------------------------------------------------------------------------------

def print_list(list):
    for item in list :
        print(item, end=" ")

print_list(movies)