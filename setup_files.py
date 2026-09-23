def stddata(): #students data
    print("\tEnter Student details\n")
    file=open("students.txt","w")
    num=int(input("Enter How many students do you want to enter:"))
    for i in range(num):
        print(f"\n Student-{i+1}")
        roll=input("Enter Roll number: ").strip().upper()
        name=input("Enter name: ").strip()
        branch=input("Enter Branch: ").strip().upper()
        file.write(roll+','+ name +','+ branch +'\n')
    file.close()
    print("File closed")
def roomdata(): #roomdata
    print("\tEnter Room details\n")
    file=open("rooms.txt","w")
    num=int(input("Enter How many Exam rooms do you have:"))
    for i in range(num):
        print(f"\n Room-{i+1}")
        roomno=input("Enter Room name :").strip().upper()
        rows=input("Enter no. of rows:")
        column=input("Enter no. of columns: ")
        file.write(roomno+','+rows +','+ column +'\n')
    file.close()
    print("File closed")
def newdata():
    stddata()
    roomdata()