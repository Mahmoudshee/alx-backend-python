#!/usr/bin/env python3
""" Utility functions for the tasks """

import requests
from functools import wraps


def access_nested_map(nested_map, path):
    """ Access nested items in a dictionary """
    for key in path:
        if key in nested_map:
            nested_map = nested_map[key]
        else:
            return None
    return nested_map


def get_json(url):
    """ Send a GET request and parse JSON response """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def memoize(func):
    """ Memoize decorator to cache function results """
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper
