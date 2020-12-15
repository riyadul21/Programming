# Riyadul Islam

# Programming Fudamentals



global last_name

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
             Main_Menu()
    elif userOptions == 2:
         print("2) Change Existing User")
         last_name_change = input("Enter The Last Name of The Persons Address You Would Like To Change\n")
         i = 0
         amt_tries = len(userOptions)
         while last_name_change not in userOptions[i][1]:
               i +=1
               if i == amt_tries:
                print("LastName was NOT found\n")
                Main_Menu()
    if last_name_change in userOptions[i][1]:
         print("Name found")
         print("Their first line of their current addreess is", userOptions[i][2])
         address_line1pt2 = input("Enter New First Line of Address")
         userOptions[i][2] = address_line1pt2
         print("Their second line of their current addreess is", userOptions[i][3])
         address_line2pt2 = input("Enter New Second Line of Address")
         userOptions[i][3] = address_line2pt2
         print("Their third line of their current addreess is", userOptions[i][4])
         address_line3pt2 = input("Enter New Fourth Line of Address")
         userOptions[i][4] = address_line3pt2
         print("Their fourth line of their current addreess is", userOptions[i][5])
         address_line4pt2 = input("Enter New Fourth Line of Address")
         userOptions[i][5] = address_line4pt2
         print("Their Post Code is", userOptions[i][6])
         postcodept2 = input ("Enter New Post code of Address")
         userOptions[i][6] = postcodept2
         print("Their stdcode is", userOptions[i][7])
         stdcodept2 = input ("Enter New Area Code")
         userOptions[i][6] = stdcodept2
         print("Telephone Number is", userOptions[i][8])
         telephone_numberpt2 = input ("Enter New Telephone Number")
         userOptions[i][8] = telephone_numberpt2
         print("New Address has been updated", userOptions[i])
         Main_Menu()
         break


    else:
            address_line1 = input("Enter First Line of Address\n")
            address_line2 = input("Enter Second Line of Address\n")
            address_line3 = input("Enter Third Line of Address\n")
            address_line4 = input("Enter Fourth Line of Address\n")
            postcode = input("Enter the PostCode\n")
            stdcode = int(input("Enter Area Code for Telephone Number\n"))
            telephone_number = int(input("Enter Telephone Number\n"))
    if userOptions == 3:
         print("3)View All Addresses Where Last Name Starts With Letter")
    elif userOptions == 4:
         print("4)List All Addresses\n")
    elif userOptions == 5:
         print("5) Quit")
    else:
         print("Input not recognised, please try again...")


Main_Menu()
