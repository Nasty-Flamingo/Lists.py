guests = ['guest1', 'guest2', 'guest3']

print(guests,"Hey guys you are the guests i would like to invite to my party \n")


print("There is a bit of problem our guest3 is not comming anymore""\n")

guests.remove('guest3')

print(guests," Now you guys are comming only""\n")


print("Hey boys i have found some new participants for our party \n")

print("Here is our New Guest List \n")
guests.insert(3, 'guest4')
guests.insert(4, 'guest5')
guests.insert(5, 'guest6')
print(guests)

invtation = 'Hey welcome to my party'
invitation2 = 'You guys are still comming'
print(guests, invtation)

table_small = guests.pop(4)
print("sorry guest6 you are not comming \n")
table_small = guests.pop(3)
print("sorry guest5 you are not comming \n")
table_small = guests.pop(2)
print("sorry guest4 you are not comming \n")

print(guests)

print(guests, invitation2)

print("Now i will end list \n")


guests.remove('guest1')
guests.remove('guest2')


print("Completed")

