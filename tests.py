import unittest
from main import PaginationGenerator


class TestPagination(unittest.TestCase):
    def setUp(self):
        self.generator = PaginationGenerator()
        self.pagination = self.generator.generate_pagination

    def test_pagination_is_correct(self):

        expected = "1 2 3 4 ... 30 31 32 33 34 35 36 ... 62 63 64 65"
        result = self.pagination(33, 65, 4, 3)
        self.assertEqual(result, expected)
    
    def test_pagination_around_gte_total_pages(self):
        
        expected = "1 2 3 4 5 6 7 8 9 10"
        result = self.pagination(5, 10, 1, 10)
        self.assertEqual(result, expected)

        expected = "1 2 3 4 5 6 7 8 9 10"
        result = self.pagination(5, 10, 1, 11)
        self.assertEqual(result, expected)

    def test_pagination_all_values_the_same(self):

        expected = "1 2 3 4 5 6 7 8 9 10"
        result = self.pagination(10, 10, 10, 10)
        self.assertEqual(result, expected)
    
    def test_pagination_boundary_eq_around(self):
        
        expected = "1 2 3 4 5 6 ... 9 10"
        result = self.pagination(4, 10, 2, 2)
        self.assertEqual(result, expected)
    
    def test_pagination_zero_boundaries(self):

        expected = "... 4 5 6 ..."
        result = self.pagination(5, 10, 0, 1)
        self.assertEqual(result, expected)
        
        expected = "... 8 9 10"
        result = self.pagination(9, 10, 0, 1)
        self.assertEqual(result, expected)

        expected = "1 2 3 4 5 ..."
        result = self.pagination(3, 10, 0, 2)
        self.assertEqual(result, expected)

    def test_pagination_zero_around(self):
        
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
    
    def test_pagination_current_page_not_int(self):
        with self.assertRaises(TypeError):
            self.pagination("0", 10, 1, 1)

    def test_pagination_total_pages_not_int(self):
        with self.assertRaises(TypeError):
            self.pagination(4, (0, ), 1, 1)

    def test_pagination_boundaries_not_int(self):
        with self.assertRaises(TypeError):
            self.pagination(4, 10, {1: " "}, 1)

    def test_pagination_around_not_int(self):
        with self.assertRaises(TypeError):
            self.pagination(4, 10, 1, [2, 3])


if __name__ == "__main__":
    unittest.main()
