# Riyadul Islam

# Programming Fudamentals

def Main_Menu():
    userOptions = int(input("Main Menu\n"
    "1)Add New Address\n"
    "2)Change Existing User\n"
    "3)View All Addresses Where Last Name Starts With Letter\n"
    "4)List All Addresses\n"
    "5)Quit\n" ))



    if userOptions == 1:
         print("1) Add new Address")
         if userOptions == 1:
              first_name = input("Enter your first name")
              last_name = input("Enter your Surname")
         if first_name + last_name == "":
           print("No Name Added")
           Main_Menu()
         else:
             address_line1 = input("Enter First Line of Address")
             address_line2 = input("Enter Second Line of Address")
             address_line3 = input("Enter Third Line of Address")
             address_line4 = input("Enter Fourth Line of Address")
             postcode = input("Enter the PostCode")
             stdcode = int(input("Enter Area Code for Telephone Number"))
             telephone_number = int(input("Enter Telephone Number"))
    elif userOptions == 2:
         print("2) Change Existing User")
         last_name_change = input("Enter The Last Name of The Persons Address You Would Like To Change")

    elif userOptions == 3:
         print("3)View All Addresses Where Last Name Starts With Letter")
    elif userOptions == 4:
         print("4)List All Addresses\n")
    elif userOptions == 5:
         print("5) Quit")
    else:
         print("Input not recognised, please try again...")


Main_Menu()









