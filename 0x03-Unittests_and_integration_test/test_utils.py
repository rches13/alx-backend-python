#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function in the utils module.
"""

import unittest
from typing import Any, Dict, Tuple
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function which retrieves values
    from a nested dictionary based on a path of keys.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict[str, Any],
        path: Tuple[str, ...],
        expected: Any
    ) -> None:
        """
        Test that access_nested_map returns the correct value
        for a given path of keys in the nested dictionary.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
