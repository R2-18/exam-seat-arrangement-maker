import setup_files
import reader
import allocator
def dsresults(plan, leftseat, studentdetail):
    ofile = open("seatingoutput.txt", "w")
    
    for roome in plan:
        row = plan[roome][0]
        column = plan[roome][1]
        seatinroom = plan[roome][2]
        
        # Explicit Room Header
        room_header = f"\n{'='*55}\n          EXAM ROOM: {roome} (Total Capacity: {row * column})\n{'='*55}\n"
        print(room_header)
        ofile.write(room_header)
        
        seatindex = 0
        for i in range(row):
            print(f"--- Row {i+1} ---")
            ofile.write(f"--- Row {i+1} ---\n")
            
            rowdis = ""
            for j in range(column):
                roll = seatinroom[seatindex]
                seat_num = j + 1
                
                if roll == "empty":
                    seat_info = f"[Seat {seat_num}: EMPTY]"
                else:
                    info = studentdetail[roll]
                    name = info[0]
                    branch = info[1]
                    seat_info = f"[Seat {seat_num}: Roll: {roll} | Name: {name} | Branch: {branch}]"
                
                # Print each seat neatly indented
                rowdis += f"  {seat_info}\n"
                seatindex += 1
                
            print(rowdis)
            ofile.write(rowdis + "\n")
            
    # Capacity summary
    if len(leftseat) > 0:
        wrn = f"\n{'!'*55}\nWarning: {len(leftseat)} student(s) could not be seated due to insufficient seating capacity!\n{'!'*55}\n"
        print(wrn)
        ofile.write(wrn)
    else:
        scs = f"\n{'-'*55}\nAll students have been successfully allocated seats!\n{'-'*55}\n"
        print(scs)
        ofile.write(scs)
        
    ofile.close()
    print(">> Seating plan has also been saved to 'seatingoutput.txt'.\n")
def allocation():
    print("\n Reading data from files \n")
    rnolist,studentdetail=reader.readstd()
    roomnos=reader.readroom()
    if len(rnolist)==0:
        print("Error students.txt is empty, enter data first")
        return
    if len(roomnos)==0:
        print("Error rooms.txt is empty, enter data first")
        return
    print(f"Total students found: {len(rnolist)}")
    print(f"Total rooms found: {len(roomnos)}")
    print("\n Assigning seats\n")
    plan,leftseat=allocator.allocate(rnolist,roomnos)
    dsresults(plan,leftseat,studentdetail)
def main():
    while True:
        print("\n"+"-"*10)
        print("    Exam seat allocator (Menu driven)")
        print("-"*10)
        print("1. Use previous data (Assign seats from existing files)")
        print("2. Enter new data (Input students and rooms, then assign)")
        print("3. Exit")
        print("=" * 10)
        choice=input("Enter your choice (1/2/3): ").strip()
        if choice=="1":
            if reader.fileexist():
                allocation()
            else:
                print("\nERROR: No previous data found!")
                print("select Option 2 to enter data first.")
        elif choice=="2":
            setup_files.newdata()
            allocation()
        elif choice=="3":
            print("\n Exiting program.")
            break
        else:
            print(f"Invalid choice {choice}")
if __name__=="__main__":
    main()