import pytest
from playwright.sync_api import Page
from pages.base_page import BasePage


class HeaderComp(BasePage):
    # loginRegister
    __TOP_BAR_MY_ACCOUNT_BTN=".list-inline >li  .dropdown-toggle"
    __TOP_BAR_LOGIN_BTN = ".dropdown-menu.dropdown-menu-right>li"
    __TOP_BAR_LOGOUT_BTN=".dropdown-menu-right :nth-child(5)"
    # register (top bar)
    __TOP_BAR_REGISTER_BTN="#top-links > ul > li.dropdown.open > ul > li:nth-child(1)"
    # contact (top bar)
    __TOP_BAR_CONTACT_BTN  = ".fa-phone"
    #home
    __HOME_BTN = ".breadcrumb  .fa-home"
    # likes / wishlist (top bar)
    __TOP_BAR_WISHLIST_BTN = "#wishlist-total"
    # checkout (top bar)
    __TOP_BAR_CHECKOUT_BTN = ".fa-share"
    # cart (top bar)
    __TOP_BAR_CART_BTN ="#top-links > ul > li:nth-child(4) > a > i"
    # CONTINUE (not top bar)
    __CONTINUE_BTN = "#content .btn-primary"
    #search
    __SEARCH_FIELD = ".input-lg"
    __SEARCH_BTN = ".btn-default.btn-lg"
    # search error message
    __SEARCH_ERROR_MESSAGE = "#content > p:nth-child(7)"

    def __init__(self, page: Page):
        super().__init__(page)

    def login_in(self):
        self.click(self.__TOP_BAR_MY_ACCOUNT_BTN)
        self.click(self.__TOP_BAR_LOGIN_BTN ,1)

    def long_out(self):
        self.click(self.__TOP_BAR_MY_ACCOUNT_BTN)
        self.click(self.__TOP_BAR_LOGOUT_BTN)

    def crate_user(self):
        self.click(self.__TOP_BAR_MY_ACCOUNT_BTN)
        self.click(self.__TOP_BAR_REGISTER_BTN,0)

    def contact_in(self):
        self.click(self.__TOP_BAR_CONTACT_BTN)
        self.page.locator("h1").filter(has_text="Contact Us").wait_for(timeout=5000)

    def open_contact(self):
        self.page.goto(
            "https://tutorialsninja.com/demo/index.php?route=information/contact"
        )
        self.page.get_by_role("heading", name="Contact Us").wait_for(timeout=5000)


    def back_home(self):
        self.click(self.__HOME_BTN)

    def go_home(self):
        self.page.goto("https://tutorialsninja.com/demo/index.php?route=common/home")
        self.page.wait_for_load_state(timeout=10000)

    def checkout(self):
        self.click(self.__TOP_BAR_CHECKOUT_BTN)

    def cart(self):
        self.click(self.__TOP_BAR_CART_BTN)

    def continue_bth(self):
        self.click(self.__CONTINUE_BTN)


    def search_bar(self, word):
        self.fill_text(self.__SEARCH_FIELD, word)
        self.click(self.__SEARCH_BTN)

    def get_search_error_message(self):
        return self.get_text(self.__SEARCH_ERROR_MESSAGE)

    def go_to_wishlist(self):
        self.page.goto("https://tutorialsninja.com/demo/index.php?route=account/wishlist" )
        self.page.wait_for_load_state("domcontentloaded")

    def navigate_to_likes_table(self):
        self.click(self.__TOP_BAR_WISHLIST_BTN)




