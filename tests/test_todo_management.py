from todomvc_test.model import todos


def test_todos_lifecycle():
    todos.visit()

    todos.add('a', 'b', 'c', 'd')
    todos.should_be('a', 'b', 'c', 'd')

    todos.edit_by_enter('b', 'b edited')

    todos.toggle('b edited')
    todos.clear_completed()
    todos.should_be('a', 'c', 'd')

    todos.cancel_editing('c', 'c edited')

    todos.delete('c')
    todos.should_be('a', 'd')
