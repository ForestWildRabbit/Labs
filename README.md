# Labs

### Info

Labs topics are based on OWASP Top 10.

Labs are located in `./labs_backend/labs_src`.
 
For now there are 3 labs:

- `sql_injection_lab`
- `broken_access_control_lab`
- `cryptographic_failures_lab`
- `security_misconfiguration_lab`

Students should write code in files in `./labs_backend/labs_src/app/student_code`.

Copy of that files is in `./labs_backend/labs_src/app/student_code_src`.

Solutions located in `./labs_backend/labs_src/app/solutions`.

Labs are independent: can be solved in any order. A solved lab must pass all tests attached to it.

#### Tests

Tests located in `./labs_backend/labs_src/app/tests`.

Tests in filenames started with `test` will be launched by `run_tests.py` file in `./labs_backend`.

### Launch

Change directory `cd ./labs_backend`

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
  

### Next labs will be released

- `insecure_design`