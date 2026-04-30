days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)
print(type(days))
# set() used to convert data structures to sets meaning unique items
lst=[10,20,30,40,10,60,30,60]
lst=set(lst)
print(lst)
lst=list(lst) 
print(lst)
# set methods
# add
days.add('mon')
print(days)
days.remove("thursday")
print(days)
days.remove("monday")
days.remove("sunday")
print(days)
days.add("monday")
days.add("sunday")
print(days)
print(type(days))