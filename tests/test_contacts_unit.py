from lib.contacts import *

def test_contacts_initialises_with_empty_dictionary():
    contacts = Contacts()

    assert contacts.phone_numbers == {}