"""
This module contains step definitions for the programmingJokes.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import requests

from pytest_bdd import scenario, given, then, parsers

# Constants
HOST = "https://officialjokeapi.onrender.com/jokes/programming"

@scenario('../features/programmingJokes.feature', 'get a random programming jokes')
def test_random():
    pass

@scenario('../features/programmingJokes.feature', 'get ten programming jokes')
def test_get_ten():
    pass

@given('The Official Jokes API is queried for a random programming joke', target_fixture='response')
def random_response():
    response = requests.get(url=f'{HOST}/random')
    return response

@given('The Official Jokes API is queried for ten programming jokes', target_fixture='response')
def list_response():
    response = requests.get(url=f'{HOST}/ten')
    return response

@then(parsers.parse('the response status code is "{code:d}"'))
def response_code(response, code):
    assert response.status_code == code

@then(parsers.parse('the returned joke is of type "{type}"'))
def validate_type(response, type):
    json = response.json()
    assert json[0]['type'] == type

@then(parsers.parse('ten jokes are returned'))
def count_list(response):
    json = response.json()
    assert len(json) == 10

@then(parsers.parse('all jokes are of type "{type}"'))
def validate_list_type(response, type):
    json = response.json()
    for joke in json:
        assert joke['type'] == type