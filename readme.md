# Python Mock One
Learning the Python PyTest Mock library

## Developer Setup
- create virtual environment
- install libraries via pip
- create .env file
- launch is set to start with the main.py file open

**2022-10-21**
I've been able to get a basic mock working, not sure if I'm doing it 'right' but the patch works.

**2022-11-04**
Continuing on, now working on mocking a postgres database, first thing I'll do is add a test database and get the read working 'normally' then I'll mock a different value and the test should return the different value.

Reference for this section is the tutorial at https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/

**2022-11-06**
Moving configuration over to poetry, trying to fix the pytest bug with proper configuration?

**2022-11-17**
~~Still fighting with the configuration of pytest, the program runs properly but I can't get pytest to run.~~ OK, I added `pythonpath = "."` to the pytest section in the `pyproject.toml` file and it's _mostly_ working now. I've also learned that `python -m pytest` is NOT the same as `pytest`, the full command adds the current directory to the path, which is what I needed. Now I can figure out the patching.



