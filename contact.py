print("======CONTACTS======")
options = ["1. Add Contact", "2. Edit Contact", "3. View Contact", "4. Exit"]
contact = dict()

while(True):
    for option in options:
        print(option) 
    choice = int(input("choose Your Choice(1,2,3 or 4): ")) 
    if(choice == 1):
        name = input("Enter Name : ")
        num = int(input("Enter Number : "))
        contact[name] = num
        print("-" * 20)
        print("Added Successfully")
        print("-" * 20)
    
    elif(choice == 2):
        search = input("Search Contact By Name: ")     
        if(search in contact.keys()):
            edOp = input("Name or Number: ")
            if edOp.lower() == "name":
                edName = input("Enter New Name: ")
                contact[edName] = contact.pop(search)
                print("-" * 20)
                print("Renamed Successfully")
                print("-" * 20)
            elif edOp.lower() == "number":
                edNum = input("Enter New Number: ")
                contact[search] = edNum
                print("-" * 20)
                print("Number Updated Successfully")
                print("-" * 20)
            else:
                print("-" * 20)
                print("Invalid Option")
                print("-" * 20)
        else:
            print("-" * 20)
            print("Contact Not Been Found !!")
            print("-" * 20)    

    elif(choice == 3):
        print("-" * 25)
        print(f"{'Name':<15} {'Number':<15}")  
        print("-" * 25)
        for k, v in contact.items():
           print(f'{k:^10} {v:^10}')
        print("-" * 20)
           
    elif(choice == 4):
        print("-" * 20)
        print("Exited Successfully !!")
        print("-" * 20)
        break
    
    else:
        print("-" * 20)
        print("Invalid Choice !!")
        print("-" * 20)