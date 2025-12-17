class campusCard:
    def __init__(self, name, number, typeOFCard):
        self.name = name
        self.number = number
        self.typeOFCard = typeOFCard

    def debbit(self):
        pass

    def get_all_accounts(self):
        return Account.__accounts__
