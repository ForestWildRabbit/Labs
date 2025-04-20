import subprocess
import os


DOCKER_COMPOSE_PATH = "./labs_src"
SERVICE_NAME = "app"


def run_tests_in_docker():
    os.chdir(DOCKER_COMPOSE_PATH)

    command = [
        "docker-compose",
        "run", "--rm", "--build",
        SERVICE_NAME,
        "pytest",
        "--disable-warnings",
        "-q"
    ]

    try:
        print(f"Running tests in service: {SERVICE_NAME}")
        result = subprocess.run(command, capture_output=True, text=True)

        print(result.stdout)

        if result.returncode == 0:
            print("✅ All tests passed.")
            return True
        else:
            print("❌ Some tests failed.")
            print(result.stderr)
            return False

    except subprocess.CalledProcessError as e:
        print(f"⚠️ Error while running the tests: {e}")
        return False


def main():
    run_tests_in_docker()


if __name__ == "__main__":
    main()
