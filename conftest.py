from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language",
        choices=(
            "en",
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
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", user_language)
        print("\nstart Firefox browser for test...")
        browser = Firefox(firefox_profile=options.profile)
    elif browser_name == "chrome":
        options = OptionsChrome()
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        print("\nstart Chrome browser for test...")
        browser = Chrome(options=options)
    else:
        raise pytest.UsageError("--browser should be `chrome` or `firefox`")
    yield browser
    print("\nquit browser...")
    browser.quit()

