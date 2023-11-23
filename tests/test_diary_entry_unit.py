from lib.diary_entry import *

def test_diary_entry_initialises_with_title_and_contents():
    entry = DiaryEntry("Day One", "Today was a good day.")

    assert entry.title == "Day One"
    assert entry.contents == "Today was a good day."

def test_diary_entry_formats():
    entry = DiaryEntry("Day One", "Today was a good day.")

    assert entry.format() == "Day One: Today was a good day."