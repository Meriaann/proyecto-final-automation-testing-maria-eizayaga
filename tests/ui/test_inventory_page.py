from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_agregar_producto_desde_inventory(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    assert inventory.is_on_inventory_page() is True

    inventory.add_backpack_to_cart()

    assert inventory.get_cart_count() == "1"
