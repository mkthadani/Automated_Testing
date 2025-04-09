import unittest
from library_system import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("Python Programming", 3)

    def test_initial_copies(self):
        self.assertEqual(self.library.get_copies("Python Programming"), 3)

    def test_add_book(self):
        self.library.add_book("Data Structures", 2)
        self.assertEqual(self.library.get_copies("Data Structures"), 2)

    def test_borrow_book(self):
        self.library.borrow_book("Python Programming")
        self.assertEqual(self.library.get_copies("Python Programming"), 2)

    def test_return_book(self):
        self.library.borrow_book("Python Programming")
        self.library.return_book("Python Programming")
        self.assertEqual(self.library.get_copies("Python Programming"), 3)

    def test_borrow_unavailable_book(self):
        self.library.borrow_book("Python Programming")
        self.library.borrow_book("Python Programming")
        self.library.borrow_book("Python Programming")
        with self.assertRaises(ValueError):
            self.library.borrow_book("Python Programming")

    def test_add_book_invalid_copies(self):
        with self.assertRaises(ValueError):
            self.library.add_book("Algorithms", 0)
    
    def test_borrow_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book("Nonexistent Book")

    def test_return_new_book(self):
        self.library.return_book("New Book")
        self.assertEqual(self.library.get_copies("New Book"), 1)

    def test_multiple_transactions(self):
        self.library.add_book("Machine Learning", 2)
        self.library.borrow_book("Machine Learning")
        self.library.borrow_book("Machine Learning")
        self.library.borrow_book("Machine Learning")
        self.library.return_book("Machine Learning")
        self.assertEqual(self.library.get_copies("Machine Learning"), 1)

if __name__ == '__main__':
    unittest.main()
