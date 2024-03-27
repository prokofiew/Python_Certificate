__comment__ = """
Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. 
For this, you need an array which can collect and process information on the occupied/free rooms.
r - rooms
f - floors
t - buildings

The first index (0 through 2) selects one of the buildings; 
the second (0 through 14) selects the floor, 
the third (0 through 19) selects the room number. All rooms are initially free.

Tasks:
- book a room for two newlyweds: in the second building, on the tenth floor, room 14:
- release the second room on the fifth floor located in the first building:
- check if there is any vacancies on 15th floor


"""

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

__answers__ = """
    |
    |
    |
    |
    V


















# book room
rooms[1][9][13] = True
rooms[0][4][1] = True

# check availability
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
        
# The vacancy variable contains 0 if all the rooms are occupied, 
# or the number of available rooms otherwise.

"""
