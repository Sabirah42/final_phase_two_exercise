from lib.todo import *

def test_todo_initalises_with_todo_and_false_complete_attribute():
    todo = Todo("Do laundry")

    assert todo.task == "Do laundry"
    assert todo.complete == False

def test_todo_tasks_can_be_marked_complete():
    todo_1 = Todo("Do laundry")
    todo_1.mark_completed()

    assert todo_1.complete == True