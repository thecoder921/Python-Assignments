def printName(ch):
    for i in range(6):
        for alp in ch:
            list=attyus.get(alp)
            line=list[i]
            for j in line:
                if j==1:
                    print("*",end='')
                else:
                    print(" ",end='')
            print("  ",end='')
        print()
attyus={'P':[[0,0,1,1,0,0,0]
   ,[0,0,1,0,1,0,0]
   ,[0,0,1,0,1,0,0]
   ,[0,0,1,1,0,0,0]
   ,[0,0,1,0,0,0,0]
   ,[0,0,1,0,0,0,0]],
'R':[[0,0,1,1,0,0,0],
   [0,0,1,0,1,0,0],
   [0,0,1,0,1,0,0],
   [0,0,1,1,0,0,0],
   [0,0,1,0,1,0,0],
   [0,0,1,0,0,1,0]],
'I':[[1,1,1,1,1,1,1],
   [0,0,0,1,0,0,0],
   [0,0,0,1,0,0,0],
   [0,0,0,1,0,0,0],
   [0,0,0,1,0,0,0],
   [1,1,1,1,1,1,1]],
'Y':[[0,1,0,0,0,1,0],
   [0,1,0,0,0,1,0],
   [0,0,1,0,1,0,0],
   [0,0,0,1,0,0,0],
   [0,0,0,1,0,0,0],
   [0,0,0,1,0,0,0]],
'A':[[0,0,0,0,1,0,0,0,0],
   [0,0,0,1,0,1,0,0,0],
   [0,0,1,0,0,0,1,0,0],
   [0,1,0,1,0,1,0,1,0],
   [1,0,0,0,0,0,0,0,1],
   [1,0,0,0,0,0,0,0,1]],
'N':[[0,1,0,0,0,0,1,0],
   [0,1,1,0,0,0,1,0],
   [0,1,0,1,0,0,1,0],
   [0,1,0,0,1,0,1,0],
   [0,1,0,0,0,1,1,0],
   [0,1,0,0,0,0,1,0]],
'S':[[0,0,1,1,1,1,1,0],
   [0,1,0,0,0,0,0,0],
   [0,0,1,1,1,1,0,0],
   [0,0,0,0,0,0,1,0],
   [0,0,0,0,0,0,1,0],
   [0,1,1,1,1,1,0,0]],
'H':[[0,1,0,0,0,0,1,0],
   [0,1,0,0,0,0,1,0],
   [0,1,1,1,1,1,1,0],
   [0,1,0,0,0,0,1,0],
   [0,1,0,0,0,0,1,0],
   [0,1,0,0,0,0,1,0]],
'U':[[0,1,0,0,0,0,1,0],
   [0,1,0,0,0,0,1,0],
   [0,1,0,0,0,0,1,0],
   [0,1,0,0,0,0,1,0],
   [0,1,0,0,0,0,1,0],
   [0,0,1,1,1,1,0,0]]}
name=(input()).upper()
printName(name)
