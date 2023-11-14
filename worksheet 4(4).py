'''
def multiply(a,b,c):
    t = c - b + 1
    temp = b
    for i in range(0,t):
        print(str(a) + " x " + str(temp) + " = " + str(a * temp))
        temp = temp + 1

time,start,end=map(int,input("enter your time table, start number, and end number\n").split())
multiply(time,start,end)'''

def emptyCarPark(carPark):
    return [["empty" for i in range(6)] for j in range(10)]

def parkACar(carPark):
    registration = input("Enter the registration number of the car: ")
    for row in range(len(carPark)):
        for column in range(len(carPark[row])):
            if carPark[row][column] == registration:
                print("This registration number is occupied. Please re-enter.")
                parkACar(carPark)
                return
    row = int(input("Enter the row number (1-10): ")) - 1
    column = int(input("Enter the column number (1-6): ")) - 1
    if carPark[row][column] == "empty":
        carPark[row][column] = registration
        print("Car with registration " + registration + " has been parked at" + str([row + 1,column + 1]) + ".")
    else:
        print("This space is occupied. Please re-enter.")
        parkACar(carPark)

def removeACar(carPark):
    registration = input("Enter the registration number of the car to remove: ")
    for row in range(len(carPark)):
        for column in range(len(carPark[row])):
            if carPark[row][column] == registration:
                carPark[row][column] = "empty"
                print("Car with registration " + registration + " has been removed")
                return
    print("error, registration " + registration + " not found")

def displayCarParkGrid(carPark):
    for row in range(len(carPark)):
        print("\n")
        for column in range(len(carPark[row])):
            print(carPark[row][column],end = "\t")

carPark=[]
carPark = emptyCarPark(carPark)

print("1. Reset all spaces in the car park to 'empty'")
print("2. Park a car")
print("3. Remove a car")
print("4. Display the car park grid")
print("5. Quit")

option = int(input("Enter your choice: "))

while option != 5:
    if option == 1:
        carPark=emptyCarPark(carPark)
        print("success")
        option = int(input("Enter your choice: "))
    elif option == 2:
        parkACar(carPark)
        option = int(input("Enter your choice: "))
    elif option == 3:
        removeACar(carPark)
        option = int(input("Enter your choice: "))
    elif option == 4:
        displayCarParkGrid(carPark)
        option = int(input("Enter your choice: "))
    else:
        print("Invalid choice - please re-enter.")
        option = int(input("Enter your choice: "))
print("goodbye")

    