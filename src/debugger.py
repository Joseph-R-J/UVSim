class debugger:
    
    def memdump(mem):
        for x in range(len(mem)):
            if type(x) == int:
                mem[x] = str(mem[x])
                mem[x] = mem[x].zfill(5)

            if str(mem[x])[0] == "+":
                mem[x] = mem[x].replace("+", "0")

            if len(mem[x]) != 5:
                mem[x] = mem[x].zfill(5)
                
        print("MEMORY")
        print('{:>3s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}'.format("","00","01","02","03","04","05","06","07","08","09"))
        i = 0
        while i < 91:
            print('{:>3s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}'.format(f"{str(i).zfill(2)}", f"{mem[i]}", f"{mem[i+1]}", f"{mem[i+2]}", f"{mem[i+3]}", f"{mem[i+4]}", f"{mem[i+5]}", f"{mem[i+6]}", f"{mem[i+7]}", f"{mem[i+8]}", f"{mem[i+9]}"))
            i += 10


#Test case
# x = ["+132"] * 100
# debugger.memdump(x)

#old version of print preserved so I don't have to type it out again if I need it
#print(f"{str(i).zfill(2)}       {mem[i]}        {mem[i+1]}      {mem[i+2]}      {mem[i+3]}      {mem[i+4]}      {mem[i+5]}      {mem[i+6]}      {mem[i+7]}      {mem[i+8]}      {mem[i+9]}".format("10d"))