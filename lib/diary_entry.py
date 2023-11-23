class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f'{self.title}: {self.contents}'