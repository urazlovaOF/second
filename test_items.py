from selenium import webdriver
import pytest
import time
import conftest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_add_to_cart(browser):
    browser.get(link)

    button_len = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))

    assert button_len == 1, "Кнопка добаления в корзину не найдена"


