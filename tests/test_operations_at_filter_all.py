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


def test_edit_by_tab():
    todos.visit_with('a', 'b')

    todos.edit_by_tab('a', 'a edited')

    todos.should_be('a edited', 'b')
    todos.items_left_should_be(2)


def test_cancel_editing():
    todos.visit_with('a', 'b')

    todos.cancel_editing('a', 'a edited')

    todos.should_be('a', 'b')
    todos.items_left_should_be(2)


def test_delete_by_edit_to_blank():
    todos.visit_with('a', 'b')

    todos.edit_by_enter('a', '')

    todos.should_be('b')
    todos.items_left_should_be(1)


def test_complete():
    todos.visit_with('a', 'b')

    todos.toggle('b')

    todos.should_be_active('a')
    todos.should_be_completed('b')
    todos.items_left_should_be(1)


def test_complete_all_with_some_completed():
    todos.visit_with('a', 'b', 'c')
    todos.toggle('a')

    todos.toggle_all()

    todos.should_be_active()
    todos.should_be_completed('a', 'b', 'c')
    todos.items_left_should_be(0)


def test_clear_completed():
    todos.visit_with('a', 'b')
    todos.toggle('b')

    todos.clear_completed()

    todos.should_be('a')
    todos.items_left_should_be(1)
    todos.should_be_clear_completed_hidden()


def test_delete():
    todos.visit_with('a', 'b')

    todos.delete('b')

    todos.should_be('a')
    todos.items_left_should_be(1)
    todos.should_be_clear_completed_hidden()


def test_activate():
    todos.visit_with('a', 'b')
    todos.toggle('b')

    todos.toggle('b')

    todos.should_be_completed()
    todos.should_be_active('a', 'b')
    todos.items_left_should_be(2)
    todos.should_be_clear_completed_hidden()


def test_activate_all():
    todos.visit_with('a', 'b', 'c')
    todos.toggle_all()

    todos.toggle_all()

    todos.should_be_completed()
    todos.should_be_active('a', 'b', 'c')
    todos.items_left_should_be(3)
