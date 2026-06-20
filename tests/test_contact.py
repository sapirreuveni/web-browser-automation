from tests.base_test import BaseTest

class TestContact(BaseTest):

    def test_01_contact_success(self):
        self.contact_details_page.fill_info_contact("עדי", "Adi12345@gmail.com","this is a valid enquiry text")
        expected_result = "Contact Us"
        actual_result = self.contact_details_page.get_pass_message()
        assert actual_result == expected_result

    def test_02_contact_failed(self):
        self.contact_details_page.fill_info_contact("", "Adi12345@gmail.com", "this is a valid enquiry text" )
        expected_result = "Name must be between 3 and 32 characters!"
        actual_result = self.contact_details_page.get_error_message_name()
        assert actual_result == expected_result

    def test_03_contact_failed(self):
        self.contact_details_page.fill_info_contact("עדי", "Adi12345gmail.com", "this is a valid enquiry text" )
        expected_result = "E-Mail Address does not appear to be valid!"
        actual_result = self.contact_details_page.get_error_message_email()
        assert actual_result == expected_result

    def test_04_contact_failed(self):
       self.contact_details_page.fill_info_contact("עדי", "Adi12345@gmail.com", "n")
       expected_result = "Enquiry must be between 10 and 3000 characters!"
       actual_result = self.contact_details_page.get_error_message_enquiry()
       assert actual_result == expected_result





