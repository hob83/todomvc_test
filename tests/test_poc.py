from selene import have
from selene.support.shared import browser
import time


def test_poc():

    browser.config.hold_browser_open = True
    browser.open('https://todomvc4tasj.herokuapp.com/')
    time.sleep(2)

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.element('#new-todo').type('d').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c', 'd'))

    browser.all('#todo-list>li').element_by(have.exact_text('b')).double_click()
    browser.element('.editing>.edit').type(' edited').press_enter()
    browser.all('#todo-list>li').element_by(have.exact_text('a')).element('.toggle').click()
    browser.all('#todo-list>li').element_by(have.exact_text('b edited')).element('.toggle').click()
    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_texts('c', 'd'))

    browser.all('#todo-list>li').element_by(have.exact_text('c')).double_click()
    browser.element('.editing>.edit').type('to be canceled').press_escape()
    browser.all('#todo-list>li').element_by(have.exact_text('c')).element('.destroy').click()
    browser.all('#todo-list>li').should(have.exact_texts('d'))
