import pytest
import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
import utils.read_utility as reader
from pages.webform_po import Webform
from pages.lightbox_po import Lightbox
from utils.actions import Action


testdata = "./test_data/test_webform.csv"
testdata_form = "./test_data/form_data.csv"

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_webform_content(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC"
#     )
#     page = context.new_page()
#     page.set_default_timeout(200000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.verify_webform_content("EN")
#     page.close()

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
def test_webform_card_content(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/CC"
    )
    page = context.new_page()
    page.set_default_timeout(200000)
    page.goto(url)
    webform_obj = Webform(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    webform_obj.verify_webform_card_content("EN")
    page.close()

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
def test_webform_required_text(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/CC"
    )
    page = context.new_page()
    page.set_default_timeout(200000)
    page.goto(url)
    webform_obj = Webform(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    webform_obj.verify_dob_and_required_field_content(config.Config.first_name, config.Config.email, config.Config.verify_email, config.Config.birthDate)
    page.close()

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
def test_placeholder_text(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/CC"
    )
    page = context.new_page()
    page.set_default_timeout(200000)
    page.goto(url)
    webform_obj = Webform(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    webform_obj.verify_placeholder_text(config.Config.first_name_placeholder, config.Config.email_placeholder, config.Config.verify_email_placeholder, config.Config.month, config.Config.day)
    page.close()

