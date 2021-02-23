from tests.pages.filter_all_oop import TodoMvcPage


def test_add():
    TodoMvcPage().visit().add('a', 'b', 'c', 'd')

    TodoMvcPage().items_count_should_be(4)


def test_edit():
    TodoMvcPage().visit().add('a').edit('a', 'a edited')

    TodoMvcPage().items_should_be('a edited')


def test_cancel_editing():
    TodoMvcPage().visit().add('a').cancel_editing('a', 'a edited')

    TodoMvcPage().items_should_be('a')


def test_complete():
    TodoMvcPage().visit().add('a', 'b', 'c').complete('b', 'c')

    TodoMvcPage().items_should_be_active('a')
    TodoMvcPage().items_should_be_completed('b', 'c')


def test_complete_all():
    TodoMvcPage().visit().add('a', 'b', 'c').complete_all()

    TodoMvcPage().items_should_be_completed('a', 'b', 'c')


def test_clear_completed():
    TodoMvcPage().visit().add('a', 'b', 'c').complete('b', 'c')
    TodoMvcPage().clear_completed()

    TodoMvcPage().items_should_be('a')


def test_delete():
    TodoMvcPage().visit().add('a', 'b', 'c').delete('b', 'c')

    TodoMvcPage().items_should_be('a')


def test_activate():
    TodoMvcPage().visit().add('a', 'b', 'c', 'd').complete('b', 'c', 'd')
    TodoMvcPage().activate('b', 'c')

    TodoMvcPage().items_should_be_completed('d')
    TodoMvcPage().items_should_be_active('a', 'b', 'c')


def test_activate_all():
    TodoMvcPage().visit().add('a', 'b', 'c')
    TodoMvcPage().complete('a')
    TodoMvcPage().complete_all().complete_all()

    TodoMvcPage().items_should_be_active('a', 'b', 'c')
