from selene import have
from selene.support.shared import browser
import time


def test_common_management():

    browser.config.hold_browser_open = True
    browser.open('https://todomvc4tasj.herokuapp.com/')
    window_uploaded = "return $._data($('#clear-completed')[0], 'events').hasOwnProperty('click')"
    browser.should(have.js_returned(True, window_uploaded))

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.element('#new-todo').type('d').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c', 'd'))

    browser.all('#todo-list>li').element_by(have.exact_text('b')).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing')).element('.edit').type(' edited').press_enter()
    browser.all('#todo-list>li').element_by(have.exact_text('a')).element('.toggle').click()
    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_texts('b edited', 'c', 'd'))

    browser.all('#todo-list>li').element_by(have.exact_text('c')).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing')).element('.edit').type(' edited').press_escape()
    browser.all('#todo-list>li').element_by(have.exact_text('c')).hover().element('.destroy').click()
    browser.all('#todo-list>li').should(have.exact_texts('b edited', 'd'))
