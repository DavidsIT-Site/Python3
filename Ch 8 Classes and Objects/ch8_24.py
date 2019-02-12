# making classes support comparison operations

from functools import total_ordering

class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width

@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(room.square_feet for room in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}: {} square footage {}'.format(self.name, self.style, self.living_space_footage)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


h1 = House('house 1', 'akers')
h1.add_room(Room('Master', 12, 5))
h1.add_room(Room('Bathroom', 5, 5))
h1.add_room(Room('Kitchen', 12, 5))

h2 = House('House 2', 'ranch')
h2.add_room(Room('Marks', 100, 1000))

h3 = House('hjouse 3', 'spaceship')
h3.add_room(Room('startship1', 200, 10000))

print(h1,'\n',h2)

houses = [h1, h2, h3]

print('Which one is biggest?', max(houses))
print('Which is smallest?', min(houses))

# total_ordering literally defines a map‐ping from each of the
# comparison-supporting methods to all of the other ones that
# would be required.