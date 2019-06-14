"""Find flaky test cases in a pytest test suite."""

__version__ = '0.1.0'


def pytest_addoption(parser):
    """Turn on fleetflakefinder features on with --fff option."""
    group = parser.getgroup("fleetflakefinder")
    group.addoption(
        "--fff",
        action="store_true",
        help="pytest_fleetflakefinder: find flaky tests in pytest test suite",
    )


def pytest_report_header(config):
    """Display diagnostic message to show the use of the plugin."""
    if config.getoption("fff"):
        return "Using --fff"
