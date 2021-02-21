from tests.pages.filter_all_oop import TodoMvcPage


def test_add():
    TodoMvcPage().visit().add('a', 'b', 'c', 'd').items_count_should_be(4)

def test_edit():
    TodoMvcPage().visit().add('a').items_count_should_be(1)
