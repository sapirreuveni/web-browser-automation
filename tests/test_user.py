from tests.base_test import BaseTest
from utils.data_generator import (
    generate_random_email,
    generate_random_first_name,
    generate_random_last_name,
    generate_random_phone,
    generate_random_password
)

class TestUser(BaseTest):

  def test_00_logout(self):
       self.my_account_page.log_out()

  def test_01_create_user_pass(self):
      email = generate_random_email()
      first_name = generate_random_first_name()
      last_name = generate_random_last_name()
      phone = generate_random_phone()
      password = generate_random_password()
      self.create_profile_page.fill_info(first_name,last_name,email,phone,password,password)
      expected_result = "Your Account Has Been Created!"
      actual_result = self.create_profile_page.get_success_message()
      assert actual_result == expected_result

  def test_02_create_a_user_with_an_existing_email(self):
      self.my_account_page.log_out()
      self.create_profile_page.fill_info("עדי", "שמאל", "Adi12345@gmail.com", "053445445", "123456", "123456")
      expected_result = "E-Mail Address is already registered!"
      actual_result = self.create_profile_page.get_error_message()
      assert actual_result == expected_result
