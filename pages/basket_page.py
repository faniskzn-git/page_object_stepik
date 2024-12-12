from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page_is_empty(self):
        self.should_be_basket_url()
        self.should_be_not_presents_items_in_basket()
        self.should_be_presents_message_in_basket()
        self.should_be_message_basket_page_is_empty()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, "URL is not available"

    def should_be_not_presents_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
        "Items in basket presented, but should not be"

    def should_be_presents_message_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE),\
        "Message in basket not presented, but should be"

    def should_be_message_basket_page_is_empty(self):
        basket_is_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text.split('.')[0]
        assert basket_is_empty_message == "Your basket is empty", "Basket is empty message don't show"