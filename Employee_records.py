# #LENGTHY CODE ABOVE
employee1=input("enter employee 1 details:")
tup1=tuple(employee1.split(','))

employee2=input("enter employee 2 details:")
tup2=tuple(employee2.split(','))

employee3=input("enter employee 3 details:")
tup3=tuple(employee3.split(','))

# tup4=tup1+tup2+tup3

# lst1=tuple(tup4)
#wrong logic abve
lst1=[]
lst1.append(tup1)
lst1.append(tup2)
lst1.append(tup3)
dict={}

key="employee"
dict[key]=lst1


print(dict)

# for value in dict:
#     value=dict[key]
#     name=value[value][0]
#     salary=value[value][1]
#     position=value[value][2]
#     print(f"The employee {value[0][0]} has salary {value[1][1]} whose position is {value[2]}")
#mistake

for employee in dict[key]:
    print(f"the employee {employee[0]} has salary {employee[1]} whose position is {employee[2]}")
 