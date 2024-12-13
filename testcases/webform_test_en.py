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
# def test_page_url_path(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(300000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     expected_partial_url = data[0]
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     action_obj.verify_current_url(expected_partial_url)
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_page_title(url, page: Page) -> None:
#     #page.set_default_timeout(300000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     page_title = data[1]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.verify_page_title(page_title)

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
def test_meta_description(url, page: Page) -> None:
    page.goto(url)
    webform_obj = Webform(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    webform_obj.meta_description_check('EN', "")

@pytest.mark.webform
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
def test_brand_img_alt_tag(url, browser : Browser) -> None:  #playwright: Playwright - device viewport
    #iphone_13 = playwright.devices['iPhone 13']
    context = browser.new_context(
        #record_video_dir= "video/",
        #**iphone_13
    )
    page = context.new_page()
    page.set_default_timeout(80000)
    page.goto(url)
    webform_obj = Webform(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    webform_obj.check_brand_img_alt_tag('EN')
    page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_brand_logo_alt_tag(url, browser : Browser) -> None:  #playwright: Playwright - device viewport
#     #iphone_13 = playwright.devices['iPhone 13']
#     context = browser.new_context(
#         #record_video_dir= "video/",
#         #**iphone_13
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.check_brand_logo_alt_tag('EN')
#     page.close()


# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_card_icon_alt_tag(url, browser : Browser) -> None:  #playwright: Playwright - device viewport
#     #iphone_13 = playwright.devices['iPhone 13']
#     context = browser.new_context(
#         #record_video_dir= "video/",
#         #**iphone_13
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.check_card_icon_alt_tag('EN')
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_href_lang(url, page: Page) -> None:
#     page.set_default_timeout(100000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     href_en, href_fr = data[4], data[5]
#     webform_obj = Webform(page)
#     webform_obj.check_href_lang("EN", href_en)
#     webform_obj.check_href_lang("FR", href_fr)

# # # @pytest.mark.webform
# # # @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# # # def test_privacy_policy(url, page: Page) -> None:
# # #     page.set_default_timeout(300000)
# # #     page.goto(url)
# # #     webform_obj = Webform(page)
# # #     webform_obj.check_privacy_policy("EN")

# # # # @pytest.mark.webform
# # # # @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# # # # def test_form_page(url, browser : Browser) -> None:
# # # #     context = browser.new_context(
# # # #         #record_video_dir= "video/"
# # # #     )
# # # #     page = context.new_page()
# # # #     page.set_default_timeout(80000)
# # # #     page.goto(url)
# # # #     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
# # # #     firstname, emailid, verify_email, birthdate, thank_you_content_one, page_content_two, expected_url = data[0], data[1], data[2], data[3], data[13], data[14], data[15]
# # # #     webform_obj = Webform(page)
# # # #     action_obj = Action(page)
# # # #     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, "")
# # # #     webform_obj.submit_button()
# # # #     action_obj.verify_current_url(expected_url)
# # # #     webform_obj.verify_thankyou_page_content(thank_you_content_one, page_content_two)
# # # #     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_empty_form(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/missing_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     name_error, email_error, verify_email_error, checkbox_error, recaptcha_error = data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, checkbox_error, recaptcha_error, 'empty')
#     page.close()

#need to update birthdate error 
# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_name_1(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_name_2(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_name_3(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_name_4(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_name_5(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_name_6(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_name_7(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_name_8(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

@pytest.mark.webform 
@pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
def test_form_invalid_data_invalid_email_1(url, browser : Browser) -> None:
    context = browser.new_context(
        #record_video_dir= "video/content/english/CC/invalid_entries",
        #record_video_size={"width": 640, "height": 480}
    )
    page = context.new_page()
    #page.set_default_timeout(80000)
    page.goto(url)
    data = reader.read_test_data(testdata_form, Action.get_current_test_name())
    firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
    webform_obj = Webform(page)
    action_obj = Action(page)
    action_obj.closeCookiePopup()
    webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
    webform_obj.submit_button()
    webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
    page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_email_2(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_email_3(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_email_4(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()

# @pytest.mark.webform 
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_invalid_data_invalid_email_5(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/invalid_entries",
#         #record_video_size={"width": 640, "height": 480}
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, birthdate, month, name_error, email_error, verify_email_error, birthdate_error, recaptcha_error = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, birthdate, month, "invalid")
#     webform_obj.submit_button()
#     webform_obj.error_messages_fields(name_error, email_error, verify_email_error, birthdate_error, recaptcha_error, 'invalid')
#     page.close()
    
# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_webform_links(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     #page.set_default_timeout(100000)
#     page.goto(url)
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.verify_links()
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod_thankyou_page)
# def test_thankyou_page_url(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/content/english/CC/thankyou_page"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     expected_partial_url = data[0]
#     action_obj = Action(page)
#     action_obj.verify_current_url(expected_partial_url)
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod_thankyou_page)
# def test_thankyou_page_content(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     thank_you_content_one, page_content_two = data[16], data[17]
#     webform_obj = Webform(page)
#     webform_obj.verify_thankyou_page_content(thank_you_content_one, page_content_two)
#     page.close()

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# # def test_webform_content(url, browser : Browser) -> None:
# #     context = browser.new_context(
# #         #record_video_dir= "video/content/english/CC"
# #     )
# #     page = context.new_page()
# #     page.set_default_timeout(200000)
# #     page.goto(url)
# #     data = reader.read_test_data(testdata, Action.get_current_test_name())
# #     content_one, content_two, checkbox_content, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four = data[9], data[10], data[11], data[12], data[13], data[14], data[15]
# #     webform_obj = Webform(page)
# #     webform_obj.verify_webform_content("EN", content_one, content_two, checkbox_content, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four)
# #     page.close()

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# # def test_dob_text(url, browser : Browser) -> None:
# #     context = browser.new_context(
# #         #record_video_dir= "video/content/english/CC"
# #     )
# #     page = context.new_page()
# #     page.set_default_timeout(200000)
# #     page.goto(url)
# #     data = reader.read_test_data(testdata, Action.get_current_test_name())
# #     dob_content = data[18]
# #     webform_obj = Webform(page)
# #     webform_obj.verify_dob_content(dob_content, "EN")
# #     page.close()

# # # @pytest.mark.webform
# # # @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# # # def test_form_recaptcha_generic(url, browser : Browser) -> None:
# # #     context = browser.new_context(
# # #         #record_video_dir= "video/"
# # #     )
# # #     page = context.new_page()
# # #     page.set_default_timeout(80000)
# # #     page.goto(url)
# # #     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
# # #     firstname, emailid, verify_email, recaptcha_error = data[0], data[1], data[2], data[8]
# # #     webform_obj = Webform(page)
# # #     webform_obj.webform_form(firstname, emailid, verify_email, "", "recaptcha")
# # #     webform_obj.submit_button()
# # #     webform_obj.recaptcha_error_check(recaptcha_error, "generic")
# # #     page.close()

# # # @pytest.mark.webform
# # # @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# # # def test_form_page_registered_error_message(url, browser : Browser) -> None:
# # #     context = browser.new_context(
# # #         #record_video_dir= "video/"
# # #     )
# # #     page = context.new_page()
# # #     page.set_default_timeout(80000)
# # #     page.goto(url)
# # #     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
# # #     firstname, emailid, verify_email, recaptcha_error = data[0], data[1], data[2], data[8]
# # #     webform_obj = Webform(page)
# # #     webform_obj.webform_form(firstname, emailid, verify_email, "", "recaptcha")
# # #     webform_obj.submit_button()
# # #     webform_obj.recaptcha_error_check(recaptcha_error, "registered")
# # #     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod_thankyou_page)
# def test_href_lang_thank_you(url, page: Page) -> None:
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     href_en, href_fr = data[4], data[5]
#     webform_obj = Webform(page)
#     webform_obj.check_href_lang("EN", href_en)
#     webform_obj.check_href_lang("FR", href_fr)

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_lightbox_not_displayed_on_careclub_page(url, page: Page) -> None:
#     page.set_default_timeout(100000)
#     page.goto(url)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_not_displayed()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_lightbox_not_displayed_for_email_traffic(url, page: Page) -> None:
#     page.set_default_timeout(300000)
#     page.goto(url + config.Config.email_utm)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_not_displayed()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.jnj_privacy_policy_prod)
# def test_lightbox_not_displayed_on_privacy_policy_page(url, page: Page) -> None:
#     page.set_default_timeout(100000)
#     page.goto(url)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_not_displayed()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.jnj_ad_choices_prod)
# def test_lightbox_not_displayed_on_ad_choices_page(url, page: Page) -> None:
#     page.set_default_timeout(100000)
#     page.goto(url)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_not_displayed()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.jnj_accessibility_statement_prod)
# def test_lightbox_not_displayed_on_acessibility_statement_page(url, page: Page) -> None:
#     page.set_default_timeout(100000)
#     page.goto(url)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_not_displayed()

# # @pytest.mark.webform
# # @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home_prod)
# # def test_lightbox_not_displayed_on_page_not_found_page(url, page: Page) -> None:
# #     page.set_default_timeout(100000)
# #     page.goto(url + config.Config.page_not_found_path)
# #     lightbox_obj = Lightbox(page)
# #     lightbox_obj.lightbox_not_displayed()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.jnj_legal_notice_prod)
# def test_lightbox_not_displayed_on_legal_notice_page(url, page: Page) -> None:
#     page.set_default_timeout(100000)
#     page.goto(url)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_not_displayed()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.aveeno_hcp_prod)
# def test_lightbox_not_displayed_on_aveeno_hcp_page(url, page: Page) -> None:
#     page.set_default_timeout(100000)
#     page.goto(url)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_not_displayed()

#Special request scripts

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home)
# def test_lightbox_not_displayed_on_canada_en_pages(url, page: Page) -> None:
#     page.set_default_timeout(100000)
#     page.goto(url)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_not_displayed()


# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_page_url_path_careclub_page_redirection(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(300000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     expected_partial_url = data[0]
#     action_obj = Action(page)
#     action_obj.verify_current_url(expected_partial_url)
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_home_prod)
# def test_lightbox_displayed_on_canada_en_pages(url, page: Page) -> None:
#     #page.set_default_timeout(100000)
#     page.goto(url, timeout= 200000)
#     lightbox_obj = Lightbox(page)
#     lightbox_obj.lightbox_displayed(0)

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod_thankyou_page)
# def test_page_url_path_thankyou_page_redirection(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(300000)
#     page.goto(url)
#     data = reader.read_test_data(testdata, Action.get_current_test_name())
#     expected_partial_url = data[0]
#     action_obj = Action(page)
#     action_obj.verify_current_url(expected_partial_url)
#     page.close()


# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_page_addresses_do_not_match(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error_text = data[0], data[1], data[2], data[7]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check("", email_error_text, "no-match")
#     page.close()

# ##Email address do not match
# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en)
# def test_form_page_addresses_do_not_match_gmail_com(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     #page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[6], data[7]
#     webform_obj = Webform(page)
#     action_obj = Action(page)
#     action_obj.closeCookiePopup()
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_page_addresses_do_not_match_gmail_ca(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_page_addresses_do_not_match_hotmail_com(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_page_addresses_do_not_match_hotmail_ca(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_page_addresses_do_not_match_outlook_com(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_page_addresses_do_not_match_outlook_ca(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "no-match")
#     page.close()


# #Form invalid addressess
# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_invalid_addresses_gmail_com(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_invalid_addresses_gmail_ca(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(100000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_invalid_addresses_hotmail_com(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_invalid_addresses_hotmail_ca(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_invalid_addresses_outlook_com(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()

# @pytest.mark.webform
# @pytest.mark.parametrize("url", config.Config.URLs_to_test_en_prod)
# def test_form_invalid_addresses_outlook_ca(url, browser : Browser) -> None:
#     context = browser.new_context(
#         #record_video_dir= "video/"
#     )
#     page = context.new_page()
#     page.set_default_timeout(80000)
#     page.goto(url)
#     data = reader.read_test_data(testdata_form, Action.get_current_test_name())
#     firstname, emailid, verify_email, email_error, email_error_text = data[0], data[1], data[2], data[5], data[6]
#     webform_obj = Webform(page)
#     webform_obj.webform_form(firstname, emailid, verify_email, "", "verify_email")
#     webform_obj.submit_button()
#     webform_obj.email_address_error_check(email_error, email_error_text, "")
#     page.close()