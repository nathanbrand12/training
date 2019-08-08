guest_list = ["Nathan", "Peter", "Michael", "Temi"]
print(guest_list)
message = "I hereby invite you, "  + guest_list[0].title() + " to my fest!"
print(message)
print('----------------------------')
guest_list[0] = 'Jon'
print(guest_list)
message2 = "I hereby invite you, "  + guest_list[0].title() + " to my fest!"
print(message2)
print('----------------------------')
guest_list.insert(0, 'Amarae')
guest_list.insert(2, 'Kevin')
guest_list.append('Jamal')
message3 = "I hereby invite you, "  + guest_list[0].title() + " to my fest!"
message4 = "I hereby invite you, "  + guest_list[2].title() + " to my fest!"
message5 = "I hereby invite you, "  + guest_list[-1].title() + " to my fest!"
print(message3)
print(message4)
print(message5)
print(guest_list)
print('Unfortunately, I can only invite two people for the fest')
message5 = guest_list.pop(0)
print("I hereby invite you, "  + guest_list[0].title() + " to my fest!")
del guest_list[0]
del guest_list[1]
del guest_list[2]
print(guest_list)
print('----------------------------')
Places = ["Rome", "Spain", "Greece", "London", "Montreal"]
print(Places)
print("\nHere is the list in alphabetical order:")
print(sorted(Places))
print("\nHere is the list in reverse order:")
Places.reverse()

