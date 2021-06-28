from todomvc_test.model import todos


def test_add():
    todos.visit()

    todos.add('a', 'b', 'c', 'd')

    todos.should_be('a', 'b', 'c', 'd')
    todos.items_left_should_be(4)


def test_edit_by_enter():
    todos.visit_with('a', 'b')

    todos.edit_by_enter('a', 'a edited')

    todos.should_be('a edited', 'b')
    todos.items_left_should_be(2)
