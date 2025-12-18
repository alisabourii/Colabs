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
        self.transactions = {}

        campusCard.__cards__.append(self)

    def get_all_cards(self=None):
        return campusCard.__cards__
    def get_all_transactions(self):
        return self.transactions

    def load_money(self, amount:int):
        self.balance += amount
        self.transactions["input money"] = amount

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
            self.transactions["Money Transfer (-)"] = amount
            otherCard.transactions["Money Transfer (+)"] = amount

    def total_mony_in_System(self=None)-> int | float:
        att = campusCard.get_all_cards()
        total = 0
        for i in range(len(att)):
            total += att[i].balance
        return total

    def canteen(self, order):
        menu = {"tost": 120, "pilav":100, "kola":40,"soda":20}
        orderPaymnet = menu[order]
        if self.typeOFCard == "StundetCard":
            orderPaymnet -= orderPaymnet*0.15
        elif self.typeOFCard == "StaffCard":
            orderPaymnet -= orderPaymnet*0.10

        if self.balance >= orderPaymnet:
            self.balance -= orderPaymnet
        else:
            print("You don't have enough money")

    def refectory(self):
        orderPaymnet = 32
        if self.typeOFCard == "StundetCard":
            orderPaymnet -= orderPaymnet * 0.15
        elif self.typeOFCard == "StaffCard":
            orderPaymnet -= orderPaymnet * 0.10

        if self.balance >= orderPaymnet:
            self.balance -= orderPaymnet
        else:
            print("You don't have enough money")

    def stationary(self, order):
        menu = {"pen": 50, "pencel": 20, "dilgi": 60, "defter": 20}
        orderPaymnet = menu[order]
        if self.typeOFCard == "StundetCard":
            orderPaymnet -= orderPaymnet * 0.15

        if self.balance >= orderPaymnet:
            self.balance -= orderPaymnet
        else:
            print("You don't have enough money")

    def ride_minibus(self):
        paymentFee = 30
        if self.typeOFCard == "StundetCard":
            paymentFee = 25

        if self.balance >= paymentFee:
            self.balance -= paymentFee

        self.transactions["Minibus fee"] = paymentFee


std = campusCard("Ali SABOURI",100, "StundetCard")
staff = campusCard("Abdullah BALCI",200, "StaffCard")
guest = campusCard("Kayra ÖZDEMİR",50, "GeustCard")

# Zorunlu Bölümler test

std.load_money(100)
print("Ali New Balance: ",std.get_balance())

std.transfer_to(guest, 50)
print("Ali New Balance2: ",std.get_balance())
print("guest new Balance:", guest.get_balance())

guest.spend_money(100)
guest.spend_money(100) # Control Done!!-> You don't have enough money

totaly = campusCard.total_mony_in_System()
print("System Totaly: ",totaly)


#Kantin Test
order = "tost"
std.load_money(50)
std.canteen(order)
staff.canteen(order)
print("Ali New Balance: ", std.get_balance())
print("Abdullah New Balance: ", staff.get_balance())

#Yemekhane Test
std.refectory()
staff.refectory()
guest.refectory()
print("Ali New Balance: ", std.get_balance())
print("Abdullah New Balance: ", staff.get_balance())
print("kayra New Balance: ", guest.get_balance())

#Kırtasite Test
order = "pencel"
std.stationary(order)
staff.stationary(order)
guest.stationary(order)
print("Ali New Balance: ", std.get_balance())
print("Abdullah New Balance: ", staff.get_balance())
print("kayra New Balance: ", guest.get_balance())

#Minibus Test
std.ride_minibus()
print("Ali New Balance: ", std.get_balance())
staff.ride_minibus()
print("Abdullah New Balance: ", staff.get_balance())

# Transactions Test
print("----------------------")
print(std.get_all_transactions())
print(staff.get_all_transactions())
print(guest.get_all_transactions())
