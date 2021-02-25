from todomvc_test.model import todos


def test_add():
    todos.visit()

    todos.add('a', 'b', 'c', 'd')

    todos.items_should_be('a', 'b', 'c', 'd')
    todos.items_count_should_be(4)


def test_edit():
    todos.visit_with('a')

    todos.edit('a', 'a edited')

    todos.items_should_be('a edited')
    todos.items_count_should_be(1)


def test_cancel_editing():
    todos.visit_with('a')

    todos.cancel_editing('a', 'a edited')

    todos.items_should_be('a')
    todos.items_count_should_be(1)


def test_complete():
    todos.visit_with('a', 'b', 'c')

    todos.complete('b', 'c')

    todos.items_should_be_active('a')
    todos.items_should_be_completed('b', 'c')
    todos.items_count_should_be(1)


def test_complete_all():
    todos.visit_with('a', 'b', 'c')

    todos.complete_all()

    todos.items_should_be_completed('a', 'b', 'c')
    todos.items_count_should_be(0)


def test_clear_completed():
    todos.visit_with('a', 'b', 'c').complete('b', 'c')

    todos.clear_completed()

    todos.items_should_be('a')
    todos.items_count_should_be(1)


def test_delete():
    todos.visit_with('a', 'b', 'c')

    todos.delete('b', 'c')

    todos.items_should_be('a')
    todos.items_count_should_be(1)


def test_activate():
    todos.visit_with('a', 'b', 'c', 'd').complete('b', 'c', 'd')

    todos.activate('b', 'c')

    todos.items_should_be_completed('d')
    todos.items_should_be_active('a', 'b', 'c')
    todos.items_count_should_be(3)


def test_activate_all():
    todos.visit_with('a', 'b', 'c')
    todos.complete('a')

    todos.complete_all().complete_all()

    todos.items_should_be_active('a', 'b', 'c')
    todos.items_count_should_be(3)
