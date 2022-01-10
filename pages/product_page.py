from .base_page import BasePage
from .locators import ProductPageLocators
#from .locators import LoginPageLocators #m
from selenium.webdriver.common.by import By
import time

class ProductPage (BasePage):

    def add_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Add to basket button is not presented"        
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_link.click()
        

    def should_be_added_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDED_BASKET), "MESSAGE_ADDED_BASKET is not found"
        added_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_BASKET)
        added_basket_message = added_basket.text
        assert "has been added to your basket" in added_basket_message, "Product has not been added in your basket"
        print(f'Message about basket - {added_basket_message}')
    

    def should_be_name_added_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_NAME_PRODUCT_IN_BASKET), "MESSAGE_NAME_PRODUCT_IN_BASKET is not found"
        name_product_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_PRODUCT_IN_BASKET).text
        name_product_on_product_page = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ON_PRODUCT_PAGE).text
        print(f'Product name in basket - {name_product_in_basket}', f'Product name on product page - {name_product_on_product_page}', sep='\n')
        assert name_product_in_basket == name_product_on_product_page, "Product name is not equal"


    def should_be_cost_added_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_COST_BASKET), "MESSAGE_COST_BASKET is not found"
        message_cost_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_COST_BASKET).text
        cost_product_in_basket = self.browser.find_element(*ProductPageLocators.COST_PRODUCT_IN_BASKET).text
        cost_product_on_product_page = self.browser.find_element(*ProductPageLocators.COST_PRODUCT_ON_PRODUCT_PAGE).text
        print(f'Message about cost basket - {message_cost_basket}', f'Product price in basket - {cost_product_in_basket}', f'Product price on product page - {cost_product_on_product_page}', sep='\n')
        assert cost_product_in_basket == cost_product_on_product_page, "cost is not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDED_BASKET), \
           "Success message add to basket is presented, but should not be"


    def should_be_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDED_BASKET), \
           "Success message add to basket is not presented, but should be"
