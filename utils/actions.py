import inspect
from playwright.sync_api import Playwright, sync_playwright, Page, Browser, expect


class Action:
    def __init__(self, page):
        self.page = page

    def verify_current_url(self, expected_partial_url):
        try:
            self.page.wait_for_timeout(10000)
            current_url = self.page.url
            assert expected_partial_url in current_url, f"Expected '{expected_partial_url}' to be present in URL, but it is not. Current URL: {current_url}"
            print(f"URL verified to contain : '{expected_partial_url}'")
        except TimeoutError:
            print(f"URL did not contain '{expected_partial_url}'")

    @classmethod
    def get_current_test_name(cls):
        frame = inspect.currentframe().f_back
        method_name = frame.f_code.co_name
        return method_name
    