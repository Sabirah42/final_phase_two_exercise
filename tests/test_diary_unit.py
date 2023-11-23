from lib.diary import *

def test_diary_initialises_with_empty_list():
    diary = Diary()

    assert diary.diary_entries == []