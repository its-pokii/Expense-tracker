choix =0
Categories= []

def menu():
    print("===============================")
    print("Welcome to the Expense Tracker")
    print("===============================")
    print("1. Show Categories")
    print("2. Add Categories")
    print("3. Remove Categories")
    print("4. Add Entry")
    print("5. Close")
    print("===============================")


def show_categories():
    print("Categories: ", Categories)

def addCategories(NewElement):
    Categories.append(NewElement)
    print('Category added : ', NewElement)

def removeCategories(Element):
    print("Categories: ", Categories)
    if Element in Categories:
        Categories.remove(Element)
        print("Category removed: ", Categories)



while choix!=5:
    menu()
    choix = int(input("Enter your choice: "))
    if choix == 1:
        show_categories()

    elif choix == 2:
        newElement = input("Enter Category you want to add: ")
        addCategories(newElement)
    elif choix == 3:
        Element = input("Enter Category you want to remove: ")
        removeCategories(Element)




