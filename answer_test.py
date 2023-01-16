
 
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
        print(f"Score:{(cls.__correct__ / cls.__total__) * 100}%")

    def test_sum(self):
        TestAnswer.__total__ += 1
        result = answer.sum(1,2)
        assert (result == 3)
        TestAnswer.__correct__ += 1
        
    def test_product(self):
        TestAnswer.__total__ += 1
        result = answer.product(2,3)
        assert (result == 6)
        TestAnswer.__correct__ += 1