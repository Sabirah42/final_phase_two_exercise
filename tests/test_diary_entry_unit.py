from lib.diary_entry import *

def test_diary_entry_initialises_with_title_and_contents():
    entry = DiaryEntry("Day One", "Today was a good day.")

    assert entry.title == "Day One"
    assert entry.contents == "Today was a good day."

def test_diary_entry_formats():
    entry = DiaryEntry("Day One", "Today was a good day.")

    assert entry.format() == "Day One: Today was a good day."

def test_diary_entry_accepts_contact_name_and_num():
    entry_1 = DiaryEntry("Day One", "Today was a good day.")
    entry_2 = DiaryEntry("Day Two", "Got Max's phone number today!", "Max Miller", "07654863902")

    assert entry_1.contact_name == None
    assert entry_1.contact_number == None
    assert entry_2.contact_name == "Max Miller"
    assert entry_2.contact_number == "07654863902"