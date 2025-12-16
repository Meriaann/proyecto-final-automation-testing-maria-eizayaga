import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
#from utils.data_manager import read_csv_data
from pages.login_page import LoginPage

def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    assert login.is_on_products_page() is True


def test_login_fallido(driver):
    login = LoginPage(driver)
    login.login("standard_user", "wrong_password")

    assert login.get_error_message() is not None





