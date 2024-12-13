import pytest
import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
import utils.read_utility as reader
from pages.webform_po import Webform
from pages.lightbox_po import Lightbox
from utils.actions import Action

lightbox_privacy_data = "./test_data/lightbox_privacy_policy.csv"
testdata = "./test_data/test_webform.csv"
testdata_form = "./test_data/form_data.csv"

# @pytest.mark.lightbox
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
# def test_lightbox_content_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.goto(url)
#     page.set_default_timeout(2000000)
#     data = reader.read_test_data(lightbox_privacy_data, Action.get_current_test_name())
#     content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four = data[2], data[3], data[4], data[5], data[6], data[7]
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     lightbox_obj.verify_lightbox_content("FR", content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four)
#     page.close()

# @pytest.mark.lightbox
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
# def test_lightbox_required_field_text_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.goto(url)
#     page.set_default_timeout(2000000)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     text_content, firstname, email, verifyemail = data[4], data[5], data[6], data[7]
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     lightbox_obj.verify_lightbox_required_text(firstname, email, verifyemail)
#     page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_placeholder_text(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(2000000)
    lightbox_obj = Lightbox(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    lightbox_obj.verify_placeholder_text(config.Config.first_name_placeholder_fr, config.Config.email_placeholder_fr, config.Config.verify_email_placeholder_fr)
    page.close()