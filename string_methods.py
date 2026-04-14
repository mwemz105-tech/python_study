text="Software DEVELOPER"
# capitalize makes the first charcter have upper case and the rest lower
text1=text.capitalize()
print(text1)
# casefold returns a version of the string suitable for caseless comparissons
text2=text.casefold()
print(text2)
# cont counts the number of appearance of a character
text3=text.count('o')
print(text3)
# replace(old,new)
text4=text.replace('DEVELOPER','Engineer')
print(text4)
# endswith and startswith returns boolean either true or false
text5=text.endswith('a')
print(text5)
text6=text.startswith('S')
print(text6)
# lower
text7=text.lower()
print(text7)
# upper
text8=text.upper
print(text8)
#strip is used to remove leading and trailling spaces 
text="   Software DEVELOPER   "
print(len(text))
text=text.strip()
print(len(text))
# split is used to split a string using a character if the character is not provided it splits with space
email='mwemz105@gmail.com'
splitted=email.split('@')
print(splitted)
text9=text.split()
print(text9)
# clean up the following variables to junior developer
text ="   jUnIoR deVelOper   "
text=text.strip()
text=text.capitalize()
print(text)