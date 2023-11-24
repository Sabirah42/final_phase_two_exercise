from lib.diary import *
from lib.diary_entry import *
from lib.todo import *
from lib.contacts import *


def test_all_entries_returns_all_added_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Day One", "Today was a good day.")
    entry_2 = DiaryEntry("Day Two", "Today was not so great.")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)

    assert diary.all_entries() == [entry_1, entry_2]

def test_all_tasks_returns_all_added_todos():
    diary = Diary()
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do dishes")
    diary.add_todo(todo_1)
    diary.add_todo(todo_2)

    assert diary.all_tasks() == [todo_1, todo_2]

def test_all_tasks_returns_only_incomplete_todos():
    diary = Diary()
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do dishes")
    diary.add_todo(todo_1)
    diary.add_todo(todo_2)
    todo_1.mark_completed()

    assert diary.all_tasks() == [todo_2]

def test_contacts_adds_contacts_from_diary_entry():
    contacts = Contacts()
    DiaryEntry("Day One", "Today was a good day.")
    DiaryEntry("Day Two", "Got Max's phone number today!", "Max Miller", "07654863902")

    assert contacts.list_numbers() == {"Max Miller": "07654863902"}  


# Still to do:
# entry given time and reading speed
# all of Contacts class
# exceptions
