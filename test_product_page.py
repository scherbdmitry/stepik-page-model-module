from pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('code_promo', ["0", "1","2","3","4","5","6",
					pytest.param("7", marks=pytest.mark.xfail),
					"8","9"])

def test_guest_can_add_product_to_basket(browser, code_promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{code_promo}"
    #http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear
    print(link)
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.add_basket()
    page_product.solve_quiz_and_get_code()
    page_product.should_be_added_basket()
    page_product.should_be_name_added_product()    
    page_product.should_be_cost_added_product()
    
    #time.sleep(5)
    
