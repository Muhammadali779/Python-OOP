class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so`m deposit qilindi. Yangi balans: {round(self.balance, 2)} so`m.")
        else:
            print("❌ Summani to`g`ri kiriting!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so`m yechildi. Qolgan balans: {round(self.balance, 2)} so`m.")
        else:
            print("Balansda yetarli mablag` yo`q!")


owner_name = input("Hisob egasining ismini kiriting: ")
start_balance = float(input("Boshlang`ich balansni kiriting: "))
account = BankAccount(owner_name, start_balance)

while True:
    print("\n--- Bank Amallari ---")
    print("1. Deposit qilish")
    print("2. Pul yechish")
    print("3. Chiqish")

    choice = input("Tanlovni kiriting (1 /2 /3 ): ")

    if choice == "1":
        amount = float(input("Qancha summa deposit qilmoqchisiz: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Qancha summa yechmoqchisiz: "))
        account.withdraw(amount)

    elif choice == "3":
        print("Dastur yakunlandi!")
        break

    else:
        print("❌ Noto`g`ri tanlov! 1, 2 yoki 3 ni tanlang.")
