# dictionries
my_dict={
    'name':'Ropy Kevin',
    'age':25,
    'gender':'Male',
    'City':'Nairobi'
}
print(my_dict)
print(type(my_dict))
# accessing values in a dictionary
print(my_dict['age'])
print(my_dict['City'])
# update and add properties
my_dict['age']=40
print(my_dict)
# add
my_dict['occupation']='Software Developer'
print(my_dict)
# dictionaty methods
# pop
my_dict.pop('gender')
# popiittem
my_dict.popitem
print(my_dict)