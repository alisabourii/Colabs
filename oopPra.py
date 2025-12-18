class campusCard:
    #  class attributes
    __cards__ = []

    def __init__(self, name:str, balance:int,typeOFCard="StundetCard"):
        """
            :param name:Input Name
            :param balance: Your Debit
            :param typeOFCard: Card Type(defualt="StundetCard"). Choice "StundetCard", "StaffCard" or "GeustCard".
        """
        self.name = name
        self.balance = balance
        self.typeOFCard = typeOFCard
        self.transactions = []

        campusCard.__cards__.append(self)

    def get_all_cards(self):
        return campusCard.__cards__

    def load_money(self, amount:int):
        self.balance += amount
        self.transactions.append(amount)

    def spend_money(self, amount:int):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("You don't have enough money")

    def get_balance(self):
        return self.balance

    def transfer_to(self,otherCard, amount:int):
        if self.balance >= amount:
            self.balance -= amount
            otherCard.load_money(amount)

    def total_mony_in_System(self=None)-> int | float:
        att = campusCard.get_all_cards("")
        total = 0
        for i in range(len(att)):
            total += att[i].balance
        return total



std = campusCard("Ali SABOURI",100, "StundetCard")
staff = campusCard("Abdullah BALCI",200, "StaffCard")
guest = campusCard("Kayra ÖZDEMİR",50, "GeustCard")

std.load_money(100)
print("Ali New Balance: ",std.get_balance())

std.transfer_to(guest, 50)
print("Ali New Balance2: ",std.get_balance())
print("guest new Balance:", guest.get_balance())

guest.spend_money(100)
guest.spend_money(100) # Control Done!!-> You don't have enough money

totaly = campusCard.total_mony_in_System()
print("System Totaly: ",totaly)
