from tests.base_test import BaseTest

class TestSearch(BaseTest):

    def test_01_search_incorrect(self):
        self.my_account_page.search_bar("good")
        expected_result = "There is no product that matches the search criteria."
        actual_result = self.my_account_page.get_search_error_message()
        assert actual_result == expected_result


