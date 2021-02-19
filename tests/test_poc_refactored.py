from todomvc_test.helpers import app


def test_common_management():
    app.open_page()

    app.add('a', 'b', 'c', 'd')
    app.assert_todos('a', 'b', 'c', 'd')

    app.edit('b', 'b edited')
    app.complete('b edited')
    app.clear_completed()
    app.assert_todos('a', 'c', 'd')

    app.cancel_editing('c', 'c edited')
    app.delete('c')
    app.assert_todos('a', 'd')
