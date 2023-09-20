my_sportlist = ["Football", "Basketball"]
favouritesport = input("What is your favourite sport ? ")
my_sportlist.append(favouritesport)
my_sportlist.sort()
print(my_sportlist)
schoolsubjects = ["science", "computer science","maths","biology","economics"]
print(schoolsubjects)
dislikedsubject = input("which of these subjects do you dislike ? ")
schoolsubjects.remove(dislikedsubject)
print("Your New list is",schoolsubjects)