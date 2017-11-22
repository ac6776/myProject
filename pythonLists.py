# Python3 Lists
print('')
print('Python3 Lists. Create')
guests = ['ross', 'joey', 'chandler', 'monica', 'rachel', 'phoebe']
print(guests)
print('')

massage = "There is my lovely friend " +guests[1].title() + "!"
print(massage)
print('')

# Edit List
# Add elemenent
print('Edit List. Add elemenent by APPEND')
guests.append('janice')
print(guests)
print('')

print('Edit List. Add elemenent by INSERT')
guests.insert(0, 'richard')
print(guests)
print('')

# Delete elements
print('Edit List. Delete elements by DEL')
del guests[0]
print(guests)
print('')

print('Edit List. Hide elements by POP()')
notFriend = guests.pop() #possible to set index. Default is the last one.
print(guests)
print('\t' + notFriend.title() + ' is not a friend!')
print('')

print("GitHub edit")
