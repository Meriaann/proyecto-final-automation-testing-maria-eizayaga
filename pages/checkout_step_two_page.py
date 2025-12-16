from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

# class CheckoutStepTwoPage(BasePage):

#     FINISH_BTN = (By.ID, "finish")
#     COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

#     def wait_for_page(self):
#         self.wait.until(EC.url_contains("checkout-step-two.html"))
#         self.wait.until(EC.visibility_of_element_located(self.FINISH_BTN))

#     def finish_checkout(self):
#         self.wait_for_page()
#         self.click_element(self.FINISH_BTN)

#     def is_checkout_complete(self):
#         return self.find_element(self.COMPLETE_HEADER).is_displayed()

class CheckoutStepTwoPage(BasePage):

    FINISH_BTN = (By.ID, "finish")

    def wait_for_page(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        self.wait.until(EC.visibility_of_element_located(self.FINISH_BTN))

    def finish_checkout(self):
        self.wait_for_page()
        self.click_element(self.FINISH_BTN)
