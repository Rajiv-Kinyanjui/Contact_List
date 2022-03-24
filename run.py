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

def del_contact(contact):
    '''
    function to delete contacts
    '''
    contact.delete_contact()

def find_contact(number):
    '''
    Functions that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)

def check_existing_contacts(number):
    '''
    function that checks if a contact exists with that number and returns a boolean
    '''
    return Contact.contact_exist(number)

def display_contact():
    '''
    Function that returns all saved contacts
    '''
    return Contact.display_contacts()