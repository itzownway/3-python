mylist = ["apple", "banana", "cherry"]
print(mylist)  # ['apple', 'banana', 'cherry']


print(type(mylist))  # <class 'list'>




thislist = ["apple", "banana", "cherry"]
print(thislist[-1])




thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])




thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)




thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)



thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)




thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1