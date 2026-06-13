import pytest
from pages.cart_page import CartPage
from pages.contact_details_page import ContactPage
from pages.create_profile_page import RegisterPage
from pages.login_page import LoginPage
from pages.my_account_page import MainPage
from pages.my_wish_list_page import WishListPage
from pages.products_page import ProductPage
from utils.config_reader import ConfigReader

@pytest.fixture(scope="class", autouse=True)
def setup_page_class(request, browser):
    request.cls.page = browser.new_page()
    request.cls.page.goto("https://tutorialsninja.com/demo/index.php")
   #User login
    request.cls.login_page = LoginPage(request.cls.page)
    email = ConfigReader.read_config("general", "email")
    password = ConfigReader.read_config("general", "password")
    request.cls.login_page.login(email, password)
    request.cls.cart_page = CartPage(request.cls.page)
    request.cls.contact_details_page=ContactPage(request.cls.page)
    request.cls.create_profile_page=RegisterPage(request.cls.page)
    request.cls.my_account_page=MainPage(request.cls.page)
    request.cls.my_wish_list_page=WishListPage(request.cls.page)
    request.cls.products_page=ProductPage(request.cls.page)
    yield
    request.cls.page.close()



