#!/usr/bin/env python3
""" Test cases for utils module """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestAccessNestedMap(unittest.TestCase):
    # Task 0
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map function """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    # Task 1
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test access_nested_map function with exceptions """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    # Task 2
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json function """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    # Task 3
    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """ Test memoize decorator """
        with patch.object(
            self.TestClass, 'a_method', return_value=42
        ) as mock_method:
            instance = self.TestClass()
            result = instance.a_property
            result2 = instance.a_property
            self.assertEqual(result, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


@parameterized_class([
    {
        "org_payload": payload["org_payload"],
        "repos_payload": payload["repos_payload"],
        "expected_repos": payload["expected_repos"],
        "apache2_repos": payload["apache2_repos"]
    }
    for payload in [
        {
            "org_payload": {"repos_url": "http://example.com/repos"},
            "repos_payload": {"name": "test_repo"},
            "expected_repos": ["test_repo"],
            "apache2_repos": []
        }
    ]
])
class TestGithubOrgClient(unittest.TestCase):
    # Task 4
    @patch('client.get_json')
    def test_org(self, mock_get):
        """ Test org method of GithubOrgClient """
        mock_get.return_value = self.org_payload
        client = GithubOrgClient("test_org")
        self.assertEqual(client.org, self.org_payload)
        mock_get.assert_called_once_with("http://example.com/repos")

    # Task 7
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test has_license method of GithubOrgClient """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    # Task 8
    @classmethod
    def setUpClass(cls):
        """ Set up test class """
        patcher = patch('client.get_json')
        cls.mock_get = patcher.start()
        cls.mock_get.return_value = [{"name": "test_repo"}]

    @classmethod
    def tearDownClass(cls):
        """ Tear down test class """
        cls.mock_get.stop()

    def test_public_repos(self):
        """ Test public_repos method of GithubOrgClient """
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, ["test_repo"])

    # Task 9
    def test_public_repos_with_license(self):
        """ Test public_repos method of GithubOrgClient with license """
        client = GithubOrgClient("test_org")
        with patch.object(client, 'has_license', return_value=True):
            repos = client.public_repos("apache-2.0")
            self.assertEqual(repos, ["test_repo"])


if __name__ == "__main__":
    unittest.main()
