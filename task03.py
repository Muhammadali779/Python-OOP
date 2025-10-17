class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

user1 = User("Eshmatov_B", "eshmatov007@gmail.com", True)
user2 = User("Toshmatov_A", "toshmatovvv@gmail.com", False)
user3 = User("Xikmatov_Legenda", "legendaaaa@gmail.com", True)

users = (user1, user2, user3)

for user in users:
    print(f"UserName: {user.username} || Email: {user.email} || Is Active: {user.is_active}")