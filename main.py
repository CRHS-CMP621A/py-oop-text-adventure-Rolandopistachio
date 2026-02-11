from room import Room
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_room = Room("Dining Room")
dining_room.set_description("an empty room with badly set up tables.")

ballroom = Room("ballroom")
ballroom.set_description("A gross place with fleas dancing in a circle to Micheal Jackson's Pretty Young Thing")


kitchen.link_room(dining_room, "south")
#print(kitchen.name + " linked rooms: " + repr(kitchen.linked_rooms))

ballroom.link_room(dining_room, "east")
#print(ballroom.name + " linked rooms: " + repr(ballroom.linked_rooms))

dining_room.link_room(ballroom, "west")
#print(dining_room.name + " linked rooms: " + repr(dining_room.linked_rooms))
dining_room.link_room(kitchen, "north")
#print(dining_room.name + " linked rooms: " + repr(dining_room.linked_rooms))

current_room = kitchen

dining_room.get_details()
dining_room.get_description()


ballroom.get_details()
ballroom.get_description()

kitchen.get_details()
kitchen.get_description()