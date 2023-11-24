from lib.diary import *

class Contacts():
    def __init__(self):
        self.phone_numbers = {}

    def all_contacts(self, diary):
        all_entries = diary.all_entries()

        for entry in all_entries:
            if entry.contact_name or entry.contact_number != None:
                self.phone_numbers[entry.contact_name] = entry.contact_number
        
        return self.phone_numbers