from tests.base_test import BaseTest

class TestCart(BaseTest):

    def test_00_navigate_to_home_page(self):
     self.my_account_page.go_home()

    def test_01_cart(self):
     self.cart_page.shopping_cart("2", "1224", "12121", "212121","China","Hunan")


