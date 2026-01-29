class StudyRoom:
    __rooms__ = [] #attribute
    def __init__(self, room_id, hours):
        self.room_id = room_id
        self.hours = hours
        self.logs = {}

    def start_session(self, stundet):
        self.logs[stundet] = "Oturum başladı."

    def end_session(self, stundet, used_hours):
        self.hours -= used_hours #Hours __init__'içinde tanımlamış. oradaki değerden düşüyor.
        self.logs[stundet] = "Oturum sona erdi."

    def remaining_hours(self):
        return self.hours

    def reserve(self,student, hours):
        if hours <= 3:
            if hours <= self.hours:
                return True
            else:
                return False
        else:
            print("Maksimum 3saat reserve edebilirsiniz")