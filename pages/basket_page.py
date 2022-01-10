from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage (BasePage):

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEM), "Basket is not empty"
        
    def should_be_text_about_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_EMPTY_TEXT), "No message about empty basket"

        
      
      

        
