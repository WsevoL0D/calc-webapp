import pytest
def pytest_addoption(parser):
    parser.addoption("--port", type=int, help="Server port of the target", required=True)
    parser.addoption("--host", type=str, help="Target server's name/address", required=False)

@pytest.fixture()
def endpoint(pytestconfig):
  # 'default' value parameter for .getoption works only if option has not been added to parser so we have to make this ternary
  port = pytestconfig.getoption("port") if pytestconfig.getoption("port") != None else "8000"
  server = pytestconfig.getoption("host") if pytestconfig.getoption("host") != None else "127.0.0.1"
  return f"http://{server}:{port}"