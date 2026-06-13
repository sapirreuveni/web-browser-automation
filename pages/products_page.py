from playwright.sync_api import Page
from pages.header import HeaderComp
from pages.base_page import BasePage

class ProductPage(HeaderComp, BasePage):
    # add product to cart button
    __ADD_PRODUCT_TO_CART_BUTTON=".button-group     .fa-shopping-cart"
    # add product to wishlist button
    __ADD_TO_WISHLIST_BUTTON = "[data-original-title='Add to Wish List']"
    # add product to compare button
    __ADD_TO_COMPARE_BUTTON  = "[data-original-title='Compare this Product']"
    # product details (item info)
    __ITEM_INFO = ".caption  a "
    # products list
    __PRODUCT_LIST=".product-layout"
    # product name text
    __PRODUCT_NAME =".caption  a"
    # success message after compare action
    __COMPARE_SUCCESS_MESSAGE =".alert-success.alert-dismissible"

    def __init__(self, page: Page):
        super().__init__(page)

    def add_product(self,name):
        areas_list = self.page.locator(self.__PRODUCT_LIST)
        for i in range(areas_list.count()):
            title_name = areas_list.nth(i).locator(self.__PRODUCT_NAME).inner_text()
            if title_name ==name:
                add_button = areas_list.nth(i).locator(self.__ADD_PRODUCT_TO_CART_BUTTON)
                add_button.click()
                break

    def add_product_to_wishlist(self,name):
        areas_list = self.page.locator(self.__PRODUCT_LIST)
        for i in range(areas_list.count()):
            title_name = areas_list.nth(i).locator(self.__PRODUCT_NAME).inner_text()
            if title_name == name:
               like_button = areas_list.nth(i).locator(self.__ADD_TO_WISHLIST_BUTTON)
               like_button.click()
               break

    def compare_product(self,name):
        areas_list = self.page.locator(self.__PRODUCT_LIST)
        for i in range(areas_list.count()):
            title_name = areas_list.nth(i).locator(self.__PRODUCT_NAME).inner_text()
            if title_name == name:
                compare_button = areas_list.nth(i).locator(self.__ADD_TO_COMPARE_BUTTON)
                compare_button.click()
                break

    def product_info(self,name):
        areas_list = self.page.locator(self.__PRODUCT_LIST)
        for i in range(areas_list.count()):
            title_name = areas_list.nth(i).locator(self.__PRODUCT_NAME).inner_text()
            if title_name == name:
                item_info_button = areas_list.nth(i).locator(self.__ITEM_INFO)
                item_info_button.click()
                self.go_home()

    def get_number_item(self):
        self.navigate_to_likes_table()  # ניווט לעמוד שבו הטבלה נמצאת
        table = self.page.locator("table.table-hover")
        table.wait_for(state="visible")
        rows = table.locator("tbody tr")
        return rows.count()

    def get_pass_message_compare(self):
        text= self.get_text(self.__COMPARE_SUCCESS_MESSAGE)
        return self.clean_text(text)




