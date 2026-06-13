from playwright.sync_api import Page
from pages.header import HeaderComp
from pages.base_page import BasePage

class RegisterPage(HeaderComp, BasePage):
    # first name input field
    __FIRST_NAME_FIELD = "#input-firstname"
    # last name input field
    __LAST_NAME_FIELD = "#input-lastname"
    # email input field
    __EMAIL_FIELD = "#input-email"
    # telephone input field
    __TELEPHONE_NUMBER_FIELD = "#input-telephone"
    # password input field
    __PASSWORD_FIELD = "#input-password"
    # confirm password input field
    __PASSWORD_CONFIRM_FIELD = "#input-confirm"
    # agree to terms checkbox
    __AGREE_CHECKBOX = "input[type='checkbox'][name='agree']"
    # success message after account creation
    __SUCCESS_MESSAGE="#content h1"
    # Error message displayed when account creation fails
    __ERROR_MESSAGE=".alert-dismissible"
    # input[type='checkbox'][name='agree']

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_info(self, first_name, last_name, email, telephone, password, password_Confirm):
        self.crate_user()
        self.fill_text(self.__FIRST_NAME_FIELD, first_name)
        self.fill_text(self.__LAST_NAME_FIELD, last_name)
        self.fill_text(self.__EMAIL_FIELD, email)
        self.fill_text(self.__TELEPHONE_NUMBER_FIELD, telephone)
        self.fill_text(self.__PASSWORD_FIELD, password)
        self.fill_text(self.__PASSWORD_CONFIRM_FIELD, password_Confirm)
        self.force_check_checkbox(self.__AGREE_CHECKBOX)
        self.continue_bth()

    def get_success_message(self):
        text= self.get_text(self.__SUCCESS_MESSAGE)
        return self.clean_text(text)

    def get_error_message(self):
        text= self.get_text(self.__ERROR_MESSAGE)
        return self.clean_text(text)
