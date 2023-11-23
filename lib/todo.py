class Todo():
    def __init__(self, task):
        self.task = task
        self.complete = False

    def mark_completed(self):
        self.complete = True