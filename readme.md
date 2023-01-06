# Python Mock One

Learning the Python PyTest Mock library

## Developer Setup

- create virtual environment
- install libraries via pip
- create `.env` file
- launch is set to start with the `main.py` file open

**2022-10-21**
I've been able to get a basic mock working, not sure if I'm doing it 'right' but the patch works.

**2022-11-04**
Continuing on, now working on mocking a Postgres database, first thing I'll do is add a test database and get the read working 'normally' then I'll mock a different value and the test should return the different value.

Reference for this section is the tutorial at https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/

**2022-11-06**
Moving configuration over to poetry, trying to fix the PyTest bug with proper configuration?

**2022-11-17**
~~Still fighting with the configuration of PyTest, the program runs properly but I can't get PyTest to run.~~ OK, I added `pythonpath = "."` to the pytest section in the `pyproject.toml` file and it's _mostly_ working now. I've also learned that `python -m pytest` is NOT the same as `pytest`, the full command adds the current directory to the path, which is what I needed. Now I can figure out the patching.

**2022-12-10**
I'm now pretty switched over to poetry, `pyproject.toml` and I'm now naming the virtual environment as `.venv`, apparently this helps with searching in vsCode as the `.venv` folder will be ignored by the search.

**2023-01-02**
Well I got it working for a little while, but now I'm having a path issue with the tests, either the tests work or the main works, I REALLY wish I understood python pathing properly... this is aggravating! The test can't find the main module (even though my linter doesn't complain)

**2023-01-06**
Got the test configuration figured out! I added a python path entry in the `pyproject.toml` file to include the `app` and `app/core` directories! That got everything working properly!!!

I am also trying out a new linter  - [ruff](https://github.com/charliermarsh/ruff) it suggests that it has near parity with flake8 but is configurable in `pyproject.toml`

By and large this completes this effort, I'm able to create the Postgres database, configure and run the tests and mock the Postgres database, now to move this knowledge into one of my own projects.