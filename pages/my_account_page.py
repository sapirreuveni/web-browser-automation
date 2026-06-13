from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.header import HeaderComp

class MainPage(HeaderComp,BasePage):
    # edit account button in the sidebar
    __SIDE_BAR_EDIT_ACCOUNT_BTN = ".list-group-item:nth-child(2)"
    # Change account password button
    __SIDE_BAR_CHANGE_PASSWORD_BTN = ".list-group-item:nth-child(3)"
    # Newsletter subscription settings button
    __SIDE_BAR_NEWSLETTER_BTN = ".list-group-item:nth-child(12)"
    # Logout button from account
    __SIDE_BAR_LOGOUT_BTN = ".list-group-item:nth-child(13)"
    # Address book management button
    __SIDE_BAR_ADDRESS_BOOK_BTN = ".list-group-item:nth-child(4)"
    # First name input field
    __NAME_FIELD="#input-firstname"
    # Last name input field
    __LAST_NAME_FIELD="#input-lastname"
    # Email input field
    __EMAIL_FIELD="#input-email"
    # Telephone number input field
    __TELEPHONE_FIELD="#input-telephone"
    # Error message text (validation errors)
    __ERROR_MESSAGE="text-danger"
    # Success alert message after successful action
    __SUCCESS_MESSAGE=".alert-success"
    # New password input field
    __PASSWORD_FIELD="#input-password"
    # Confirm password input field
    __CONFIRM_PASSWORD_FIELD="#input-confirm"
    # Subscribe to newsletter - Yes option
    __NEWSLETTER_YES=".radio-inline [value='1']"
    # Subscribe to newsletter - No option
    __NEWSLETTER_NO=".radio-inline [value='0']"
    # Success message displayed after personal details are updated
    __DETAILS_UPDATED_SUCCESS_MESSAGE = ".alert.alert-success"
    # Continue button displayed after successful account details update
    __DETAILS_UPDATE_CONTINUE_BUTTON="[value='Continue']"

    def __init__(self, page: Page):
        super().__init__(page)



    def get_personal_details(self):
        return {
                "name": self.page.locator("#input-firstname").input_value().strip(),
                "email": self.page.locator("#input-email").input_value().strip(),
                "lastname": self.page.locator("#input-lastname").input_value().strip(),
                "telephone": self.page.locator("#input-telephone").input_value().strip(),
            }

    def reload_page(self):
            self.page.reload()

    def change_personal_details(self,name,email,lastname,telephone):
        self.fill_text(self.__NAME_FIELD,name)
        self.fill_text(self.__LAST_NAME_FIELD,lastname)
        self.fill_text(self.__EMAIL_FIELD,email)
        self.fill_text(self.__TELEPHONE_FIELD,telephone)
        self.click_details_update_continue_btn()

    def change_password(self,password):
        self.click(self.__SIDE_BAR_CHANGE_PASSWORD_BTN)
        self.fill_text(self.__PASSWORD_FIELD,password)
        self.fill_text(self.__CONFIRM_PASSWORD_FIELD,password)
        self.continue_btn()

    def long_out_by_side_bar(self):
        self.click(self.__SIDE_BAR_LOGOUT_BTN)
        self.continue_btn()

    def newsletter(self,value):
        self.click(self.__SIDE_BAR_NEWSLETTER_BTN)
        if value=="no":
            self.click(self.__NEWSLETTER_NO)
            self.continue_btn()

        else:
            self.click(self.__NEWSLETTER_YES)
            self.continue_btn()

    def update_success_message(self):
        text = self.get_text(self.__DETAILS_UPDATED_SUCCESS_MESSAGE)
        return self.clean_text(text)

    def navigate_to_personal_details_from_sidebar(self):
        self.click(self.__SIDE_BAR_EDIT_ACCOUNT_BTN)

    def click_details_update_continue_btn(self):
       return self.click(self.__DETAILS_UPDATE_CONTINUE_BUTTON)








