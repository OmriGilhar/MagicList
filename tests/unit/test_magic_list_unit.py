from unittest import main, TestCase
from src.magic_list import MagicList


class TestMagicListUnit(TestCase):
    def setUp(self) -> None:
        """
        Set up a fresh MagicList instance for the following tests.
        """
        self.list = MagicList()

    def test_setitem_normal_behavior(self) -> None:
        """
        Test the normal behavior of the MagicList, test the assignment of a
        new value into a specific location within the MagicList.
        """
        for i in range(5):
            with self.subTest(f"Subtest Number: {i}", i=i):
                self.list[i] = i**2
                self.assertEqual(self.list[i], i**2)

    def test_setitem_fill(self) -> None:
        """
        Test if the MagicList inset Nones before the proper location.
        """
        self.list[5] = 5
        filter(lambda x: x is None, self.list[0:-1])

    def test_setitem_exception(self) -> None:
        """
        False Positive test, test if MagicList raises the proper Exception
        when called with index less then 0.
        """
        with self.assertRaises(IndexError) as context:
            self.list[-1] = 5
        self.assertTrue('Index most be positive.' in str(context.exception))

    def tearDown(self) -> None:
        """
        Post test, Clean the list.
        """
        self.list.clear()


if __name__ == '__main__':
    main()
