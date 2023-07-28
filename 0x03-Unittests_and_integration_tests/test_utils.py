#!/usr/bin/env python3
"""
Test Module for tasks in 0x03-Unittests_and_integration_tests
"""

import unittest
from fixtures import GITHUB_API_DATA
from unittest.mock import patch, MagicMock
from parameterized import parameterized, parameterized_class
from typing import Any
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap Class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test access_nested_map function for exception
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson Class
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize Class
    """

    class TestClass:
        """
        TestClass for memoization
        """

        def a_method(self):
            """
            Test method
            """
            return 42

        @memoize
        def a_property(self):
            """
            Test property
            """
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        Test memoize decorator
        """
        instance = self.TestClass()
        instance.a_property()
        instance.a_property()
        mock_a_method.assert_called_once()


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
    for org_payload, repos_payload, expected_repos, apache2_repos in
    fixtures.GITHUB_API_DATA.values()
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    TestIntegrationGithubOrgClient Class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method
        """
        client = GithubOrgClient("test")
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload
        ]
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with license parameter
        """
        client = GithubOrgClient("test")
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload
        ]
        repos = client.public_repos("apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
