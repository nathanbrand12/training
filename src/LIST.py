GuestList = ["Tom Hanks", "Chris Brown", "Adam Levine", "Justin Aberdeen"]
print(GuestList)
message = "I hereby invite " + GuestList[0].title() + " to my annual fest"
print(message)
print('-----------------------------------------')
GuestList[2] = 'Malboro Man'
print(GuestList)
message = "I hereby invite " + GuestList[2].title() + " to my annual fest"
print(message)
print('-----------------------------------------')
GuestList.insert(0, 'Amaya Jumal')
print(GuestList)
GuestList.insert(2, 'Henry Duval')
print(GuestList)