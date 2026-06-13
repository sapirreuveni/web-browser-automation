from pages.cart_page import CartPage
from pages.contact_details_page import ContactPage
from pages.create_profile_page import RegisterPage
from pages.login_page import LoginPage
from pages.my_account_page import MainPage
from pages.my_wish_list_page import WishListPage
from pages.products_page import ProductPage


class BaseTest:
   cart_page : CartPage
   login_page : LoginPage
   contact_details_page : ContactPage
   create_profile_page : RegisterPage
   products_page : ProductPage
   my_wish_list_page : WishListPage
   my_account_page : MainPage





