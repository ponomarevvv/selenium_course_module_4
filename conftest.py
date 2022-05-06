from selenium.webdriver import Firefox, FirefoxProfile, Chrome
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en-gb",
        help="Choose language",
        choices=(
            "en-gb",
            "fr",
            "es",
            "cs",
            "da",
            "de",
            "fi",
            "it",
            "ru",
        ),
    )

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="options available: chrome, firefox",
        choices=("chrome", "firefox"),
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("--language")
    browser = None
    if browser_name == "firefox":
        fp = FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart Firefox browser for test...")
        browser = Firefox(firefox_profile=fp)
    elif browser_name == "chrome":
        oprions = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        print("\nstart Chrome browser for test...")
        browser = Chrome(options=options)
    else:
        raise pytest.UsageError("--browser should be `chrome` or `firefox`")
    yield browser
    print("\nquit browser...")
    browser.quit()

