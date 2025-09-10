import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest
from verify_cinema_hall import verify_cinema_hall

def test_valid_hall():
    assert verify_cinema_hall('HallA1', 10, 20) is True

def test_invalid_hall_name():
    # Name with special character
    assert verify_cinema_hall('Hall@1', 10, 20) is False
    # Name with spaces is allowed
    assert verify_cinema_hall('Hall 1', 10, 20) is True

def test_invalid_hall_height():
    # Non-integer height
    assert verify_cinema_hall('HallA1', 'ten', 20) is False
    assert verify_cinema_hall('HallA1', 10.5, 20) is False
    # Negative height
    assert verify_cinema_hall('HallA1', -10, 20) is False

def test_invalid_hall_length():
    # Non-integer length
    assert verify_cinema_hall('HallA1', 10, 'twenty') is False
    assert verify_cinema_hall('HallA1', 10, 20.5) is False
    # Negative length
    assert verify_cinema_hall('HallA1', 10, -20) is False
