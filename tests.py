import unittest
from main import generate_pagination


class TestPagination(unittest.TestCase):
    def setUp(self):
        self.pagination = generate_pagination

    def test_pagination_is_correct(self):
        expected = "1 ... 4 5"
        result = self.pagination(4, 5, 1, 0)
        self.assertEqual(result, expected)

    def test_pagination_is_correct_on_big_numbers(self):
        expected = (
            "1 2 3 4 5 6 7 8 9 10 ... "
            "97 98 99 100 101 102 103 ... "
            "491 492 493 494 495 496 497 498 499 500"
        )
        result = self.pagination(100, 500, 10, 3)
        self.assertEqual(result, expected)

    def test_pagination_current_page_zero(self):
        with self.assertRaises(ValueError):
            self.pagination(0, 10, 1, 1)

    def test_pagination_total_pages_zero(self):
        with self.assertRaises(ValueError):
            self.pagination(4, 0, 1, 1)

    def test_pagination_boundaries_negative(self):
        with self.assertRaises(ValueError):
            self.pagination(4, 10, -1, 1)

    def test_pagination_around_negative(self):
        with self.assertRaises(ValueError):
            self.pagination(4, 10, 1, -1)


if __name__ == "__main__":
    unittest.main()
