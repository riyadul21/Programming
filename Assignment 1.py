# Riyadul Islam

# Programming Fudamentals





userList = []

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
             userList.append([first_name, last_name, address_line1, address_line2, address_line3, address_line4, postcode, stdcode, telephone_number])
             Main_Menu()

    elif userOptions == 2:
         print("2) Change Existing User")
         last_name_change = input("Enter The Last Name of The Persons Address You Would Like To Change\n")
         i = 0
         amt_tries = len(userList)
         while last_name_change not in userList[i][1]:
               i += 1
               if i == amt_tries:
                print("LastName was NOT found\n")
                Main_Menu()

    if last_name_change in userList[i][1]:
         print("Name found")
         print("Their first line of their current addreess is", userList[i][2])
         address_line1pt2 = input("Enter New First Line of Address")
         userList[i][2] = address_line1pt2
         print("Their second line of their current addreess is", userList[i][3])
         address_line2pt2 = input("Enter New Second Line of Address")
         userList[i][3] = address_line2pt2
         print("Their third line of their current addreess is", userList[i][4])
         address_line3pt2 = input("Enter New Fourth Line of Address")
         userList[i][4] = address_line3pt2
         print("Their fourth line of their current addreess is", userList[i][5])
         address_line4pt2 = input("Enter New Fourth Line of Address")
         userList[i][5] = address_line4pt2
         print("Their Post Code is", userList[i][6])
         postcodept2 = input ("Enter New Post code of Address")
         userList[i][6] = postcodept2
         print("Their stdcode is", userList[i][7])
         stdcodept2 = input ("Enter New Area Code")
         userList[i][6] = stdcodept2
         print("Telephone Number is", userList[i][8])
         telephone_numberpt2 = input ("Enter New Telephone Number")
         userList[i][8] = telephone_numberpt2
         print("New Address has been updated", userList[i])
         Main_Menu()




    elif userOptions == 3:
         print("3)View all addresses where last name starts with letter")

         LastLetter = input ("Enter the first letter of their last name")

         i = 0
         amt_tries = len(userList)
         while lastLetter not in userList[i][1][0]:
               i += 1
               if i == amt_tries:
                  print("Last name not found!")
                  Main_Menu
         if LastLetter in userList[i][1][0]:
            print("Last name has been found")
            print("\nfirstname", userList[i][0], "\nlastname", userList[i][1], "\naddress", userList[i][2],
            "\n", userList[i][3], "\n", userList[i][4], "\n", userList[i][5], "\nPostcode", userList[i][6],
            "\nstdcode", userList[i][7], "\ntelephone", userList[i][8], "\n" )
            Main_Menu


    elif userOptions == 4:
         print("4)List All Addresses\n")

         i = 0
         amt_tries = len(userList) -1
         while i <= amt_tries:
            print("\nfirstname", userList[i][0], "\nlastname", userList[i][1], "\naddress", userList[i][2],
            "\n", userList[i][3], "\n", userList[i][4], "\n", userList[i][5], "\nPostcode", userList[i][6],
            "\nstdcode", userList[i][7], "\ntelephone", userList[i][8], "\n" )
            i += 1
         if i == amt_tries:
            Main_Menu



    elif userOptions == 5:
         print("Thank You, goodbye.")
    else:
         print("Input not recognised, please try again...")
         Main_Menu




Main_Menu()
