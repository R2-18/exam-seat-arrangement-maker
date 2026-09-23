def fileexist():
    try:
        f1 = open("students.txt", "r")
        f1.close()
        f2 = open("rooms.txt", "r")
        f2.close()
        return True
    except FileNotFoundError:
        return False
def readstd(): #read students file
    rnolist=[]
    studentdetail={}
    file=open("students.txt","r")
    for i in file:
        newline=i.strip()
        if newline!="":
            sm=newline.split(",")
            roll=sm[0].strip()
            name=sm[1].strip()
            branch=sm[2].strip()

            if roll in studentdetail:
                print(f"Error: Duplicate roll number {roll} found!")
                continue

            rnolist.append(roll)
            studentdetail[roll]=[name,branch]
    file.close()
    return rnolist,studentdetail
def readroom(): #read room file
    roomnos=[]
    file=open("rooms.txt","r")
    for i in file:
        newline=i.strip()
        if newline!="":
            nm=newline.split(",")
            roome=nm[0].strip()
            row=int(nm[1].strip())
            column=int(nm[2].strip())
            roomnos.append([roome,row,column])
    file.close()
    return roomnos