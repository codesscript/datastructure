from array import *
arr=[[1,2,3],[4,5,6],[7,8,9]]
val=11
print(arr)
#updation
for x in arr:
    for y in range(0,len(x)):
        x[y]=val
        val+=1
print("after the updation array :  "+ str(arr))
#insertion
arr.insert(1,[1,2,3])
print(arr)
del(arr[1])
print(arr)