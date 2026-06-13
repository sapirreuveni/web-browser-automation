import pytest
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


@pytest.mark.usefixtures("setup_page_class")
class TestWishlist(BaseTest):

      __PRODUCT_NAME = ConfigReader.read_config("general", "product")

      def test_00_navigate_to_home_page(self):
            self.my_account_page.go_home()

      def test_01_add_to_cart_from_wishlist(self):
            self.products_page.add_product_to_wishlist(self.__PRODUCT_NAME)
            self.my_wish_list_page.add_product_to_cart_from_wishlist()

            a=self.my_wish_list_page.get_product_name()
            actual_result = self.my_wish_list_page.get_pass_message()
            expected_result = f"You have added {a} to your shopping cart!"
            assert actual_result == expected_result

      def test_02_remove_from_wishlist(self):
            self.my_wish_list_page.remove_product_from_wishlist()
            expected_result = "You have modified your wish list!"
            actual_result = self.my_wish_list_page.get_pass_message()
            assert actual_result == expected_result


      def test_03_continue(self):
            self.my_wish_list_page.click_continue_button()
            expected_result ="My Account"
            actual_result = self.my_wish_list_page.get_my_account_text()
            assert actual_result == expected_result








