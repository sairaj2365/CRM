import pytest
import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
import utils.read_utility as reader
from pages.webform_po import Webform
from utils.actions import Action

testdata = "./test_data/test_webform.csv"

# @pytest.mark.webform
# def test_page_url_path_fr(set_up) -> None:
#     login_data = reader.read_test_data(testdata, Action.get_current_test_name())
#     expected_partial_url = login_data[0]
#     page = set_up
#     action_obj = Action(page)
#     action_obj.verify_current_url(expected_partial_url)

# @pytest.mark.webform
# def test_page_title_fr(set_up) -> None:
#     login_data = reader.read_test_data(testdata, Action.get_current_test_name())
#     page_title = login_data[1]
#     page = set_up
#     action_obj = Action(page)
#     action_obj.verify_page_title(page_title)

# @pytest.mark.webform
# def test_meta_description(set_up) -> None:
#     page = set_up
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     webform_obj.meta_description_check()

# @pytest.mark.webform
# def test_alt_tag_logo_and_brand_image(set_up) -> None:
#     page = set_up
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     webform_obj.check_img_alt_tags("logo")
#     webform_obj.check_img_alt_tags("brand")

# @pytest.mark.webform
# def test_href_lang(set_up) -> None:
#     page = set_up
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     webform_obj.check_href_lang("EN")
#     webform_obj.check_href_lang("FR")

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_prod)
def test_privacy_policy(url, page: Page) -> None:
    page.set_default_timeout(300000)
    page.goto(url)
    webform_obj = Webform(page)
    webform_obj.check_privacy_policy("FR")