from tests.base_test import BaseTest
from utils.data_generator import generate_random_email
from utils.config_reader import ConfigReader


class TestLogin(BaseTest):

    __EMAIL = ConfigReader.read_config("general", "email")
    __PASSWORD = ConfigReader.read_config("general", "password")

    def test_00_logout(self):
       self.my_account_page.long_out()

    def test_01_login_failed(self):
        random_email = generate_random_email()
        self.login_page.login(random_email, "123456")
        expected_result= "No match for E-Mail Address and/or Password."
        actual_result=  self.login_page. get_error_message()
        assert actual_result==expected_result

    def test_02_login_success(self):
        self.login_page.login(self.__EMAIL, self.__PASSWORD)
        expected_result = "My Account"
        actual_result =  self.login_page.get_pass_message()
        assert actual_result == expected_result








