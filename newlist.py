#Sinead and Abby
#1-10-24
#list

#initialize

#functions

#main
def movieList():
    movielist = []
    while True:
        choice = input("What would you like to do? 1 - add, 2- view, 3 - mark as complete, 4- remove, 5- exit, 6 - clear list, 7 - alphabetalize, 8 - list # of items")
        if choice == "1":
            ListItem = input("What do you want to add to the list? ")
            movielist.insert(0,ListItem)
        elif choice == "2":
            print(movielist)
        elif choice == "3":
            ans = input("Please enter movie to change: ")
            i = movielist.index(ans)
            movielist[i] = ans + " complete!!"
            print(i)
        elif choice == "4":
            RemoveListItem = input("What item would you like to remove? ")
            movielist.remove(RemoveListItem)
        elif choice == "6":
            movielist.clear()
        elif choice == "7":
            movielist.sort(key=str.lower)
            print(movielist)
        elif choice == "8":
            print(len(movielist))
        elif choice == "5":
            break

#main
movieList()