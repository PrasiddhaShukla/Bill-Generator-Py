import pandas as pd
#import numpy as np
#Size and width
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#Greetings
name = input("Name :")
print("HI",name,"This project/code is aimed at generating correct customer bills")
print("electronically, in a user-friendly way.")
#Type of product
print("1)Dairy                 2)Frozen Food")
print("3)Stationary            4)Sports")
print("what kind of products do you want to buy? ")
kinds = [1, 2, 3, 4]
while True:
    try:
        kind = int(input("Enter the number corresponding to the item type: "))
        if kind in kinds:
            break
        else:
            print("Incorrect input")
    except ValueError:
        print("Please enter a valid number")
#Personal Details
print("Answer the below requirments ")
country = input("Country :")
country = country.upper()
state = "none"
if country == "INDIA":
    state = input("State :")
    state = state.upper()
#CSV files and product data
df1=pd.read_csv("C:\\Users\\Prasiddha\\OneDrive\\Desktop\\C Programming\\Bill generator\\Dairy.csv")
df2=pd.read_csv("C:\\Users\\Prasiddha\\OneDrive\\Desktop\\C Programming\\Bill generator\\Frozen Foods.csv")
df3=pd.read_csv("C:\\Users\\Prasiddha\\OneDrive\\Desktop\\C Programming\\Bill generator\\Itemlist.csv")
df4=pd.read_csv("C:\\Users\\Prasiddha\\OneDrive\\Desktop\\C Programming\\Bill generator\\Sports.csv")
#Prints the item list according to the item type entered
if kind == 1:
    print(df1) 
elif kind == 2:
    print(df2)
elif kind == 3:
    print(df3)
elif kind == 4:
    print(df4)
#Product details
times = int(input("How many products you want to buy?"))
tax = 0 #acc to place/location
total_price = 0
amount = 0
if times == 0:
    print("Invalid product ID")
else:
    I = []
    Q = []
    P = []
    A = []
    for a in range(1,times+1,1):
        rowindex = int(input("Enter the Rowindex :"))
        if kind == 1:
            real = df1.at[rowindex,'Product']
        elif kind == 2:
            real = df2.at[rowindex,'Product']
        elif kind == 3:
            real = df3.at[rowindex,'Product']
        elif kind == 4:
            real = df4.at[rowindex,'Product']
        I.append(real)
        quan = int(input("enter quantity :"))
        Q.append(quan)
        if kind == 1:
            price = df1.at[rowindex,'Price(Rs)']
        elif kind == 2:
            price = df2.at[rowindex,'Price(Rs)']
        elif kind == 3:
            price = df3.at[rowindex,'Price(Rs)']
        elif kind == 4:
            price = df4.at[rowindex,'Price(Rs)']
        P.append(price) 
        amount = price*quan #amount calculated using rate multiplied with quantity
        A.append(amount)
        print("amount =",amount)
        print("-----------------------------------")
        #Different amt of tax as per location
        if state == "MAHARASHTRA":
           tax = (amount*0.025)
        elif state != "MAHARASHTRA":
            tax = (amount*0.05)
        elif country != "INDIA":
            tax = (amount*0.1)
        #Total Price calculation
        total_price = amount+total_price+tax
#Final Bill Generated
print("______________________________________________________________")
print("            Tax invoice                                       ")                                        
print("         Daily Stationary                                     ")
print("______________________________________________________________")
print("Product/s       :",I)
print("Quantity/ies    :",Q)
print("Rates           :",P)
print("Amounts         :",A)
print('Totalprice      :',total_price,"Rs")
print("______________________________________________________________")
print("interzonal rates: 2.5% tax")
print("interstate rates: 5.0% tax")
print("international rates: 10.0% tax")
print("______________________________________________________________")
print("For more details contact the undermentioned ")
print("MAHARASHTRA: **********")
print("Any other state than MAHARASHTRA: **********")
print("Any other country than INDIA: **********")
print("--------------------------------------------------------------")
print("TERMS AND CONDITIONS APPLY")
print("--------------------------------------------------------------")

