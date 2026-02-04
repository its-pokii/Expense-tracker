import time
import numpy as np

choix =0
second_choix = 0
Categories= []
Entries = []
Prices = []



#this function is to delete a line in the text file using the check methode "if it exist then dont write it"
def fileUpdate(string_deleted):

    with open("Data.txt", "r") as f:
        lines = f.readlines()
    with open("Data.txt", "w") as f:
        for line in lines:
            if  string_deleted not in line:
                f.write(line)
        print("file updated")


f = open("Data.txt",'r+')
info_lines = f.readlines()
for line in info_lines:
    details = line.split("|")
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
    print("7. Calculate")
    print("8. Close")
    print("===============================")


def show_categories(): #to show the categories
    print("Categories: ", Categories)

def addCategories(NewElement): #to add a new category
    Categories.append(NewElement)
    Entries.append([0])
    Prices.append([0])
    print('Category added : ', NewElement)


def removeCategories(Element): #to remove categories
    print("Categories: ", Categories)
    if Element in Categories:
        ind = Categories.index(Element)
        Entries.remove(Entries[ind])
        Prices.remove(Prices[ind])
        Categories.remove(Element)
        print("Category removed: ", Categories)

def showEntries():
    show_categories()
    Categ_indices = input("select your category: ")
    if Categ_indices in Categories:
        ind = Categories.index(Categ_indices)  # to get the index of the category
        for i in range(len(Entries[ind])):
            print(Entries[ind][i]," with ",Prices[ind][i])
    else:
        print("Invalid choice")
        time.sleep(2)

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
        tempInd = Entries[indice].index(element)
        Prices[indice].pop(tempInd)
        Entries[indice].remove(element)
        print('Entry removed : ', element)

def Calculate_menu():
    print("==============================")
    print("Calculate Menu")
    print("==============================")
    print("1. Sum of a Category")
    print("2. Sum of everything")
    print("3. Average of a Category")
    print("4. Average of everything")
    print("5. the rest")
    print("6. Exit")
    print("==============================")

def SumOfCategory(Categ_indices):
    array_price = np.array(Prices)
    array_price = array_price.astype(float)
    sumOfCategory = array_price[Categ_indices].sum()
    print("Sum of category: ", sumOfCategory)

def SumOfeverything():
    array_price = np.array(Prices)
    array_price = array_price.astype(float)
    SumOfEverything = array_price.sum()
    print(f"Sum of everything: {SumOfEverything}" )


while choix!=8:#to close when I click 8
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
        fileUpdate(Element)
        time.sleep(1)

    elif choix == 4: #4.Show Entry
        showEntries()

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
            fileEntry = f"{Categ_indices}|{Entry}"
            fileUpdate(fileEntry)
        else:
            print("Invalid choice")
            time.sleep(2)
    elif choix == 7:
        Calculate_menu()
        while second_choix != 5:
            second_choix = int(input("Enter your choice: "))
            if second_choix == 1:
                show_categories()
                Categ_indices = input("select your category: ")
                if Categ_indices in Categories:
                    ind = Categories.index(Categ_indices)
                    SumOfCategory(ind)
            elif second_choix == 2:
                SumOfeverything()






f.close()

