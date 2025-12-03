n=int(input("Enter the number of items to be added "))
items_list=[]
dict1={}
i=1
while i<=n:
    items=input("Enter items")
    items=items.split(',')
    items=tuple(items)
    items_list.append(items)
    i+=1
dict1["order"]=items_list
print(dict1)
'''i created lst as emplty list and lst.append() was asssigned to items_list hence output showed {'order': None} hence in this case always make sure to contain declare the list as empty in which u are using append'''

order_eg= {
    "order_id":5001,
    "customer":"Apeksha",
    "items":}
    