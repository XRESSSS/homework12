import pytest

from homework12 import sanitize_string
from homework12 import humanize_car_info


def test_sanitize_string():
    base_string = 'nnmmmnmnnmnnm5'
    exclude = 'nnmmjhfhgf'
    max_len = 5
    expected_result = ['5']
    actual_result = sanitize_string(
        string_value=base_string,
        max_result_length=max_len,
        exclude=exclude
    )
    assert actual_result == expected_result


def test_sanitize_zero_string():
    base_string = ''
    exclude = 'nnmmjhfhgf'
    max_len = 5
    expected_result = []
    actual_result = sanitize_string(
        string_value=base_string,
        max_result_length=max_len,
        exclude=exclude
    )
    assert actual_result == expected_result


def test_sanitize_unsuccess_string():
    base_string = '1' * 500
    exclude = 'nnmmjhfhgf'
    max_len = 0

    with pytest.raises(ValueError):
        sanitize_string(
            string_value=base_string,
            max_result_length=max_len,
            exclude=exclude
        )

def test_sanitize_overload_string():
    base_string = '1' * 500
    print(base_string)
    exclude = 'nnmmjhfhgf'
    max_len = 5
    expected_result = ['1'] * 5
    actual_result = sanitize_string(
        string_value=base_string,
        max_result_length=max_len,
        exclude=exclude
    )
    assert actual_result == expected_result


def test_valid_input():
    result = humanize_car_info(seconds=10, speed_meters_per_seconds=20, car_weight=500)
    expected = "Транспортний засіб вагою 500 кг рухався 10 секунд зі швидкістю 20," \
               " і подолав відстань 200 метрів"
    assert result == expected

def test_seconds_less_than_zero():
    with pytest.raises(ValueError) as excinfo:
        humanize_car_info(seconds=-5, speed_meters_per_seconds=20, car_weight=500)
    assert str(excinfo.value) == 'seconds value cannot be less than 0'

def test_speed_less_than_zero():
    with pytest.raises(ValueError) as excinfo:
        humanize_car_info(seconds=10, speed_meters_per_seconds=-5, car_weight=500)
    assert str(excinfo.value) == 'speed_meters_per_seconds value cannot be less than 0'

def test_weight_less_than_zero():
    with pytest.raises(ValueError) as excinfo:
        humanize_car_info(seconds=10, speed_meters_per_seconds=20, car_weight=-100)
    assert str(excinfo.value) == 'car_weight value cannot be less than 0'
