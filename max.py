myList = [1,2,8,9,100,5000]

for i in range(len(myList)):
        print myList[i]

max = 0

for i in myList:
    if(i > max):
        max = i

print "Max in list is: "
print max
