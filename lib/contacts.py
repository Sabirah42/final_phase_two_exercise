from lib.diary_entry import *

class Contacts():
    def __init__(self):
        self.phone_numbers = {}

    def list_numbers(self):
        if DiaryEntry().contact_name or DiaryEntry().contact_number != None:
            self.phone_numbers[DiaryEntry().contact_name] = DiaryEntry().contact_number
        
        return self.phone_numbers