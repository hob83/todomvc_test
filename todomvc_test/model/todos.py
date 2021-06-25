from selene import have
from selene.support.shared import browser

have_completed = have.css_class('completed')


class TextTodo:
    def __init__(self, text_todo: str, status: str = 'new'):
        self.text_todo = text_todo
        if status == 'new':
            self.status = 'false'
        else:
            self.status = 'true'


class TodoMvcPage:
    def __init__(self):
        self.collection = browser.all('#todo-list>li')

    def visit(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        js_loaded = \
            '''return $._data($('#clear-completed')[0], 'events')
            .hasOwnProperty('click') & 
            Object.keys(require.s.contexts._.defined).length == 39'''
        browser.should(have.js_returned(True, js_loaded))
        return self

    #def visit_with(self, *texts):
    #    self.visit().add(*texts)
    #    return self

    def visit_with(self, *texts):
        self.visit()
        script = ''
        if isinstance(texts[0], TextTodo):
            for text in texts:
                script += f'''{{\\\"completed\\\":{text.status},\\\"title\\\":\\\"{text.text_todo}\\\"}},'''
            browser.execute_script(
                f'''localStorage['todos-troopjs'] = "[{script.rstrip(',')}]"''')
            browser.driver.refresh()
        else:
            for text in texts:
                stat = 'false'
                tex = text
                script += f'''{{\\\"completed\\\":{stat},\\\"title\\\":\\\"{tex}\\\"}},'''
            browser.execute_script(
                f'''localStorage['todos-troopjs'] = "[{script.rstrip(',')}]"''')
            browser.driver.refresh()

    def add(self, *texts):
        for text in texts:
            browser.element('#new-todo').type(text).press_enter()
        return self

    def items_left_should_be(self, value: int):
        browser.element('#todo-count>strong'). \
            should(have.exact_text(str(value)))
        return self

    def start_editing(self, text: str, new_text: str):
        self.collection.element_by(have.exact_text(text)).double_click()
        return self.collection.element_by(have.css_class('editing')) \
            .element('.edit').with_(set_value_by_js=True).set_value(new_text)

    def edit_by_enter(self, text: str, new_text: str):
        self.start_editing(text, new_text).press_enter()

    def edit_by_tab(self, text: str, new_text: str):
        self.start_editing(text, new_text).press_tab()

    def cancel_editing(self, text: str, new_text: str):
        self.start_editing(text, new_text).press_escape()

    def should_be(self, *texts: str):
        self.collection.should(have.exact_texts(*texts))

    def toggle(self, text: str):
        self.collection.element_by(have.exact_text(text))\
            .element('.toggle').click()

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def should_be_active(self, *texts: str):
        self.collection.filtered_by(have_completed.not_)\
            .should(have.exact_texts(*texts))
        return self

    def should_be_completed(self, *texts: str):
        self.collection.filtered_by(have_completed)\
            .should(have.exact_texts(*texts))
        return self

    def should_be_clear_completed_hidden(self):
        browser.element('#clear-completed')\
            .should(have.attribute('style', 'display: none;'))
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def delete(self, text: str):
        self.collection.element_by(have.exact_text(text)).hover()\
            .element('.destroy').click()
