from array import *
arr=array("f",[1.1,2.2,3.3,4.4,5.5])
val=11.1
for i in range(0,len(arr)):
    arr[i]=val
    val+=1
print(arr)
to_list=arr.tolist()
print(to_list)
to_list[0]=12
print(to_list)