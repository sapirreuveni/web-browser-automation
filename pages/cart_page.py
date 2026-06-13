from playwright.sync_api import Page
from pages.header import HeaderComp
from pages.base_page import BasePage

class CartPage(HeaderComp, BasePage):
    # add product to cart
    __ADD_TO_CART_BUTTON = ".button-group .fa-shopping-cart"
    # quantity input field
    __CHANGE_QUANTITY = ".btn-block>[value='1']"
    # update quantity button
    __UPDATE_QUANTITY_BUTTON = ".fa-refresh"
    # remove item from cart
    __DELETE_ITEM_BUTTON = ".fa-times-circle"
    # proceed to checkout
    __CHECKOUT_BUTTON = ".pull-right>.btn-primary"
    # expand / collapse cart sections
    __SECTION_TOGGLE_BUTTON = ".fa-caret-down"
    # coupon code input field
    __COUPON_FIELD = "#input-coupon"
    # apply coupon button
    __APPLY_COUPON_BUTTON = "#button-coupon"
    # country selection field
    __COUNTRY_FIELD = "#input-country"
    # zone / region selection field
    __ZONE_FIELD = "#input-zone"
    # postcode / zip code input field
    __POSTCODE_FIELD = "#input-postcode"
    # get shipping quote button
    __QUOTE_BUTTON = "#button-quote"
    # voucher code input field
    __VOUCHER_FIELD = "#input-voucher"
    # apply voucher button
    __APPLY_VOUCHER_BUTTON = "#button-voucher"
    # shipping method selection field
    __SELECT_SHIPPING_METHOD = "[name='shipping_method']"
    # apply selected shipping method
    __APPLY_SHIPPING_BUTTON = "[value='Apply Shipping']"

    def __init__(self, page: Page):
        super().__init__(page)

    def shopping_cart(self, number,coupon,post_code, gift_code,country_value,value2):
        self.click(self.__ADD_TO_CART_BUTTON,1)
        self.cart()
        self.fill_text(self.__CHANGE_QUANTITY,number)
        self.click(self.__UPDATE_QUANTITY_BUTTON)

        self.click(self.__SECTION_TOGGLE_BUTTON,1)
        self.fill_text(self.__COUPON_FIELD,coupon)
        self.click(self.__APPLY_COUPON_BUTTON)

        self.click(self.__SECTION_TOGGLE_BUTTON,2)
        self.select_option(self.__COUNTRY_FIELD,country_value)
        self.click(self.__ZONE_FIELD)
        self.select_option(self.__ZONE_FIELD,value2)
        self.fill_text(self.__POSTCODE_FIELD,post_code)
        self.click(self.__QUOTE_BUTTON)
        self.click(self.__SELECT_SHIPPING_METHOD)
        self.click(self.__APPLY_SHIPPING_BUTTON)

        self.click(self.__SECTION_TOGGLE_BUTTON,3)
        self.fill_text(self.__VOUCHER_FIELD,gift_code)
        self.click(self.__APPLY_VOUCHER_BUTTON)
        self.click(self.__CHECKOUT_BUTTON)
        self.click(self.__DELETE_ITEM_BUTTON)

    def get_number_item(self):
        area_list=self.page.locator("")
        return  area_list.count()

    def clear_cart(self):
        self.page.goto("https://tutorialsninja.com/demo/index.php?route=checkout/cart")
        self.page.wait_for_load_state("domcontentloaded")
        while True:
            delete_buttons = self.page.locator(self.__DELETE_ITEM_BUTTON)
            if delete_buttons.count() == 0:
                break
            delete_buttons.first.click()
            self.page.wait_for_load_state("domcontentloaded")
        self.go_home()