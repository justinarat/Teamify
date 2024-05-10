# cits3403-project

## About the project

## Project Group

| UWA ID   | Name        | Github     |
| -------- | ----------- | ---------- |
| 23080798 | Justin Arat | justinarat |
| 23431003 | Dominic Davies | dominictdavies |
| 23395411  | John Giampaolo | JohnGiampaolo |
| 22992693  | Fatimah Ali O Aljanobi | FAljanobi |

## Summary of Application Architecture

## How to launch the application

1. Create a virtual environment `python3 -m venv .venv`
2. Activate the virtual environment `source .venv/bin/activate`
3. Install project requirements `pip install -r requirements.txt`
4. Set the environment variable (use a different key instead of "poor secret")
    `CITS3403_FLASK_SECRET_KEY="poor secret"` 
5. Start up the flask server `flask run`

## How to run the tests

First, in a separate terminal start up the flask server if it's not running:
`flask run`

To run all tests:
`python -m unittest`

To run specific test modules:
`python -m unittest tests.test_file`
