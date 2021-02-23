from todomvc_test.model.pages import app


def test_test_tasks_lifecycle():
    app.visit()

    app.add('a', 'b', 'c', 'd')
    app.should_be('a', 'b', 'c', 'd')

    app.edit('b', 'b edited')
    app.toggle('b edited')
    app.clear_completed()
    app.should_be('a', 'c', 'd')

    app.cancel_editing('c', 'c edited')
    app.delete('c')
    app.should_be('a', 'd')
