from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.header import HeaderComp

class LoginPage(HeaderComp, BasePage):
    # email input field
    __EMAIL_FIELD = "#input-email"
    # password input field
    __PASSWORD_FIELD = "#input-password"
    # login submit button
    __LOGIN_BUTTON = "[value='Login']"
    # error message shown when login fails
    __ERROR_MESSAGE=".alert-dismissible"
    # success message header after successful login
    __SUCCESS_MESSAGE="#content> h2:nth-child(1)"

    def __init__(self, page: Page):
     super().__init__(page)

    def login(self , email ,password):
        self.login_in()
        self.fill_text(self.__EMAIL_FIELD, email)
        self.fill_text(self. __PASSWORD_FIELD, password)
        self.click(self.__LOGIN_BUTTON)

    def get_error_message(self):
         text= self.get_text(self. __ERROR_MESSAGE)
         return self.clean_text(text)

    def get_pass_message(self):
         text= self.get_text(self. __SUCCESS_MESSAGE)
         return self.clean_text(text)






