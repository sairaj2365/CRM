import pytest
import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
import utils.read_utility as reader
from pages.lightbox_po import Lightbox
from utils.actions import Action

lightbox_privacy_data = "./test_data/lightbox_privacy_policy.csv"

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_privacy_policy_fr(url, page: Page) -> None:
    page.set_default_timeout(300000)
    page.goto(url)
    data = reader.read_test_data(lightbox_privacy_data, Action.get_current_test_name())
    input_data_1, input_data_2 = data[0], data[1]
    lightbox_obj = Lightbox(page)
    lightbox_obj.check_privacy_policy("FR", input_data_1, input_data_2)