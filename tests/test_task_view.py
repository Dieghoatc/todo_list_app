from pytest import mark

from src.view.task_view import print_all_task

all_task_values_params = {
}


@mark.parametrize('value, expected_value', all_task_values_params)
def test_print_all_task(value, expected_value):
    assert print_all_task(value) == expected_value
