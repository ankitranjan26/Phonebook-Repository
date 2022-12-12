##To input the contacts 
contacts={"sidhharth":9794722895,
          "farooq":9059513480,
          "nitish":7380583988,
          "ankit":8340200403,
          "sumit":7372858878,
          "atharv":8271398787}
## Printing all the contacts 
for i,j in contacts.items():
    print("name:{}\nNumber:{}".format(i,j))
##function to search the contacts 
def search():
    '''To search the contacts'''
    name=input("Enter the contact name : ").lower() #Taking name as input
    if name in contacts:#condition to check the name
        print(f"{name}:{contacts[name]}")
    else:
        b=input("no results found\nTo create a contact type yes or no if you don't want to  :")# taking input 
        while True:
            if b=="yes":#condition 2
                contacts[name]=int(input("Enter the number : "))
                for i,j in contacts.items(): #Printing all the contacts 
                        print("name:{}\ncontacts:{}".format(i,j))
                break
            elif b=="no":#condition 3
                break
            else:# If there is no input it return to the first condition
                return
def multiple_search():
    '''to search multiple contacts'''
    num=int(input("Enter the number of contacts you want to search : "))
    for name in range(num):
        name=input("Enter the contact name : ")
        if name in contacts:
            print(f"{name}:{contacts[name]}")
        else:
            b=input("no results found\nTo create a contact type yes or no if you don't want to  :")# taking input 
            while True:
                if b=="yes":#condition 2
                    contacts[name]=int(input("Enter the number : "))
                    print(f"{name}:{contacts[name]}")
                    for i,j in contacts.items(): #Printing all the contacts 
                            print("name:{}\ncontacts:{}".format(i,j))
                    break
                elif b=="no":#condition 3
                    break
                else:# If there is no input it return to the first condition
                    return
            
while True:
    c=input("Type 'search' to search\nType multiple search to search multiple contacts\nType no to stop searching\nchoose an option given below: ") #Taking input
    if c=='search': #condition 4
        search()
    elif c=='multiple search':
        multiple_search()
    elif c=='no':#condition 5
        break
    else:# If there is no input it return to the first condition
        print("Type any of the Options")
