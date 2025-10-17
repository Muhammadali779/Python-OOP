class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        if not self.is_active:
            self.is_active = True
            print(f"Foydalanuchi: {self.username} Aktiv holatga o`tdi ✅")
        

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            print(f"Foydalanuchi: | {self.username} | No Aktiv holatga o`tkazildi ❌")

user1 = User("Eshmatov_B", "eshmatov007@gmail.com", True)
user2 = User("Toshmatov_A", "toshmatovvv@gmail.com", False)
user3 = User("Xikmatov_Legenda", "legendaaaa@gmail.com", True)

users = (user1, user2, user3)

for i in users:
    i.activate()
    #i.deactivate()