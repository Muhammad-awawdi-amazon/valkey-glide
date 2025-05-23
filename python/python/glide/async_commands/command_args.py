# Copyright Valkey GLIDE Project Contributors - SPDX Identifier: Apache-2.0

from enum import Enum


class Limit:
    """
    Represents a limit argument for range queries in various commands.

    The `LIMIT` argument is commonly used to specify a subset of results from the matching elements,
    similar to the `LIMIT` clause in SQL (e.g., `SELECT LIMIT offset, count`).

    This class can be utilized in multiple commands that support limit options,
    such as [ZRANGE](https://valkey.io/commands/zrange), [SORT](https://valkey.io/commands/sort/) and others.

    Args:
        offset (int): The starting position of the range, zero based.
        count (int): The maximum number of elements to include in the range.
            A negative count returns all elements from the offset.

    Examples:
        >>> limit = Limit(0, 10)  # Fetch the first 10 elements
        >>> limit = Limit(5, -1)  # Fetch all elements starting from the 5th element
    """

    def __init__(self, offset: int, count: int):
        self.offset = offset
        self.count = count


class OrderBy(Enum):
    """
    Enumeration representing sorting order options.

    This enum is used for the following commands:

        - `SORT`: General sorting in ascending or descending order.
        - `GEOSEARCH`: Sorting items based on their proximity to a center point.
        - `FT.AGGREGATE`: Used in the SortBy clause of the FT.AGGREGATE command.

    """

    ASC = "ASC"
    """
    ASC: Sort in ascending order.
    """

    DESC = "DESC"
    """
    DESC: Sort in descending order.
    """


class ListDirection(Enum):
    """
    Enumeration representing element popping or adding direction for List commands.
    """

    LEFT = "LEFT"
    """
    LEFT: Represents the option that elements should be popped from or added to the left side of a list.
    """

    RIGHT = "RIGHT"
    """
    RIGHT: Represents the option that elements should be popped from or added to the right side of a list.
    """


class ObjectType(Enum):
    """
    Enumeration representing the data types supported by the database.
    """

    STRING = "String"
    """
    Represents a string data type.
    """

    LIST = "List"
    """
    Represents a list data type.
    """

    SET = "Set"
    """
    Represents a set data type.
    """

    ZSET = "ZSet"
    """
    Represents a sorted set data type.
    """

    HASH = "Hash"
    """
    Represents a hash data type.
    """

    STREAM = "Stream"
    """
    Represents a stream data type.
    """
