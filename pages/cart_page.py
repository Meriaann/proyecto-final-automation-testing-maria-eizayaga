from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):

    CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_item_present(self, item_name):
        items = self.driver.find_elements(*self.CART_ITEM_NAME)
        return any(item.text == item_name for item in items)


    def go_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        self.click_element(self.CHECKOUT_BUTTON)

        self.wait.until(EC.url_contains("checkout-step-one.html"))

        from pages.checkout_step_one_page import CheckoutStepOnePage
        return CheckoutStepOnePage(self.driver)
