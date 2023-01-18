
 
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

    def test_print(self):
        TestAnswer.__total__ += 1
        result = answer.print()
        assert (result.lower() == "i am really excited to learn python")
        TestAnswer.__correct__ += 1
        