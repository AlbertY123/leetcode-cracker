import logging

from fav_plots.utils import add_one


def test_add_one():
    logging.info("Testing the add_one function")
    x = 10
    expected_result = x + 1
    function_result = add_one(x)
    assert expected_result == function_result 