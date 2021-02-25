from todomvc_test.model import todos


def test_tasks_lifecycle():
    todos.visit()

    todos.add('a', 'b', 'c', 'd')
    todos.items_should_be('a', 'b', 'c', 'd')

    todos.edit('b', 'b edited')
    todos.complete('b edited')
    todos.clear_completed()
    todos.items_should_be('a', 'c', 'd')

    todos.cancel_editing('c', 'c edited')
    todos.delete('c')
    todos.items_should_be('a', 'd')
