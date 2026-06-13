from playwright.sync_api import Page
from pages.header import HeaderComp
from pages.base_page import BasePage

class WishListPage(HeaderComp, BasePage):
    # remove product button
    __REMOVE_PRODUCT="[data-original-title='Remove']"
    # add product to cart button
    __ADD_TO_CART_BUTTON="[data-original-title='Add to Cart']"
    # continue button (to proceed to next step)
    __CONTINUE_BUTTON=".pull-right   .btn-primary"
    # success message shown after action is completed
    __SUCCESS_MESSAGE=" .alert-success"
    # product name link/text
    __PRODUCT_NAME="#content .table-responsive tbody tr td.text-left a"
    # Locator for the "My Account" page main heading
    __MY_ACCOUNT_TEXT="#content >h2:nth-child(1)"

    def __init__(self, page: Page):
        super().__init__(page)

    def add_product_to_cart_from_wishlist(self):
        self.go_to_wishlist()
        self.click(self.__ADD_TO_CART_BUTTON)

    def remove_product_from_wishlist(self):
        self.go_to_wishlist()
        self.click(self.__REMOVE_PRODUCT)

    def click_continue_button(self):
        self.continue_bth()

    def get_pass_message(self):
        text= self.get_text(self.__SUCCESS_MESSAGE)
        return self.clean_text(text)

    def get_product_name(self):
        return self.get_text(self.__PRODUCT_NAME)

    def get_my_account_text(self):
        return self.get_text(self.__MY_ACCOUNT_TEXT)





