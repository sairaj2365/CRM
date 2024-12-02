import config
import inspect
from playwright.sync_api import Playwright, sync_playwright, Page, Browser, expect


class Action:
    def __init__(self, page : Page):
        self.page = page
        self.cookieCloseButton = page.locator("#onetrust-button-group #onetrust-accept-btn-handler")
        self.brand_name = page.get_attribute("meta[property='og:title']", "content")
        self.cookieCloseButton_aveeno = page.locator("#adchoice-buttons .click-processed")


    def verify_current_url(self, expected_partial_url):
        try:
            self.page.wait_for_timeout(1000)
            current_url = self.page.url
            assert expected_partial_url in current_url, f"Expected '{expected_partial_url}' to be present in URL, but it is not. Current URL: {current_url}"
            print(f"URL verified to contain : '{current_url}'")
        except TimeoutError:
            print(f"URL did not contain '{current_url}'")

    @classmethod
    def get_current_test_name(cls):
        frame = inspect.currentframe().f_back
        method_name = frame.f_code.co_name
        return method_name
    

    """
    Function to navigate to new tab
    """
    def new_tab_validate_url(self, url):
        # obj.highlight()
        # with self.page.expect_popup() as new:
        #     obj.click()
        #     new_page = new.value
            try:
                if url == config.Config.privacy_policy_link_en:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.terms_condition_link_en:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.privacy_policy_link_fr:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.terms_condition_link_fr:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.privacy_policy_link_fr_jnj:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                elif url == config.Config.privacy_policy_link_en_jnj:
                    assert True
                    print(f"Link navigates to correct url:'{url}'")
                else:
                    #expect(new_page).to_have_url(url)
                    print(f"Link navigates to correct url:'{url}'")
            except TimeoutError:
                print("URL is incorrect")
    

    """
    Function to close cookie pop-up
    """
    def closeCookiePopup(self):
        try:
            button = self.cookieCloseButton #changes on 27/11/24
            button.highlight()
            button.click()
            # text = self.brand_name
            # # if text == "CLEAN & CLEAR® Canada":
            # #     print(f"No cookie banner displayed")
            # # el
            # if text == "Zarbee's® Canada":
            #     #submit
            #     button = self.cookieCloseButton_aveeno
            #     self.page.mouse.down()
            #     button.highlight()
            #     button.click()
            # # if text=="NEUTROGENA®":
            # #     print(f"Cookie banner not present")
            # else:
            #     #submit
            #     button = self.cookieCloseButton #changes on 19/04/24
            #     self.page.mouse.down()
            #     button.highlight()
            #     button.click()          
        except TimeoutError:
                print(f"Timeout Error")

    """
    Function to compare content
    """
    def compare_text(self, text_one, text_two, type):
         try:
            if type == "error":
                expect(text_one).to_have_text(text_two)
                print(f"Error message is present and is correct: '{text_two}'")
            else:
                expect(text_one).to_have_text(text_two)
                print(f"Text is present and is correct: '{text_two}'")
         except TimeoutError:
                print(f"Text/Message not present or displayed")
    
    """
    Function to validate alt text
    """
    def validate_alt_text(self, alt_text, site_alt_text):
        if alt_text == site_alt_text:
            assert True
            print(f"Image Alt Text: {alt_text}")
        else:
            assert False, f"Image has no Alt Text."
    
            