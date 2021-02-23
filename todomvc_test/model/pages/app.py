from selene import have, command
from selene.support.shared import browser

todo_list = browser.all('#todo-list>li')


def visit():
    browser.config.hold_browser_open = True
    browser.open('https://todomvc4tasj.herokuapp.com/')
    window_uploaded = "return $._data($('#clear-completed')[0], 'events')" \
                      ".hasOwnProperty('click') & " \
                      "Object.keys(require.s.contexts._.defined).length == 39"
    browser.should(have.js_returned(True, window_uploaded))


def add(*texts):
    for text in texts:
        browser.element('#new-todo').type(text).press_enter()


def should_be(*texts):
    todo_list.should(have.exact_texts(*texts))


def start_editing(text, new_text):
    todo_list.element_by(have.exact_text(text)).double_click()
    return todo_list.element_by(have.css_class('editing')).element('.edit').\
        perform(command.js.set_value(new_text))


def edit(text, new_text):
    start_editing(text, new_text).press_enter()


def toggle(text):
    todo_list.element_by(have.exact_text(text)).\
        element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def cancel_editing(text, new_text):
    start_editing(text, new_text).press_escape()


def delete(text):
    todo_list.element_by(have.exact_text(text)).hover().\
        element('.destroy').click()
