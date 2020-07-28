from numpy import *
month = [['jan',11,19,24],['feb',12,15,00],
         ['mar',10,16,25] ,['apr',11,10,25],
         ['may',12,25,10], ['jun',13,19,15],
         ['jul',21,15,13],['aug', 13, 52,10],
         ['sep',11,25,24], ['oct',15,18,22],
         ['nev',21,28,15],['dec',12,15,19]]
a=reshape(month,(12,4))
print(a)
#adding a new row
#row_add=append(month,([['jann',10,20,30]]), axis=0)
#print(row_add)
#adding a new column
#col_add=append(month,s_[[10],[20],[30],[11],[12],[13],[14],[15],[16],[21],[31],[22]], axis=1)
#print(col_add)
#delete a row
#del_row=delete(month,3,0)
#multiple row
#del_row=delete(month,[3,5],0)
#print(del_row)
#delete column
#del_col=delete(month,1,1)
#delete multiple column
#del_col=delete(month,[1,3],1)
#print(del_col)
#update the row
#month[11]=[['janu',12,13,14]]
#print(month)
#update column
#month[4][1]=3
#print(month)