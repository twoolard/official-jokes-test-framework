@programming
Feature: Official Jokes API
    As a system user I want to be able to generate programming jokes.

    @random
    Scenario: get a random programming jokes
        Given The Official Jokes API is queried for a random programming joke
        Then the response status code is "200"
        And the returned joke is of type "programming"

    @tenJokes
    Scenario: get ten programming jokes
        Given The Official Jokes API is queried for ten programming jokes
        Then the response status code is "200"
        And ten jokes are returned
        And all jokes are of type "programming" 
