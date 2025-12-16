from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def is_on_inventory_page(self):
        return self.find_element(self.TITLE).text == "Products"

    def add_backpack_to_cart(self):
        self.click_element(self.ADD_TO_CART_BACKPACK)

    def get_cart_count(self):
        return self.find_element(self.CART_BADGE).text

    def go_to_cart(self):
        self.click_element(self.CART_ICON)
