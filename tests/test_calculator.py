from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        a = 321
        b = 123

        result = Calculator().subtract(a,b)

        expected = 198
        assert result == expected

    def test_multiply(self):
        a = 100
        b = 5

        result = Calculator().multiply(a,b)

        expected = 500
        assert result == expected

    def test_divide(self):
        a = 963
        b = 9

        result = Calculator().divide(a,b)

        expected = 107
        assert result == expected
