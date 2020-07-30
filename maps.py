import collections
dict1= {'sno1':'01','color1':'red','name1':'tom'}
dict2= {'sno2':'02','color2':'green','name2':'jerry'}
dict3= {'sno3':'03','color3':'blue','name3':'alexa'}
dict4= {'sno4':'04','color4':'yellow','name4':'bella'}
res=collections.ChainMap(dict1,dict2,dict3,dict4)
print(res.maps)
dup={}
dict4['color4']='green'
#print(res)
for key,val in res.items():
    print(f'{key}=={val}')
    dup.setdefault(val, set()).add(key)
for key,val in dup.items():
    if len(val)>1:
        print("The duplicate value=="+ str(key))