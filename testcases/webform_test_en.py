import pytest
import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
import utils.read_utility as reader
from pages.webform_po import Webform
from utils.actions import Action

testdata = "./test_data/test_webform.csv"
testdata_form = "./test_data/form_data.csv"

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_page_url_path(url, browser : Browser) -> None:
#     context = browser.new_context(
#         record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(300000)
#     page.goto(url)
#     login_data = reader.read_test_data(testdata, Action.get_current_test_name())
#     expected_partial_url = login_data[0]
#     action_obj = Action(page)
#     action_obj.verify_current_url(expected_partial_url)
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_page_title(url, page: Page) -> None:
#     page.set_default_timeout(300000)
#     page.goto(url)
#     login_data = reader.read_test_data(testdata, Action.get_current_test_name())
#     page_title = login_data[1]
#     webform_obj = Webform(page)
#     webform_obj.verify_page_title(page_title)

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_meta_description(url, page: Page) -> None:
#     page.set_default_timeout(300000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     webform_obj.meta_description_check()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_img_alt_tags(url, browser : Browser, playwright: Playwright) -> None:  #playwright: Playwright - device viewport
#     iphone_13 = playwright.devices['iPhone 13']
#     context = browser.new_context(
#         record_video_dir= "video/",
#         **iphone_13
#     )
#     page = context.new_page()
#     page.set_default_timeout(300000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     webform_obj.check_img_alt_tags("logo")
#     webform_obj.check_img_alt_tags("brand")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_href_lang(url, page: Page) -> None:
#     page.set_default_timeout(300000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     webform_obj.check_href_lang("EN")
#     webform_obj.check_href_lang("FR")

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_privacy_policy(url, page: Page) -> None:
#     page.set_default_timeout(300000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     webform_obj.check_privacy_policy("EN")

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_page(url, browser : Browser) -> None:
#     context = browser.new_context(
#         record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(300000)
#     page.goto(url)
#     login_data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate = login_data[0], login_data[1], login_data[2], login_data[3]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate)
#     webform_obj.submit_button()
#     page.close()

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
def test_empty_form(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    page = context.new_page()
    page.set_default_timeout(300000)
    page.goto(url)
    login_data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    name_error, email_error, verify_email_error, checkbox_error, recaptcha_error = login_data[4], login_data[5], login_data[6], login_data[7], login_data[8]
    webform_obj = Webform(page)
    webform_obj.submit_button()
    webform_obj.error_messages_empty_fields(name_error, email_error, verify_email_error, checkbox_error, recaptcha_error)
    page.close()