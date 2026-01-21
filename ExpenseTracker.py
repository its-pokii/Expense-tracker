import time

choix =0
Categories= []
Entries = []

def menu():
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


def show_categories():
    print("Categories: ", Categories)

def addCategories(NewElement):
    Categories.append(NewElement)
    Entries.append([0])
    print('Category added : ', NewElement)

def removeCategories(Element):
    print("Categories: ", Categories)
    if Element in Categories:
        Categories.remove(Element)
        print("Category removed: ", Categories)

def AddEntries(indice,element):
    Entries[indice].append(element)
    print('Entry added : ', element)

def RemoveEntries(indice,element):
    if element in Entries[indice]:
        Entries[indice].remove(element)
        print('Entry removed : ', element)

while choix!=7:
    menu()
    choix = int(input("Enter your choice: "))
    if choix == 1:
        show_categories()
        time.sleep(1)


    elif choix == 2:
        newElement = input("Enter Category you want to add: ")
        addCategories(newElement)
        time.sleep(1)
    elif choix == 3:
        Element = input("Enter Category you want to remove: ")
        removeCategories(Element)
        time.sleep(1)
    elif choix == 4:
        show_categories()
        indices = input("select your category: ")
        if indices in Categories:
            ind = Categories.index(indices)
            print(Entries[ind])
        else:
            print("Invalid choice")
            time.sleep(2)

    elif choix == 5:
        show_categories()
        indices = input("select your category: ")
        if indices in Categories:
            ind = Categories.index(indices)
            NewEntry = input("Enter Entry you want to add: ")
            AddEntries(ind, NewEntry)
        else:
            print("Invalid choice")
            time.sleep(2)
    elif choix == 6:
        show_categories()
        indices = input("select your category: ")
        if indices in Categories:
            ind = Categories.index(indices)
            Entry = input("Enter Entry you want to remove: ")
            RemoveEntries(ind, Entry)
        else:
            print("Invalid choice")
            time.sleep(2)