class User:
    def __init__(self, user_id):
        self._id = user_id
    @property
    def id(self):
        return self._id
user = User(220207)
print(f"User ID: {user.id}")