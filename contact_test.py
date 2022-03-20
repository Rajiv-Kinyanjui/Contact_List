import unittest #Importing the unittest module
from contact import Contact

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

if __name__ == '__main__':
    unittest.main()