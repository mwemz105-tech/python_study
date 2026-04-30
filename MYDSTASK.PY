my_ds=[23,"Jane",(560),["Lesson","Maths",{"currency":"KES"}],987,(76,"John")]
# 1. Print KES
print(my_ds)
print(type(my_ds))
print(my_ds[3][2]["currency"])
# 2. print 560 
print(my_ds[2])
# 3. Print Maths
print(my_ds[3][1])
# 4.
my_ds[3][2]["amount"] = 90
print(my_ds[3][2])
# 5.
my_ds[4]=str(my_ds[4])
print(my_ds)
# converting to a string
my_ds[4]=my_ds[4][::-1]
my_ds[4]=int(my_ds[4])
print(my_ds)
# 6.
my_ds[5]=list(my_ds[5])
my_ds[5][1]='Jane'
my_ds[5]=tuple(my_ds[5])
print(my_ds)
