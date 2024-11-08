def vaccum(rooms):
    current=input("Enter starting Room:")
    while 0 in rooms.values():
        print("Cuurent State:",current)
        choice=int(input("\n What is your choice:\n 1.Clean \n 2.Move\n"))
        if (choice==1):
            if rooms[current]==1:
                print("Room is already Cleaned")
            else:
                rooms[current]=1
                print("Cleaning room",current,"\n Room",current,"is cleaned.\n")
            
        elif choice==2:
            move=input("Enter which room you want to move to:\n")
            if move in rooms:
                current=move
                print("Current Room:",current)
            else:
                print("\n Invalid Room.")
        else:
            print("Invalid choice.\n")
rooms={
    'a':1,
    'b':0,
    'c':1,
    'd':0
}
vaccum(rooms)
