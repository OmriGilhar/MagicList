from unittest import main, TestCase
from src.magic_list import MagicList
from collections import namedtuple
import uuid

Person = namedtuple('Person', 'name,id')


class TestMagicListIntegrated(TestCase):
    def setUp(self) -> None:
        """
        Set up a fresh MagicList instance for the following tests.
        """
        self.list = MagicList()

    def test_magic_list_use_case_no1(self) -> None:
        """
        Test a basic use case of the MagicList.
        """
        self.list[4] = 'and this is '
        self.list[1] = 'is '
        self.list[0] = 'This '
        self.list[3] = '<-- None? '
        self.list[4] = Person(name='User', id=str(uuid.uuid4())).name

        self.assertListEqual(
            self.list,
            [
                'This ', 'is ', None, '<-- None? ', 'User'
            ]
        )

    def tearDown(self) -> None:
        """
        Post test, Clean the list.
        """
        self.list.clear()


if __name__ == '__main__':
    main()
