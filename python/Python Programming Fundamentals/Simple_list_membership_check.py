# Write a pytest test function called test_contains_five that takes an argument called numbers to check if a given list contains the number 5.
my_list = [1,3,5,7,9]

import pytest
def test_contains_five(numbers):
    assert 5 in numbers, "The list does not contain the number 5"
    # test case to check if the list contains the number 5


# running

