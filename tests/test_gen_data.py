from pytest import mark

from src.controller.gen_date import gen_uuid, gen_date

uuid_values_params = {
    '84dc38a693b84cd6a4034f52b097af19'
}


@mark.parametrize('expected_value', uuid_values_params)
def test_gen_uuid(expected_value):
    assert len(gen_uuid()) == 32


date_value_params = {
    '2021-10-29'
}


@mark.parametrize('expected_value', date_value_params)
def test_gen_date(expected_value):
    assert type(gen_date()) is str
    assert gen_date() == expected_value
