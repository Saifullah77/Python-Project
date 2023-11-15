contact = { }

def showfuntion():
    print(contact.items())
    print("name \t contact")
    for key in contact:
        print("{} \t {}".format(key, contact.get(key) ))
while True:
    choice = int (input("1. add new contact \n "
                   "2.scarch the contact \n "
                   "3. display the contact \n "
                   "4. edit the contact \n "
                   "5. delete the contact \n "
                   "6. exit \n "
                   "please write number between 1-11:  ") )
    if choice == 1:
        name = input("add your contact name:")
        phone = input("add your phone number:")
        contact[name] = phone
        
    elif choice == 2:
        contactname = input("scarch the contact: ")
        if contactname in contact:
           print(contactname, "contact number is ", contact[contactnumber])
        else:
            print("not found the contact")    
    
    elif choice == 3:
        if not contact:
            print("contact book is empty")
        else:
            showfuntion() 
            
            
    elif choice == 4:
        editcontact = input("edit your contact: ")
        if editcontact in contact:
            phone = input("change your number: ")
            contact[editcontact] = phone
            print("contact updated successfully ")
            showfuntion()
        else:
            print("name is not found")  
            
    elif choice == 5:
        
         Delcontact = input("which contact do you want to delete?")
         if Delcontact in contact:
            deletedconfirm = input("do you want to delete this contact y/n")
            if deletedconfirm == "y" or deletedconfirm == "Y":
                contact.pop(Delcontact)
            showfuntion()    
            
         else:
            print("the number is not found in contact") 
            
    else:
        break                       
     
