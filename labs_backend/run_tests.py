import os
import sys
import subprocess

DOCKER_COMPOSE_PATH = "./labs_src"

path_table = {
    'sql_injection_lab': "./app/tests/test_sql_injection_lab.py",
    'broken_access_control_lab': "./app/tests/test_broken_access_control_lab.py",
    'cryptographic_failures_lab': "./app/tests/test_cryptographic_failures_lab.py",
    'security_misconfiguration_lab': "./app/tests/test_security_misconfiguration_lab.py",
    'insecure_design_lab': "./app/tests/test_insecure_design_lab.py",
    'security_logging_failures_lab': "./app/tests/test_security_logging_failures_lab.py",

    'C01_vulnerable_dependencies_lab' : "./app/tests/test_C01_vulnerable_dependencies",
    'C02_access_control_lab' : "./app/tests/test_C02_access_control",
    'C03_file_handling_lab' : "./app/tests/test_C03_file_handling",
    'C04_insufficient_authentication_lab' : "./app/tests/test_C04_insufficient_authentication",
    'C05_code_injection_lab' : "./app/tests/test_C05_code_injection",
    'C06_command_injection_lab' : "./app/tests/test_C06_command_injection",
    'C07_weak_cryptography_lab' : "./app/tests/test_C07_weak_cryptography",
    'C08_privilege_escalation_lab' : "./app/tests/test_C08_privilege_escalation",
    'C09_authentication_bypass_lab' : "./app/tests/test_C09_authentication_bypass",
    'C10_race_conditions_lab' : "./app/tests/test_C10_race_conditions",

    'all': "./app/tests"
}


def run_docker_compose_up():
    os.chdir(DOCKER_COMPOSE_PATH)
    subprocess.run(
        ["docker-compose", "up", "--build", "-d"],
        check=True,
    )


def run_tests(test_file_path):
    command = [
        "docker-compose", "exec", "app", "pytest", test_file_path
    ]
    subprocess.run(command)


def stop_docker_services():
    print("Stopping services...")
    subprocess.run(
        ["docker-compose", "down"],
        check=True,
    )


def main():
    if len(sys.argv) != 2:
        print("Usage: python run_tests.py <test_file_path>")
        sys.exit(1)

    lab_name = sys.argv[1]

    if lab_name not in path_table:
        print("Invalid path")
        sys.exit(1)

    test_file_path = path_table[lab_name]

    try:
        run_docker_compose_up()
        run_tests(test_file_path)
    finally:
        stop_docker_services()


if __name__ == "__main__":
    main()
