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

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_img_alt_tags(url, page: Page) -> None:
    #page.set_default_timeout(80000)
    page.goto(url)
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.check_image_alt_tag("FR")

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_close_icon_alt_fr(url, page: Page) -> None:
    page.set_default_timeout(80000)
    page.goto(url)
    data = reader.read_test_data(lightbox_privacy_data, Action.get_current_test_name())
    input_data_1 = data[0]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.check_close_icon_alt_tag("FR", input_data_1)

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_empty_form_fr(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/missing_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    name_error, email_error, verify_email_error, recaptcha_error = data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "empty")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_fr(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_name_fr_1(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_name_fr_2(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_name_fr_3(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_name_fr_4(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_name_fr_5(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_name_fr_6(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_name_fr_7(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_name_fr_8(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_email_fr_1(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_email_fr_2(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_email_fr_3(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_email_fr_4(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_invalid_data_invalid_email_fr_5(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/LB/invalid_entries"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, name_error, email_error, verify_email_error, recaptcha_error = data[0], data[1], data[2], data[5], data[6], data[7], data[9]
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "invalid")
    lightbox_obj.submit_button()
    lightbox_obj.error_messages_fields(name_error, email_error, verify_email_error, recaptcha_error, "invalid")
    page.close()

# @pytest.mark.lightbox
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
# def test_form_page(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, input_data_1, brand_text, alt_tag, text_content = data[0], data[1], data[2], data[9], data[10], data[11], data[12]
#     action_obj = Action(page)
#     lightbox_obj = Lightbox(page)
#     action_obj.closeCookiePopup()
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     lightbox_obj.submit_button()
#     lightbox_obj.check_thankyou_modal_content(text_content)
#     # lightbox_obj.check_close_icon_alt_tag("EN", input_data_1)
#     # lightbox_obj.check_image_alt_tag("EN", brand_text)
#     # lightbox_obj.check_checkmark_image_alt_tag(alt_tag)
#     # page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_lightbox_links(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.verify_links()
    page.close()

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# # def test_lightbox_content_fr(url, browser : Browser) -> None:
# #     context = browser.new_context(
# #         #record_video_dir= "video/"
# #     )
# #     page = context.new_page()
# #     page.set_default_timeout(200000)
# #     page.goto(url)
# #     data = reader.read_test_data(lightbox_privacy_data, Action.get_current_test_name())
# #     content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four = data[2], data[3], data[4], data[5], data[6], data[7]
# #     lightbox_obj = Lightbox(page)
# #     lightbox_obj.verify_lightbox_content("FR", content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four)
# #     page.close()

# # # @pytest.mark.webform
# # # @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
# # # def test_form_page_generic_message_fr(url, browser : Browser) -> None:
# # #     context = browser.new_context(
# # #         #record_video_dir= "video/"
# # #     )
# # #     page = context.new_page()
# # #     page.set_default_timeout(80000)
# # #     page.goto(url)
# # #     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
# # #     firstname, emailid, verify_email, recaptcha_error = data[0], data[1], data[2], data[8]
# # #     action_obj = Action(page)
# # #     lightbox_obj = Lightbox(page)
# # #     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "recaptcha")
# # #     action_obj.closeCookiePopup()
# # #     lightbox_obj.submit_button()
# # #     lightbox_obj.recaptcha_error_check(recaptcha_error, "generic")
# # #     page.close()

# # # @pytest.mark.webform
# # # @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
# # # def test_form_page_registered_error_message_fr(url, browser : Browser) -> None:
# # #     context = browser.new_context(
# # #         #record_video_dir= "video/"
# # #     )
# # #     page = context.new_page()
# # #     page.set_default_timeout(80000)
# # #     page.goto(url)
# # #     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
# # #     firstname, emailid, verify_email, recaptcha_error = data[0], data[1], data[2], data[8]
# # #     action_obj = Action(page)
# # #     lightbox_obj = Lightbox(page)
# # #     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "recaptcha")
# # #     action_obj.closeCookiePopup()
# # #     lightbox_obj.submit_button()
# # #     lightbox_obj.recaptcha_error_check(recaptcha_error, "registered")
# # #     page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_page_addresses_do_not_match_fr(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, email_error_text = data[0], data[1], data[2], data[7]
    action_obj = Action(page)
    webform_obj = Webform(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
    lightbox_obj.submit_button()
    lightbox_obj.email_address_error_check("", email_error_text, "no-match")
    page.close()

@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_lightbox_not_displayed_on_close(url, page: Page) -> None:
    #page.set_default_timeout(300000)
    page.goto(url)
    action_obj = Action(page)
    lightbox_obj = Lightbox(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_not_displayed_on_close()
    page.close()

#Email address do not match
@pytest.mark.lightbox
@pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home)
def test_form_page_addresses_do_not_match_gmail_com_fr(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/"
    )
    page = context.new_page()
    page.set_default_timeout(100000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[6], data[7]
    lightbox_obj = Lightbox(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    page.reload()
    lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
    lightbox_obj.submit_button()
    lightbox_obj.email_address_error_check(email_error,email_error_text, "")
    page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_page_addresses_do_not_match_gmail_ca_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_page_addresses_do_not_match_hotmail_com_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_page_addresses_do_not_match_hotmail_ca_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_page_addresses_do_not_match_outlook_com_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_page_addresses_do_not_match_outlook_ca_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()


# #Form invalid addressess
# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_invalid_addresses_gmail_com_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_invalid_addresses_gmail_ca_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_invalid_addresses_hotmail_com_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_invalid_addresses_hotmail_ca_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_invalid_addresses_outlook_com_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_fr_home_prod)
# def test_form_invalid_addresses_outlook_ca_fr(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     lightbox_obj = Lightbox(page)
#     action_obj = Action(page)
#     lightbox_obj.lightbox_form(firstname, emailid, verify_email, "verify_email")
#     action_obj.closeCookiePopup()
#     lightbox_obj.submit_button()
#     lightbox_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()