#bubble sort

mylist = [10,15,3,9,7,0]
for i in range (0,len(mylist)):
    for j in range(i, len(mylist)):
        if mylist[i] < mylist[j]:
            mylist[i],mylist[j] = mylist[j], mylist[i]
print("Sorted list is", mylist)