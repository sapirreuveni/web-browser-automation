from tests.base_test import BaseTest
from utils.config_reader import ConfigReader

class TestPersonalDetails(BaseTest):

    def test_00_reset_details(self):
        email = ConfigReader.read_config("general", "email")
        self.my_account_page.navigate_to_personal_details_from_sidebar()
        self.my_account_page.change_personal_details("עדי", email, "לוי", "0534545468")

    def _go_and_get_before(self):
        self.my_account_page.navigate_to_personal_details_from_sidebar()
        before = self.my_account_page.get_personal_details()
        return before

    def _reload_and_get_after(self):
        self.my_account_page.reload_page()
        self.my_account_page.navigate_to_personal_details_from_sidebar()
        after = self.my_account_page.get_personal_details()
        return after

    def test_invalid_name_should_not_save_anything(self):
        before = self._go_and_get_before()
        self.my_account_page.change_personal_details(
            "4000", before["email"], before["lastname"], before["telephone"]
        )
        after = self._reload_and_get_after()
        assert after == before

    def test_invalid_email_should_not_save_anything(self):
        before = self._go_and_get_before()
        self.my_account_page.change_personal_details(
            before["name"], "Adi12345gmail.com", before["lastname"], before["telephone"]
        )
        after = self._reload_and_get_after()
        assert after == before

    def test_invalid_lastname_should_not_save_anything(self):
        before = self._go_and_get_before()
        self.my_account_page.change_personal_details(
            before["name"], before["email"], "44656", before["telephone"]
        )
        after = self._reload_and_get_after()
        assert after == before

    def test_invalid_telephone_should_not_save_anything(self):
        before = self._go_and_get_before()
        self.my_account_page.change_personal_details(
            before["name"], before["email"], before["lastname"], "05a744!105"
        )
        after = self._reload_and_get_after()
        assert after == before

    def test_99_reset_details(self):
        email = ConfigReader.read_config("general", "email")
        self.my_account_page.navigate_to_personal_details_from_sidebar()
        self.my_account_page.change_personal_details("עדי", email, "לוי", "0534545468")