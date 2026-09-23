import random
def allocate(rnolist,roomnos):
    copyrnolist=list(rnolist)
    random.shuffle(copyrnolist)
    plan={}
    for room in roomnos:
        roome=room[0]
        row=room[1]
        column=room[2]
        if roome in plan:
            print(f"Error: Duplicate room name {roome} found!")
            continue
        tseats=row*column
        seatinroom=[]
        for i in range(tseats):
            if len(copyrnolist)>0:
                seatinroom.append(copyrnolist.pop(0))
            else:
                seatinroom.append("empty")
        plan[roome]=[row,column,seatinroom]
    leftseat=copyrnolist
    return plan,leftseat