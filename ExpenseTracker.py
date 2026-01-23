import time

choix =0
Categories= []
Entries = []
Prices = []

f = open("Data.txt",'r+')
info_lines = f.readlines()
for line in info_lines:
    details = line.split("|")
    print(details)
    if details[0] in Categories:
        ind = Categories.index(details[0])
        Entries[ind].append(details[1])
        Prices[ind].append(details[2])
    else:
        Categories.append(details[0])
        Entries.append([0])
        Prices.append([0])
        ind = Categories.index(details[0])
        Entries[ind].append(details[1])
        Prices[ind].append(details[2])

def menu(): #this is the memu bar shown in the beginning
    print("===============================")
    print("Welcome to the Expense Tracker")
    print("===============================")
    print("1. Show Categories")
    print("2. Add Categories")
    print("3. Remove Categories")
    print("4. Show Entry")
    print("5. Add Entry")
    print("6. Remove Entry")
    print("7. Close")
    print("===============================")


def show_categories(): #to show the categories
    print("Categories: ", Categories)

def addCategories(NewElement): #to add a new category
    Categories.append(NewElement)
    Entries.append([0])
    Prices.append([0])
    print('Category added : ', NewElement)


def removeCategories(Element): #to remove the categories I don't want
    print("Categories: ", Categories)
    if Element in Categories:
        Categories.remove(Element)
        print("Category removed: ", Categories)

def AddEntries(indice,element,price): #to add new entries
    Entries[indice].append(element)
    Prices[indice].append(price)
    print('Entry added : ', element, " with price : ", price)
    category = Categories[indice]
    f.write(category)
    f.write("|")
    f.write(element)
    f.write("|")
    f.write(price)
    f.write("|")
    f.write("\n")

def RemoveEntries(indice,element):#to remove the entries
    if element in Entries[indice]:
        Entries[indice].remove(element)
        Prices[indice].remove(element)
        print('Entry removed : ', element)

while choix!=7: #to close when I click 7
    menu()
    choix = int(input("Enter your choice: "))

    if choix == 1: #1.show categories
        show_categories()
        time.sleep(1)


    elif choix == 2: #2.Add Category
        newElement = input("Enter Category you want to add: ")
        addCategories(newElement)
        time.sleep(1)
    elif choix == 3: #3.Remove Category
        Element = input("Enter Category you want to remove: ")
        removeCategories(Element)
        time.sleep(1)

    elif choix == 4: #4.Show Entry
        show_categories()
        Categ_indices = input("select your category: ")
        if Categ_indices in Categories:
            ind = Categories.index(Categ_indices) #to get the index of the category
            print(Entries[ind])
        else:
            print("Invalid choice")
            time.sleep(2)

    elif choix == 5: #5.Add Entry
        show_categories()
        Categ_indices = input("select your category: ")
        if Categ_indices in Categories:
            ind = Categories.index(Categ_indices)
            NewEntry = input("Enter Entry you want to add: ")
            NewPrice = input("Enter Price: ")
            AddEntries(ind, NewEntry, NewPrice)
        else:
            print("Invalid choice")
            time.sleep(2)
    elif choix == 6: #6. Remove Entry
        show_categories()
        Categ_indices = input("select your category: ")
        if Categ_indices in Categories:
            ind = Categories.index(Categ_indices)
            Entry = input("Enter Entry you want to remove: ")
            RemoveEntries(ind, Entry)
        else:
            print("Invalid choice")
            time.sleep(2)

f.close()