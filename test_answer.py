import pytest
import answer

class TestAnswer():

    __correct__ = 0
    __total__ = 0

    @classmethod
    def setup_class(cls):
        print("Before")
        cls.__correct__ = 0
        cls.__total__ = 0

    @classmethod
    def teardown_class(cls):
        print(f"Score:{(cls.__correct__/cls.__total__)*100}%")

    def test_number_x(self):
        TestAnswer.__total__ += 1
        x,y = answer.number(5)
        assert(x==25)
        TestAnswer.__correct__ += 1
        
    def test_number_y(self):
        TestAnswer.__total__ += 1
        x = answer.number(5)
        assert(x==2)
        TestAnswer.__correct__ += 1
