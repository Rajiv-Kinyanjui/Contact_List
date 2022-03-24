#!/usr/bin/env python3.6
from operator import truediv
from contact import Contact

#Creating a contact
def create_contact(fname, lname, phone, email):
    '''
    function to create a new contact
    '''
    new_contact = Contact(fname, lname, phone, email)

    return new_contact


#Save contacts
def save_contacts(contact):
    '''
    function to save contact
    '''
    contact.save_contact()


#Delete contact
def del_contact(contact):
    '''
    function to delete contacts
    '''
    contact.delete_contact()


#Finding a contact
def find_contact(number):
    '''
    Functions that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)


#Check if contact exists
def check_existing_contacts(number):
    '''
    function that checks if a contact exists with that number and returns a boolean
    '''
    return Contact.contact_exist(number)


#Displaying all contacts
def display_contact():
    '''
    Function that returns all saved contacts
    '''
    return Contact.display_contacts()




#Main function
def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    