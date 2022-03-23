from cgi import test
import unittest #Importing the unittest module
from contact import Contact
import pyperclip

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours

    Args:
        unittest.Testcase: TestCase class that helps test cases
    '''
    #First Test
    def setUp(self):
        '''
        Set up method runs before each test case
        '''
        self.new_contact = Contact("James","Muriuki", "0712345678", "james@ms.com") #Create contact object

    def test_init(self):
        '''
        test_init test case to test if the object in initiatted proberly
        '''
        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0712345678")
        self.assertEqual(self.new_contact.email, "james@ms.com")


    def tearDown(self):
        '''
        teardown method that does clean up after each test case has run
        '''
        Contact.contact_list = []


    #second test
    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into the contact list
        '''
        self.new_contact.save_contact() #saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

    #third test
    def test_save_multiple_contact(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact objects to our contact_list
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711345678", "test@user.com") #new contact
        test_contact.save_contact()

        self.assertEqual(len(Contact.contact_list),2)


    #fourth test
    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact_list
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711345678", "test@user.com") #new contact
        test_contact.save_contact()

        self.new_contact.delete_contact() #Deleting a contact object
        self.assertEqual(len(Contact.contact_list),1)


    #fifth test
    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display infomation
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711345678", "test@user.com") #new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711345678")
        self.assertEqual(found_contact.email,test_contact.email)

    #sixth test
    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the contact
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711345678", "test@user.com")#new contact
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("0711345678")
        
        self.assertTrue(contact_exists)

    #seventh test
    def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts saved
        '''
        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

    #8th test
    def test_copy_email(self):
        '''
        test to confirm that we are copying the email address from a found contact
        '''
        self.new_contact.save_contact()
        Contact.copy_email("0711345678")

        self.assertEqual(self.new_contact.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()