# Unit Tests

- The unit_tests.py contains 9 unit tests.
- These unit tests are used to test each web scrapper to check if the expected and actual data type are same. The data contents can not be used for unit testing as our data is updated regularly.
- The unit test also tests get_response.py file as it is important as the BOT fetches its response from this file.

# Running Unit Tests

- The unit test is created using unittest library.
- The web scrapping and get_response programs are imported to unit test file.
- The unit test can be executed only when the web scrapping programs and get_response program are in the same directory.
- Since unittest library is used, the program can be directly executed without creation of any objects or providing any input.
