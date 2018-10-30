# Case
We want to make smoke tests to verify that http://beta.rikstoto.no works as expected in production, and you are the test developer in the project. The first phase of the project is considered to be a "mini-pilot".

We are considering to use Selenium in Python to implement the smoke tests, and we are starting with the front page. 

The initial analysis has been completed and we found that 3 tests are needed to test the frontpage.

Implement the missing tests to [frontpage_tests.py](tests/frontpage_tests.py)

Your are free to refactor/restructure the code as you see fit.

## Time Restrictions
The the solution shall be delivered within Friday November 2nd at 11:00.

The solution is submitted by sending the file frontpage_tests.py to roger.hoem-martinsen@rikstoto.no

There are no time restrictions to this case, other than the deadline.

# What are we looking for?
We are looking for:
* Clear understanding on how (and why) use Selenium and Python
* Clean code

Note that you will be given the opportunity to explain how you think during the interview. We will also have a small discussion about the choice of framwork. Do you have any proposal for other frameworks to use?

# Getting started
## Install
Install requirements:
pip install -r requirement.txt

If any problems, refer to:
https://selenium-python.readthedocs.io/installation.html#introduction

## Run Pytest
pytest -c .\python.ini
