from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_producto_presente_en_carrito(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)

    assert cart.is_item_present("Sauce Labs Backpack") is True
