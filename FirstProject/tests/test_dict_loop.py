import mock
from ..dict_loop import data_printer

student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}

def test_data_printer():
    with mock.patch.object(__builtins__, 'input', lambda: "items"):
        assert data_printer(student_grades) == [('Marry', 9.1), ('Sim', 8.8), ('John', 7.5)]
    with mock.patch.object(__builtins__, 'input', lambda: "keys"):
        assert data_printer(student_grades) == ['Marry', 'Sim', 'John']
    with mock.patch.object(__builtins__, 'input', lambda: 'values'):
        assert data_printer(student_grades) == [9.1, 8.8, 7.5]