# ---------------------------------------------
# Name: Jaziah Sanders
# Project: Hospital Billing System
# Status: COMPLETE
# ---------------------------------------------
# Project Objectives
#   The program will have a menu allowing the user to enter the type of surgery, the type
#   of medication, the number of days in the hospital, and check the patient out. When the
#   patient checks out, the total charges will be displayed
# ---------------------------------------------



#Class
class Patient:
    def __init__(self, eName):
        self.name = eName
        self.days = 0
        self.medicine = []
        self.surgery = []

    def setDays(self, value):
        self.days = self.days + value

    def getName(self):
        return self.name

    def getDays(self):
        return self.days

    def getMedicine(self):
        return self.medicine

    def setMedicine(self, value):
        self.medicine.append(value)

    def getSurgery(self):
        return self.surgery

    def setSurgery(self, value):
        self.surgery.append(value)

#Main function
def main():
    projectStart()

    surgeryList = {}
    readFile('surgery.txt', surgeryList)

    if len(surgeryList) == 0:
        print("\tSorry, the hospital is closed.")
        return

    medicineList = {}
    readFile('medicine.txt', medicineList)

    if len(medicineList) == 0:
        print("\tSorry, the hospital is closed.")
        return

    hospitalVisit(surgeryList, medicineList)
    projectEnd()


#This function carries out operations depending on which letter the user selects 
def hospitalVisit(surgeryList, medicineList):
    print("\tWelcome to Fredrickson's Hospital!!")
    name = getStringData("\tEnter your name: ")
    myPatient = Patient(name)

    while True:
        menu()
        selection = getCharData("\tMake your selection: ")

        if selection == 'D':
            print('Hospital Days')
            countDays = getIntegerData("\tEnter how many days in the hospital: ")
            cost = countDays * 100
            print('\tThe cost is: $', format(cost, '0.2f'), sep='')
            myPatient.setDays(countDays)

        elif selection == 'M':
            displayData(medicineList, 'medicine.txt')
            cmd = getIntegerData("\tSelect the medicine ID: ")

            try:
                print("\tYou have selected", medicineList[cmd][0])
                cost = float(medicineList[cmd][1])
                print("\tThe price is: $", format(cost, '0.2f'), sep='')
                myPatient.setMedicine(cmd)
            except KeyError:
                print("\tError Message!!! Selection is not correct.")

        elif selection == 'S':
            displayData(surgeryList, 'surgery.txt')
            cmd = getIntegerData("\tSelect the surgery ID: ")

            try:
                print("\tYou have selected", surgeryList[cmd][0])
                cost = float(surgeryList[cmd][1])
                print("\tThe price is: $", format(float(surgeryList[cmd][1]), '0.2f'), sep='')
                myPatient.setSurgery(cmd)
            except KeyError:
                print("\tError Message!!! Selection is not correct.")

        elif selection == 'C':
            print("\tCheckout Time")
            displayCheckout(myPatient, medicineList, surgeryList)
            print("\tPatient name: ", myPatient.getName())
            break
        else:
            print("\tError Message!!! Invalid selection.")

#This function displays the options avaliable to the user
def menu():
    print('-' * 50)
    print("Fredrickson's Hospital")
    print('-' * 50)
    print("\tD) Day in the hospital")
    print("\tM) Medicine")
    print("\tS) Surgery")
    print("\tC) Check out")
    print('-' * 60)

#This function displays the checkout information
def displayCheckout(myPatient, medicineList, surgeryList):
    totalCost = 0
    print('-' * 60)
    print("\tHospital Final Bill")
    print('-' * 60)
    print("Patient name: ", myPatient.getName())
    print('-' * 60)

    print("\t\tDays: ", myPatient.getDays(), end='')
    cost = myPatient.getDays() * 100
    print("\tCost: $", format(cost, '.2f'), sep='')
    totalCost = totalCost + cost

    # Medicine
    listMedicine = myPatient.getMedicine()
    print("\t\tMedicine")
    medicineCost = 0

    for ctr in listMedicine:
        print("\t\t\t", medicineList[ctr][0], end='')
        cost = float(medicineList[ctr][1])
        print("\tCost: $", format(cost, '.2f'), sep='')
        medicineCost = medicineCost + cost

    print("\t\t\tTotal Due for Medicine: $", format(medicineCost, "0.2f"), sep='')
    totalCost = totalCost + medicineCost

    # Surgery
    listSurgery = myPatient.getSurgery()
    print("\t\tSurgery")
    surgeryCost = 0

    for ctr in listSurgery:
        print("\t\t\t", surgeryList[ctr][0], end='')
        cost = float(surgeryList[ctr][1])
        print("\tCost: $", format(cost, '.2f'), sep='')
        surgeryCost = surgeryCost + cost

    print("\t\t\tTotal Due for Surgery: $", format(surgeryCost, "0.2f"), sep='')
    totalCost = totalCost + surgeryCost

    print('-' * 60)
    print("\tTotal Due: $", format(totalCost, "0.2f"), sep='')
    print('-' * 60)


def displayData(dataList, header):
    print('-' * 60)
    print(header)
    print('-' * 60)
    print('\tID', '\tName', '\t\tPrice')
    print('-' * 60)

    for ctr in dataList.keys():
        print('\t', ctr, end='')
        print('\t', dataList[ctr][0], end='')
        print('\t', dataList[ctr][1])


#This function reads the files
def readFile(dataFile, dataList):
    try:
        fileRead = open(dataFile, 'r')
        count = 0

        for line in fileRead:
            line = line.strip('\n').split(',')
            dataList[count] = line
            count = count + 1

        fileRead.close()

    except FileNotFoundError:
        print("Error Message!!! File not found.")


def getCharData(display):
    while True:
        value = input(display)
        value = value.upper()
        if value in ['D', 'M', 'S', 'C']:
            return value
        print("\tError Message!!! Enter 'D', 'M', 'S', or 'C' ")


def getStringData(display):
    while True:
        value = input(display)
        value = value.capitalize()
        return value


def getIntegerData(display):
    while True:
        try:
            value = int(input(display))
            if value < 0:
                raise ValueError
            else:
                return value
        except ValueError:
            print("\tError Message!!! Enter a positive value.")


def projectStart():
    print("Project #")
    print("Written by: Jaziah Sanders")
    print("Date: November 19th, 2024")
    print("Objective")
    print("\tObject Oriented Programming Basics")
    print("-" * 60)


def projectEnd():
    print("-" * 60)
    print("End of project")

main()