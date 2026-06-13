from playwright.sync_api import Page
from pages.header import HeaderComp
from pages.base_page import BasePage
from playwright.sync_api import expect


class ContactPage(HeaderComp, BasePage):
    # name input field
    __NAME_FIELD = "#input-name"
    # email input field
    __EMAIL_FIELD= "#input-email"
    # enquiry / message text area
    __ENQUIRY_FIELD = "#input-enquiry"
    # success message title after form is submitted
    __SUCCESS_MESSAGE ="#content h1"
    # Error message displayed when the Name field is invalid
    __NAME_ERROR_MESSAGE = "#input-name + .text-danger"
    # Error message displayed when the Email field is invalid
    __EMAIL_ERROR_MESSAGE = "#input-email + .text-danger"
    # Error message displayed when the Enquiry field is empty or invalid
    __ENQUIRY_ERROR_MESSAGE = "#input-enquiry + .text-danger"

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_info_contact(self, name ,email, enquiry):
        self.open_contact()
        self.page.fill(self.__NAME_FIELD, "")
        self.page.fill(self.__EMAIL_FIELD, "")
        self.page.fill(self.__ENQUIRY_FIELD, "")
        self.fill_text(self.__NAME_FIELD, name)
        self.fill_text(self.__EMAIL_FIELD, email)
        self.fill_text(self.__ENQUIRY_FIELD, enquiry)
        self.continue_bth()
        self.page.wait_for_load_state("networkidle", timeout=5000)

    def get_error_message_email(self):
            return self.get_text(self.__EMAIL_ERROR_MESSAGE)

    def get_error_message_name(self):
        return self.get_text(self.__NAME_ERROR_MESSAGE)

    def  get_error_message_enquiry(self):
        return self.get_text(self.__ENQUIRY_ERROR_MESSAGE)

    def get_pass_message(self):
        return self.get_text(self.__SUCCESS_MESSAGE)

