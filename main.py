from room import Room
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_room = Room("Dining Room")
dining_room.set_description("an empty room with badly set up tables.")

ballroom = Room("ballroom")
ballroom.set_description("A gross place with fleas dancing in a circle to Micheal Jackson's Pretty Young Thing")


kitchen.link_room(dining_room, "south")
ballroom.link_room(dining_room, "east")
dining_room.link_room(ballroom, "west")
dining_room.link_room(kitchen, "north")


current_room = kitchen


#dining_room.get_details()
#ballroom.get_details()
#kitchen.get_details()

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")   
    current_room = current_room.move(command)  
 
