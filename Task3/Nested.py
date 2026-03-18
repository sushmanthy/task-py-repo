# #Print pattern

rows=5
for i in range(rows):
     for j in range(i+1):
         print("*", end=" ")
     print()

#Numbers

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    
#Multiplictaions

for i in range(1,6):
    print()
    for j in range(1,6):
        print(i,"X",j,"=",i*j)

#Repeat

for i in range(3):
    for j in range(1):
        print("ABC",end=" ")
    print()

#Diff numbers

for i in range(3):
    for j in range(3):
        num=i*3+j+1
        print(num,end=" ")
    print()