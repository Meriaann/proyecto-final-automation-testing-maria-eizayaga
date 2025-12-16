from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.checkout_step_two_page import CheckoutStepTwoPage

class CheckoutStepOnePage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def fill_information_and_continue(self, name, last_name, zip_code):
        self.input_text(self.FIRST_NAME, name)
        self.input_text(self.LAST_NAME, last_name)
        self.input_text(self.POSTAL_CODE, zip_code)

        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
        self.click_element(self.CONTINUE_BTN)

        return CheckoutStepTwoPage(self.driver)


