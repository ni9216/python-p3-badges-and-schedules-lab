def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    names = ['Guido', 'Edsger', 'Ada', 'Charles', 'Alan', 'Grace', 'Linus','Matz']
    rooms = range(1,9)
    room_assignment = []
    for i, name in enumerate (names):
        rooms_message = f"Hello, {name}! You'll be assigned to room {rooms[i]}!"
        room_assignment.append(rooms_message)
    return room_assignment

def printer(names):
    badge = batch_badge_creator(names)
    room_assign = assign_rooms(names)
    for badges in badge:
        print(badges)
    for rooms_assigned in room_assign:
        print(rooms_assigned)
    