import pyperclip


class Contact:
    """
    Class that generates new instances of contacts
    """

    contact_list = [] #Empty contact list

    def __init__(self, first_name, last_name, phone_number, email):
        """
        __init__ method that helps us define propertes for our objects.

        Args:
            first_name: New contact first name.
            last_name: New contact last name.
            phone_number: New contact phone number.
            email: New contact email
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    

    def save_contact(self):
        '''
        save_contact saves contact objects into contact_list
        '''
        Contact.contact_list.append(self)

    def delete_contact(self):
        '''
        delete_contact method deletes a saved contact from the contact list
        '''
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        method that takes in a number and returns a contact matches that number.

        Args:
            number:Phone number to search for
        returns:
            Contact of person tha tmatches the number
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exist(cls, number):
        '''
        Method that checks if a contact exists from the contact exist.
        Args:
            number: Phone number to search if it exists
        
        Returns:
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True
        return False

    @classmethod
    def display_contacts(cls):
        '''
        Method that returns the contact list
        '''
        return cls.contact_list

    
    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
