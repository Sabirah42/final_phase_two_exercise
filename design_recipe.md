# Multi-Class Planned Design Recipe
 
## 1. Describe the Problem
 
    As a user
    So that I can record my experiences
    I want to keep a regular diary

    As a user
    So that I can reflect on my experiences
    I want to read my past diary entries

    As a user
    So that I can reflect on my experiences in my busy day
    I want to select diary entries to read based on how much time I have and my reading speed

    As a user
    So that I can keep track of my tasks
    I want to keep a todo list along with my diary

    As a user
    So that I can keep track of my contacts
    I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

See Final Challenge Initial Design image

Sketching more complex cases:
```python
class DiaryEntry():
    def __init__(self, title, contents, contact_name=None, contact_number=None):
        self.title = title
        self.contents = contents    
```

## 3. Create Examples as Integration Tests

Create examples of the classes being used together in different situations
and combinations that reflect the ways in which the system will be used.

**When multiple diary entries are added  
Diary returns these in a list:**  
```python
    diary = Diary
    entry_1 = DiaryEntry("Day One", "Today was a good day.")
    entry_2 = DiaryEntry("Day Two", "Today was not so great.")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)

    assert diary.all_entries() == [entry_1, entry_2]
```
**When multiple Todos are added  
Diary returns all Todos in a list**
```python
    diary = Diary()
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do dishes")
    diary.add_todo(todo_1)
    diary.add_todo(todo_2)

    assert diary.all_tasks() == [todo_1, todo_2]
```
**When multiple Todos are added  
Diary returns only incomplete Todos in a list**
```python
    diary = Diary()
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do dishes")
    diary.add_todo(todo_1)
    diary.add_todo(todo_2)
    todo_1.mark_completed()

    assert diary.all_tasks() == [todo_2]
```

~~**When a phone number is added to diary entry  
Contacts adds this to contacts list**~~
~~    entry_1 = DiaryEntry("Day One", "Today was a good day.")~~
~~    entry_2 = DiaryEntry("Day Two", "Got Max's phone number today! 07654863902.")~~

~~    assert contacts.phone_numbers == ["07654863902"]~~

**When a phone number is added to diary entry  
Contacts adds this to contacts list**
    entry_1 = DiaryEntry("Day One", "Today was a good day.")
    entry_2 = DiaryEntry("Day Two", "Got Max's phone number today!", "Max Miller", "07654863902")

    assert contacts.phone_numbers == {"Max Miller": "07654863902"}
Encode one of these as a test and move to step 4.

## 4. Create Examples as Unit Tests

Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail.

### Diary Entry Class:

**Initialises with a title and contents**
```python
    entry = DiaryEntry("Day One", "Today was a good day.")

    assert entry.title == "Day One"
    assert entry.contents == "Today was a good day."
```
**Formats diary entry**
```python
    entry = DiaryEntry("Day One", "Today was a good day.")

    assert entry.format() == "Day One: Today was a good day."
```
### Diary Class:

**Initialises with an empty list**
```python
    diary = Diary()

    assert diary.diary_entries == []
```
### Todo Class:

**Initialises with a task and False completed attribute**
```python
    todo = Todo("Do laundry")
    
    assert todo.task == "Do laundry"
    assert todo.complete == False
```
**Tasks can be marked as complete**
```python
    todo_1 = Todo("Do laundry")
    todo_2 = Todo("Do shopping")
    todo_1.mark_completed()

    assert todo_1.complete == True
```

Encode one of these as a test and move to step 5.

## 5. Implement the Behaviour

For each example you create as a test, implement the behaviour that allows the
class to behave according to your example.

Then return to step 3 until you have addressed the problem you were given. You
may also need to revise your design, for example if you realise you made a
mistake earlier.
