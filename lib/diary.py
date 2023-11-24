class Diary():
    def __init__(self):
        self.diary_entries = []
        self.tasks = []

    def add_entry(self, entry):
        self.diary_entries.append(entry)

    def all_entries(self):
        return self.diary_entries
    
    def add_todo(self, task):
        self.tasks.append(task)

    def all_tasks(self):
        incomplete_tasks = []
        for task in self.tasks:
            if task.complete == False:
                incomplete_tasks.append(task)
        return incomplete_tasks