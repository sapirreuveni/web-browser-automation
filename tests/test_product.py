from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


class TestProduct(BaseTest):

    __PRODUCT_NAME = ConfigReader.read_config("general", "product")

    def test_00_navigate_to_home_page(self):
        self.my_account_page.go_home()

    def test_01_product(self):
        self.products_page.add_product(self.__PRODUCT_NAME)
        self.products_page.add_product_to_wishlist(self.__PRODUCT_NAME)
        self.products_page.product_info(self.__PRODUCT_NAME)

    def test_02_product_compare_success(self):
        self.products_page.compare_product(self.__PRODUCT_NAME)
        expected_result =f"You have added {self.__PRODUCT_NAME} to your product comparison!"
        actual_result = self.products_page.get_pass_message_compare()
        assert actual_result == expected_result

    def test_03_product_likes_count(self):
         actual_result = self.products_page.get_number_item()
         expected_result = 1
         assert actual_result == expected_result














