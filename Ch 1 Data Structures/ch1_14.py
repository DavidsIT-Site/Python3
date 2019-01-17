# sorting objects without native comparison support

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
users = [User(23), User(3), User(48), User(4)]
print(users)
x = sorted(users, key=lambda u: u.user_id)
print(x)


from operator import attrgetter
x = sorted(users, key=attrgetter('user_id'))
print(x)