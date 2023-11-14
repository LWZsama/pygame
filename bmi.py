name = ""
weight = 0
height = 0
bmi = 0

def iname():
    global name
    name = input("what is your name?\n")
    print(f"hello {name}, let's start")

def iweight():
    global weight
    weight = float(input(f"what is your weight(kg), {name}?\n"))

def iheight():
    global height
    height = float(input(f"what is your height(m), {name}?\n"))

def calculate():
    global bmi
    bmi = weight / (height ** 2)
    print(f"your bmi is {bmi}")

def assess():
    global bmi
    if bmi < 18.5:
        print("your weight is too low!")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("you are 6healthy, keep on!")
    elif bmi > 24.9 and bmi < 29.9:
        print("your weight is high!")
    else:
        print("your weight is too high!! Do more exercise!")

def main():
    iname()
    iweight()
    iheight()
    calculate()
    assess()

main()