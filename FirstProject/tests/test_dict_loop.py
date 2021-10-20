from ..dict_loop import data_printer_value
from ..dict_loop import data_printer_item
from ..dict_loop import data_printer_key


student_grades = {'Marry': 9.1, 'Sim': 8.8, 'John': 7.5}
student_grades2 = ('Marry', 9.1, 'Sim', 8.8, 'John', 7.5)

def test_data_printer_item():
    assert data_printer_item(student_grades) == [('Marry', 9.1), ('Sim', 8.8), ('John', 7.5)]


def test_data_printer_key():
    assert data_printer_key(student_grades) == ['Marry', 'Sim', 'John']

def test_data_printer_value():
    assert data_printer_value(student_grades) == [9.1, 8.8, 7.5]

