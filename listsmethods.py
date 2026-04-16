my_list=["mike","mary","junior",100,200,True,False]
# remove Removes the item with the specified value
my_list.remove(100)
print(my_list)
# pop Removes the item with at a specified index...if the index is not specified it removes the last item
my_list.pop(2)
print(my_list)
# append adds items at the end of the list
my_list.append('hope')
print(my_list)
# insert adds items t a specified index
my_list.insert(1,'Richard')
print(my_list)

lst=[10,20,30,['mary','kim',[1000,2000,3000]],40,50,60]
# usin methods add 70 at the end of the list
lst.append(70)
print(lst)
# add jane btwn mary and kim 
lst[3].insert(1,'jane')
print(lst)

# add 1500 btwn 1000 and 2000
lst[3][3].insert(1,1500)
print(lst)

# using methods remove 2000
lst[3][3].remove(2000)
print(lst)

# count counts number of apperance of an item in a list
lst2=["mike","mary","junior"]
print(lst2.count('mike'))
# sort arranges items in a certain order
lst3=[1,30,2,40,3,50]
lst3.sort(reverse=True)
print(lst3)
# extend
lst1=[10,20,30,40]
lst2.extend(lst1)
print(lst2)
# clear
lst1.clear()
print(lst1)
# in operator checks for membership
print('mike' in lst2)