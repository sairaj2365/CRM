import pytest
import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
import utils.read_utility as reader
#from applitools.playwright import Eyes, Target
from playwright.sync_api import Page
from pages.lightbox_po import Lightbox
from pages.webform_po import Webform
from utils.actions import Action

lightbox_privacy_data = "./test_data/lightbox_privacy_policy.csv"
testdata = "./test_data/test_webform.csv"
testdata_form = "./test_data/form_data.csv"

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home)
def test_lightbox_content(url, browser : Browser, page: Page) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    # page = context.new_page()
    #page.set_default_timeout(200000)
    page.goto(url)
    #eyes.check(Target.window().fully().with_name("Lightbox Modal"))
    data = reader.read_test_data(lightbox_privacy_data, Action.get_current_test_name())
    content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four = data[2], data[3], data[4], data[5], data[6], data[7]
    lightbox_obj = Lightbox(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    lightbox_obj.verify_lightbox_content("EN", content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four)
    #lightbox_obj.verify_bold_text()
    #eyes.check("Form Elements", Target.region(".lightbox-form").layout())
    #eyes.check("Bold Text", Target.text("$5 off my next purchase of eligible Kenvue products").font("font-family", "font-weight: bold"))
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home)
def test_lightbox_required_field_text(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    page = context.new_page()
    page.set_default_timeout(200000)
    page.goto(url)
    data = reader.read_test_data(testdata, Action.get_current_test_name())
    text_content, firstname, email, verifyemail = data[4], data[5], data[6], data[7]
    lightbox_obj = Lightbox(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    lightbox_obj.verify_lightbox_required_text(text_content, firstname, email, verifyemail)
    page.close()

