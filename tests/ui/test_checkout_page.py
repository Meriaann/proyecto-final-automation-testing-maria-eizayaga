from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage

def test_checkout_completo(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    step_one = CartPage(driver).go_to_checkout()

    step_two = step_one.fill_information_and_continue(
        "Juan", "Perez", "12345"
    )

    step_two.finish_checkout()




