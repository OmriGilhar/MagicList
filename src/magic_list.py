from typing import Any


class MagicList(list):
    """
    MagicList
    ------

    MagicList is an enhancement version of Python list
    =======================

    Enhancement summary:

    * MagicList don't contain any boundary check.

    ```
        >>> a = MagicList()
        >>> a[0] = 5
        >>> print(a)
        [5]
    ```

    Another good example:

    ```
        >>> a = MagicList()
        >>> a[5] = 5
        >>> print(a)
        [None, None, None, None, None, 5]
    ```

    References and Footnotes
    -------

        [1] https://docs.python.org/3/tutorial/datastructures.html

    """
    def __setitem__(self, index: int, value: Any) -> None:
        """ Called to implement assignment to self[key].

        Assign an value to a specific index, if the index does not exists,
        appends Nones till the value location then insert the value in the
        proper location, otherwise, override the existing value.

        :param index: The value location within the MagicList.
        :param value: The value we want to insert.
        :raises IndexError: When index is less than 0.
        """
        if index < 0:
            raise IndexError('Index most be positive.')
        if len(self)-1 < index:
            while len(self) < index:
                self.append(None)
            self.append(value)
        else:
            super(MagicList, self).__setitem__(index, value)
