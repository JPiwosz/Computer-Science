userage = input("Please enter your age  ")
useragenew = int(userage)
if useragenew >= 18:
    print("You can Vote")
elif useragenew == 17:
    print("You can learn to drive")
elif useragenew == 16:
    print("You can buy an lottery ticket")
elif useragenew <= 15:
    print("You can go Trick-Or-Treating")
