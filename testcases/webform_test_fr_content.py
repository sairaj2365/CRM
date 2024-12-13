import pytest
import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
import utils.read_utility as reader
from pages.lightbox_po import Lightbox
from pages.webform_po import Webform
from utils.actions import Action

testdata = "./test_data/test_webform.csv"
testdata_form = "./test_data/form_data.csv"

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_prod)
def test_webform_content_fr(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    page = context.new_page()
    page.set_default_timeout(200000)
    page.goto(url)
    data = reader.read_test_data(testdata, Action.get_current_test_name())
    content_one, content_two, checkbox_content, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four = data[9], data[10], data[11], data[12], data[13], data[14], data[15]
    webform_obj = Webform(page)
    webform_obj.verify_webform_content("FR", content_one, content_two, checkbox_content, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four)
    page.close()

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_prod)
def test_dob_text_fr(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    page = context.new_page()
    page.set_default_timeout(200000)
    page.goto(url)
    data = reader.read_test_data(testdata, Action.get_current_test_name())
    dob_content = data[18]
    webform_obj = Webform(page)
    webform_obj.verify_dob_content(dob_content, "FR")
    page.close()

