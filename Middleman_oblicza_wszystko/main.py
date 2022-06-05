import math
import tkinter
from tkinter import *
from numpy import *
import numpy as np
from Calculate import Calculations

numberOfCustomers = 0
numberOfSuppliers = 0

customerEntries = {}
supplierEntries = {}
transportEntries = {}


def mainWindow():
    rootWindow = Tk()
    rootWindow.title("Middleman problem")
    rootWindow.configure(background="white")
    rootWindow.resizable(width=True, height=True)
    # rootWindow.geometry("300x500")
    global numberOfCustomers
    global numberOfSuppliers

    numberOfSuppliers = 0

    def submitInputData():

        def calculate():
            customersArray = [[0 for x in range(2)] for y in range(numberOfCustomers)]
            suppliersArray = [[0 for x in range(2)] for y in range(numberOfSuppliers)]


            print(numberOfCustomers, numberOfSuppliers)
            temp5 = 0
            for x in range(0, numberOfSuppliers):
                for y in range(0, 2):
                    temp4 = int(supplierEntries[x + y + temp5].get())
                    suppliersArray[x][y] = temp4
                temp5 += 1
            temp5 = 0
            for x in range(0, numberOfCustomers):
                for y in range(0, 2):
                    temp4 = int(customerEntries[x + y + temp5].get())
                    customersArray[x][y] = temp4
                temp5 += 1
            tempArray = []
            for x in range(0, numberOfCustomers * numberOfSuppliers):
                temp4 = int(transportEntries[x].get())
                tempArray.append(temp4)

            transportCostsArray = np.reshape(tempArray, (int(numberOfSuppliers), int(numberOfCustomers)))

            provider = []
            for x in range(0, len(suppliersArray)):
                provider.append(suppliersArray[x][0])

            recipient = []
            for x in range(0, len(customersArray)):
                recipient.append(customersArray[x][0])

            profits = [[0 for x in range(len(recipient))] for y in range(len(provider))]

            for x in range(0, len(profits)):
                for y in range(0, len(profits[0])):
                    #print("customer",customersArray[y][1])
                    #print("supplier",suppliersArray[x][1])
                    #print("transport",transportCostsArray[x][y])
                    profits[x][y] = customersArray[y][1] - (suppliersArray[x][1] + transportCostsArray[x][y])
                    #print("profit",profits[x][y])
            calc = Calculations()
            result = calc.compute(provider, recipient, profits)

            print(result)
            totalCost = 0
            opt = ""
            for x in range(0, len(result)):
                for y in range(0, len(result[0])):
                    print("Result",result[x][y])
                    opt = opt + str(result[x][y]) + " "
                opt = opt + "\n"



            for x in range(0,len(profits[0])-1):
                for y in range(0, len(profits[0])):
                    totalCost = totalCost + (profits[x][y] * result[x][y])

            print(totalCost)


            purchase = 0 #TO SA KOSZTY ZAKUPU
            for x in range(0,len(profits[0])-1):
                for y in range(0, len(profits[0])):
                    #print("supplier", suppliersArray[x-1][1])
                    #print("Result", result[x][y])
                    purchase = purchase + (result[x][y] * suppliersArray[x][1])

            print(purchase)

            transport = 0
            for x in range(0,len(profits[0])-1):
                for y in range(0, len(profits[0])):
                    #print("transport", transportCostsArray[x][y])
                    #print("Result", result[x][y])
                    transport = transport + (result[x][y] * transportCostsArray[x][y])
            print(transport)

            revenue = 0
            for x in range(0, len(profits[0]) - 1):
                for y in range(0, len(profits[0])):
                    #print("transport", transportCostsArray[x][y])
                    #print("Result", result[x][y])
                    revenue = revenue + (result[x][y] * customersArray[y][1])
            print(revenue)

            #totalCost = 0 # trzeba obliczyc to
           # revenue = 0
            #middlemansProfit = 0

            resultsWindow = Tk()
            resultsWindow.resizable(width=True, height=True)  # okno główne rozciągalność
            resultsWindow.title("Results")
            resultsWindow.configure(bg="white")

            resultLabel1 = Label(resultsWindow, text='Total cost:\t{}'.format(totalCost), font=("Helvetica,15"))
            resultLabel1.grid(sticky=N, row=0, column=0)
            resultLabel1.configure(fg='green', background="white")

            resultLabel2 = Label(resultsWindow, text='Purchase Cost:\t{}'.format(purchase), font=("Helvetica,15"))
            resultLabel2.grid(sticky=N, row=1, column=0)
            resultLabel2.configure(fg='green', background="white")

            resultLabel3 = Label(resultsWindow, text='Transport Cost:\t{}'.format(transport),font=("Helvetica,15"))
            resultLabel3.grid(sticky=N, row=2, column=0)
            resultLabel3.configure(fg='green', background="white")

            resultLabel4 = Label(resultsWindow, text='Revenue:\t{}'.format(revenue),font=("Helvetica,15"))
            resultLabel4.grid(sticky=N, row=3, column=0)
            resultLabel4.configure(fg='green', background="white")

            resultLabel5 = Label(resultsWindow, text='Optimized:\n{}'.format(opt),font=("Helvetica,15"))
            resultLabel5.grid(sticky=N, row=4, column=0)
            resultLabel5.configure(fg='green', background="white")

            resultsWindow.mainloop()

        global numberOfCustomers
        global numberOfSuppliers
        global customerEntries
        global supplierEntries
        global transportEntries
        numberOfSuppliers = numberOfSuppliersEntry.get()
        numberOfCustomers = numberOfCustomersEntry.get()
        numberOfSuppliers = int(numberOfSuppliers)
        numberOfCustomers = int(numberOfCustomers)
        rootWindow.destroy()
        inputTableWindow = Tk()
        inputTableWindow.resizable(width=True, height=True)  # okno główne rozciągalność
        inputTableWindow.title("Input Data Tables")
        inputTableWindow.configure(bg="white")

        columnLabel1 = Label(inputTableWindow, text="Supplier's ID")
        columnLabel1.grid(sticky=N, row=0, column=0)
        columnLabel1.configure(fg='green', bg="white")

        columnLabel2 = Label(inputTableWindow, text="Supply")
        columnLabel2.grid(sticky=N, row=0, column=1)
        columnLabel2.configure(fg='green', bg="white")

        columnLabel3 = Label(inputTableWindow, text="Selling price")
        columnLabel3.grid(sticky=N, row=0, column=2)
        columnLabel3.configure(fg='green', bg="white")

        temp = 0
        temp2 = 0
        temp3 = 0
        cCounter = 0
        sCounter = 0
        tCounter = 0

        for i in range(0, numberOfSuppliers):
            columnLabel = Label(inputTableWindow, text='{}:'.format(i + 1), font=("Helvetica,15"))
            columnLabel.grid(sticky=N, row=i + 1, column=0)
            columnLabel.configure(fg='green', bg="white")

            supplierEntries[sCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"))
            supplierEntries[sCounter].grid(sticky=N, row=i + 1, column=1)
            supplierEntries[sCounter].configure(fg="magenta")

            sCounter += 1

            supplierEntries[sCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"), fg="magenta")
            supplierEntries[sCounter].grid(sticky=N, row=i + 1, column=2)

            sCounter += 1

            temp += 1

        columnLabel1 = Label(inputTableWindow, text="Customers's ID")
        columnLabel1.grid(sticky=N, row=temp + 2, column=0)
        columnLabel1.configure(fg='green', bg="white")

        columnLabel2 = Label(inputTableWindow, text="Demand")
        columnLabel2.grid(sticky=N, row=temp + 2, column=1)
        columnLabel2.configure(fg='green', bg="white")

        columnLabel3 = Label(inputTableWindow, text="Purchasing price")
        columnLabel3.grid(sticky=N, row=temp + 2, column=2)
        columnLabel3.configure(fg='green', bg="white")

        for i in range(0, numberOfCustomers):
            columnLabel = Label(inputTableWindow, text='{}:'.format(i + 1), font=("Helvetica,15"))
            columnLabel.grid(sticky=N, row=temp + 3 + i, column=0)
            columnLabel.configure(fg='green', bg="white")

            customerEntries[cCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"))
            customerEntries[cCounter].grid(sticky=N, row=temp + 3 + i, column=1)
            customerEntries[cCounter].configure(fg="magenta")
            cCounter += 1

            customerEntries[cCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"))
            customerEntries[cCounter].grid(sticky=N, row=temp + 3 + i, column=2)
            customerEntries[cCounter].configure(fg="magenta")
            cCounter += 1

            temp2 += 1

        label = Label(inputTableWindow, width=10, font=("Helvetica,15"))
        label.grid(sticky=N, row=temp + temp2 + 3, column=0)
        columnLabel2.configure(fg='green', bg="white")

        for i in range(0, numberOfCustomers):  # naglowki
            label = Label(inputTableWindow, width=10, text='C{}:'.format(i + 1), font=("Helvetica,15"))
            label.grid(sticky=N, row=temp + temp2 + 3, column=i + 1)
            columnLabel2.configure(fg='green', bg="white")

        for i in range(0, numberOfSuppliers):  # naglowki
            label = Label(inputTableWindow, width=10, text='S{}:'.format(i + 1), font=("Helvetica,15"))
            label.grid(sticky=N, row=temp + temp2 + 4 + i, column=0)
            columnLabel2.configure(fg='green', bg="white")
            for j in range(0, numberOfCustomers):
                transportEntries[tCounter] = Entry(inputTableWindow, width=10, font=("Helvetica,15"))
                transportEntries[tCounter].grid(sticky=N, row=temp + temp2 + 4 + i, column=j + 1)
                transportEntries[tCounter].configure(fg="magenta")
                tCounter += 1
            temp3 = temp + temp2 + 4 + i

        submitButton = Button(inputTableWindow, text='Calculate', command=calculate, font=("Helvetica,15"), width=20)
        submitButton.grid(row=temp3 + 1, column=1)
        submitButton.config(fg='green', background="white")

        inputTableWindow.mainloop()

    numberOfSuppliersLabel = Label(rootWindow, text="Number of suppliers", font=("Helvetica,15"))
    numberOfSuppliersLabel.grid(sticky=N, row=1, column=0)
    numberOfSuppliersLabel.configure(fg='green', background="white")

    numberOfSuppliersEntry = Entry(rootWindow, width=20, fg="magenta", font=("Helvetica,15"))
    numberOfSuppliersEntry.grid(sticky=N, row=1, column=1, padx=3)

    numberOfCustomersLabel = Label(rootWindow, text="Number of clients", font=("Helvetica,15"))
    numberOfCustomersLabel.grid(sticky=N, row=2, column=0)
    numberOfCustomersLabel.configure(fg='green', background="white")

    numberOfCustomersEntry = Entry(rootWindow, width=20, fg="magenta", font=("Helvetica,15"))
    numberOfCustomersEntry.grid(sticky=N, row=2, column=1, padx=3)

    button = Button(rootWindow, text='Submit data', command=submitInputData, font=("Helvetica,15"))
    button.grid(row=5, column=0)
    button.config(fg='green', background="white")

    rootWindow.mainloop()


if __name__ == '__main__':
    mainWindow()