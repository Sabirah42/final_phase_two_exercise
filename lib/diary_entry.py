class DiaryEntry():
    def __init__(self, title=None, contents=None, contact_name=None, contact_number=None):
        self.title = title
        self.contents = contents
        self.contact_name = contact_name
        self.contact_number = contact_number

    def format(self):
        return f'{self.title}: {self.contents}'