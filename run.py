#!/usr/bin/env python3.6
from contact import Contact

def create_contact(fname, lname, phone, email):
    '''
    function to create a new contact
    '''
    new_contact = Contact(fname, lname, phone, email)

    return new_contact

def save_contacts(contact):
    '''
    function to save contact
    '''
    contact.save_contact()

