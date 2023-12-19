
list1 = list(input("Enter the contents of the list seperated by commas:  ").split(","))
print(list1)
alternatelist = []
alternatelist = list1[::2]
print(alternatelist)

"""
[::2]
in python means to take every second element
in this case every second element in 1,2,3,4,5,6 is
1,3,5
definition = "default start index,default stop index,stepsize is two"
"""

list2 = list(input("Enter the contents of the list seperated by commas:  ").split(","))
print(list2)
list2.reverse()
print(list2)

list3 = []
addnum = input("Enter the number you want to add to the list, to stop type 'end'  ")
while addnum != 'end':
    print(addnum)
    list3.append(int(addnum))
    addnum = input("Enter the number you want to add to the list, to stop type 'end'  ")
list3.sort()
sorted(list3)
print(list3)
largestnumber = list3[-1]
print(largestnumber)
    
    