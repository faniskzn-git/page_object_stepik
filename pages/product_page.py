from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_product_add_to_basket(self):
        self.should_be_see_add_to_basket_button()
        self.go_to_basket_page()
        self.solve_quiz_and_get_code()
        self.should_be_product_name_equal_basket_name()
        self.should_be_basket_amount_equal_product_price()

    def should_be_see_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"

    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "'Success message is still present, but should disappear"

    def should_be_product_name_equal_basket_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_message_product_name = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_NAME).text
        assert product_name == basket_message_product_name, "Product name does not match message in basket"

    def should_be_basket_amount_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.split(' ')[0]
        basket_message_product_price = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_PRICE).text.split(' ')[0]
        assert product_price == basket_message_product_price, "Product price does not match message in basket"