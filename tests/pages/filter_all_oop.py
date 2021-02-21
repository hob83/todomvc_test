from selene import have
from selene.support.shared import browser
from selene import command


class TodoMvcPage:
    def collection(self):
        return browser.all('#todo-list>li')

    def visit(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        window_uploaded = "return $._data($('#clear-completed')[0], 'events')" \
                      ".hasOwnProperty('click') & " \
                      "Object.keys(require.s.contexts._.defined).length == 39"
        browser.should(have.js_returned(True, window_uploaded))
        return self

    def add(self, *texts: str):
        for text in texts:
            browser.element('#new-todo').type(text).press_enter()
        return self

    def items_count_should_be(self, value: int):
        browser.element('#todo-count>strong').\
            should(have.exact_text(str(value)))

    def editing_start(self, text: str, new_text: str):
        self.collection().element_by(have.exact_text(text)).double_click()
        return self.collection().element_by(have.css_class('editing')) \
            .element('.edit').perform(command.js.set_value(new_text))
