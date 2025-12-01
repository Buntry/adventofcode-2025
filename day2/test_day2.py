import pytest
from day2 import add

class TestDay2:
    def test_add(self):
        assert add(3, 5) == 8