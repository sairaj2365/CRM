import pytest
import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
import utils.read_utility as reader
from pages.lightbox_po import Lightbox
from pages.webform_po import Webform
from utils.actions import Action

lightbox_privacy_data = "./test_data/lightbox_privacy_policy.csv"
testdata = "./test_data/test_webform.csv"
testdata_form = "./test_data/form_data.csv"


# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home)
# def test_privacy_policy_en(url, page: Page) -> None:
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(lightbox_privacy_data, Action.get_current_test_name())
#     input_data_1, input_data_2 = data[0], data[1]
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.check_privacy_policy("EN", input_data_1, input_data_2)


# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home_prod)
# def test_img_alt_tags(url, page: Page) -> None:
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     brand_text = data[3]
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.check_image_alt_tag("EN", brand_text)

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home_prod)
# def test_close_icon_alt_en(url, page: Page) -> None:
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(lightbox_privacy_data, Action.get_current_test_name())
#     input_data_1 = data[0]
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.check_close_icon_alt_tag("EN", input_data_1)

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home_prod)
# def test_empty_form(url, browser : Browser) -> None:
#     context = browser.new_context(
#         record_video_dir= "video/content/english/LB/missing_entries"
#     )
#     page = context.new_page()
#     page.set_default_timeout(100000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     name_error, email_error, verify_email_error, recaptcha_error = data[4], data[5], data[6], data[8]
#     action_obj = Action(page)
#     lightbox_obj = Lightbox(page)
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "empty")
#     page.close()

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home)
# # def test_form_page(url, browser : Browser) -> None:
# #     context = browser.new_context(
# #         #record_video_dir= "video/"
# #     )
# #     page = context.new_page()
# #     page.set_default_timeout(80000)
# #     page.goto(url)
# #     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
# #     firstname, emailid, verify_email, input_data_1, brand_text, alt_tag, text_content = data[0], data[1], data[2], data[9], data[10], data[11], data[12]
# #     action_obj = Action(page)
# #     lightbox_obj = Lightbox(page)
# #     lightbox_obj.lightbox_form(firstname, emailid, verify_email)
# #     action_obj.closeCookiePopup()
# #     lightbox_obj.submit_button()
# #     lightbox_obj.check_close_icon_alt_tag("EN", input_data_1)
# #     lightbox_obj.check_image_alt_tag("EN", brand_text)
# #     lightbox_obj.check_checkmark_image_alt_tag(alt_tag)
# #     lightbox_obj.check_thankyou_modal_content(text_content)
# #     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home_prod)
# def test_form_invalid_data(url, browser : Browser) -> None:
#     context = browser.new_context(
#         record_video_dir= "video/content/english/LB/invalid_entries"
#     )
#     page = context.new_page()
#     page.set_default_timeout(100000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[4], data[5], data[6], data[8]
#     action_obj = Action(page)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home_prod)
# def test_webform_links(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(100000)
#     page.goto(url)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.verify_links('EN')
#     page.close()

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home)
def test_lightbox_content(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    page = context.new_page()
    page.set_default_timeout(200000)
    page.goto(url)
    data = reader.read_test_data(lightbox_privacy_data, Action.get_current_test_name())
    content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four = data[2], data[3], data[4], data[5], data[6], data[7]
    lightbox_obj = Lightbox(page)
    lightbox_obj.verify_lightbox_content("EN", content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four)
    page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home)
# def test_form_recaptcha_generic(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, recaptcha_error = data[0], data[1], data[2], data[8]
#     action_obj = Action(page)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "recaptcha")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.recaptcha_error_check(recaptcha_error, "generic")

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home)
# def test_form_page_registered_error_message(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, recaptcha_error = data[0], data[1], data[2], data[8]
#     action_obj = Action(page)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "recaptcha")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.recaptcha_error_check(recaptcha_error, "registered")

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home_prod)
# def test_form_page_addresses_do_not_match(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error_text = data[0], data[1], data[2], data[6]
#     action_obj = Action(page)
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     webform_obj.email_address_error_check(email_error_text)
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home_prod)
# def test_lightbox_not_displayed_on_close(url, page: Page) -> None:
#     page.set_default_timeout(300000)
#     page.goto(url)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_not_displayed_on_close()
#     page.close()
