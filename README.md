# Labs

### Info

Labs topics are based on OWASP Top 10.

Labs module is located in `./labs_backend/labs_src`.
 
For now there are 6 labs:

- `sql_injection_lab`
- `broken_access_control_lab`
- `cryptographic_failures_lab`
- `security_misconfiguration_lab`
- `insecure_design_lab`
- `security_logging_failures_lab`

Students should write code in files in directory `/labs_backend/labs_src/app/student_code`.

e.g. `/labs_backend/labs_src/app/student_code/code_sql_injection_lab.py`

Copy of that files is in `./labs_backend/labs_src/app/student_code_src`.

e.g. `/labs_backend/labs_src/app/student_code/src_sql_injection_lab.py`

Possible labs' solutions located in `/labs_backend/labs_src/app/solutions`.

e.g. `/labs_backend/labs_src/app/student_code/solution_sql_injection_lab.py`

Labs are independent: can be solved in any order. A solved lab must pass all tests attached to it.

#### Tests

Tests located in `/labs_backend/labs_src/app/tests`.

Test filename pattern is `test_<lab_name>.py`.

e.g. `/labs_backend/labs_src/app/tests/test_sql_injection_lab.py`

Tests will try to exploit the given vulnerability, a lab code must be safe to pass all attached tests.

The one of tests to sql_injection_lab:

![sql_injection_lab test example](/assets/images/sql_injection_lab_test.png)

### Launch

Change directory `cd .../labs_backend`

Activate virtual environment in your OS (optional).

Install dependencies `pip install -r ./labs_src/requirements.txt`

There is a file `run_tests.py` that runs a lab and attached tests.

#### CLI (recommended)

Run `python run_tests.py <lab_name>`

e.g. `python run_tests.py sql_injection_lab`

There is an option to run all labs `python run_tests.py all`.

#### Docker Compose

The application can be run via Docker Compose.

Change directory `cd ./labs_backend/labs_src`

Run application `docker-compose up --build`

Run tests `docker-compose exec app pytest <path_to_test_file>`

e.g. `docker-compose exec app pytest ./app/tests/test_sql_injection_lab.py`

There is also an option to run all labs `docker-compose exec app pytest`


### API

Launch `docker-compose up --build`

- POST `127.0.0.1:8000/upload`

  BODY
  ```
  {
      file: File
      lab_name: string
  }
  ```
    
  RESPONSE
  Archive (.zip file) of `labs_src` directory with uploaded file.

- STATIC `127.0.0.1:8000/static`

  Mounted `labs_src` directory
  Fetch file example `http://127.0.0.1:8000/static/app/student_code/code_sql_injection_lab.py`
  
