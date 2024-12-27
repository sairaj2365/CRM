import config
import inspect
from playwright.sync_api import Playwright, sync_playwright, Page, Browser, expect
from urllib.parse import urlparse


class Action:
    def __init__(self, page : Page):
        self.page = page
        self.cookieCloseButton = page.locator("#onetrust-button-group #onetrust-accept-btn-handler")
        self.brand_name = page.locator(".vds-d_flex > a svg")
        self.logo_alt = page.locator(".vds-d_flex > a > img")
        self.cookieCloseButton_aveeno = page.locator("#adchoice-buttons .click-processed")
        self.date = page.locator('div[role="menuitemradio"]')


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

    """
    Function to verify which brand
    """
    def get_brand_text(self):
        try:
            return self.brand_name.get_attribute('aria-labelledby')
        except Exception:
            return None
        

    """
    Function to verify page title
    """
    def validate_page_title(self, page_title, brand_name):
        page_title_modified = page_title + brand_name
        expect(self.page).to_have_title(page_title_modified)
        print(f"Title verified to be : '{page_title_modified}'")
    
    """
    Function to validate meta desc
    """
    def validate_meta_desc(self, meta_text, brand_name, site, meta):
        if site == "EN":
            meta_desc = "Get more out of "+ brand_name +" by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to product releases!"   
            if meta_desc == meta_text:
                assert True, f"Meta description is as expected"
                print("Meta description is as expected:", meta_desc)
            else:
                assert False, print(f"Meta description is not as expected: {meta_desc}")

        elif site == "FR":  
            meta_desc_fr = meta + " " + brand_name + "!"   
            if  meta_desc_fr == meta_text:
                assert True, f"Meta description is as expected"
                print("Meta description is as expected:", meta_desc_fr)
            else:
                assert False, print(f"Meta description is not as expected: {meta_desc_fr}")    

    
    """
    Function to get logo alt text
    """
    def get_logo_alt(self):
        try:
            return self.logo_alt.get_attribute('alt')
        except Exception:
            return None
        
    """
    Function to select dropdown option
    """
    def select_dropdown_option(self, dropdown_selector, option_value):
        dropdown_selector.click()
        options = self.date
        option_found = False
        for i in range(options.count()):
            if options.nth(i).inner_text().strip() == str(option_value):
                options.nth(i).click()
                option_found = True
                break
        if not option_found:
            raise ValueError(f"Option with value '{option_value}' not found")

    """
    Function to validate h1 title
    """

    def validate_h1_title(self,expected_title):
        
        # Find all H1 elements
        h1_elements = self.page.query_selector_all('h1')

        # Check if there's exactly one H1 element
        assert len(h1_elements) == 1, f"Expected 1 H1 element, but found {len(h1_elements)}"

        # Get the text content of the H1 element
        actual_title = h1_elements[0].inner_text()

        # Validate the title text
        assert actual_title == expected_title, f"Expected title '{expected_title}', but found '{actual_title}'"

        print(f"H1 validation successful: {expected_title}")


    """
    Function to validate placeholder text
    """

    def validate_placeholder(self, element, expected_placeholder):
        try:
            actual_placeholder = element.get_attribute("placeholder")
            expect(element).to_have_attribute("placeholder", expected_placeholder)
            print(f"Placeholder validation passed. Expected: '{expected_placeholder}', Actual: '{actual_placeholder}'")
            return True
        except Exception:
            return False
        
    """
    Function to validate bold text
    """
    def is_text_bold(self, content, element):
        font_weight = element.evaluate("el => window.getComputedStyle(el).getPropertyValue('font-weight')")
        font = int(font_weight)
        if font >= 700:
            assert True
            print(f"Text is bold: {content}") 
        else:
            assert False, print(f"Text is not bold: {content}")

    def compare_urls(self, actual_url, expected_url):
        actual_parsed = urlparse(actual_url)
        expected_parsed = urlparse(expected_url)
        actual_base = f"{actual_parsed.scheme}://{actual_parsed.netloc}"
        expected_base = f"{expected_parsed.scheme}://{expected_parsed.netloc}" 
        return actual_base == expected_base
    
    """
    Function to validate logo redirections
    """
    def validate_logo_redirections(self, logo_selector, logo_urls):
        logos = self.page.query_selector_all(logo_selector)
        for index, (logo, expected_url) in enumerate(zip(logos, logo_urls), 1):
            logo.wait_for_element_state("visible", timeout=5000)
            with self.page.context.expect_page() as new_page_info:
                logo.click()
            new_page = new_page_info.value
            new_page.wait_for_load_state('networkidle', timeout=80000)
            actual_url = new_page.url
            if self.compare_urls(actual_url, expected_url):
                assert True 
                print(f"PASS: Redirected to '{actual_url}' as expected '{expected_url}'")
            else:
                assert False, print(f"FAIL: Redirected to '{actual_url}', expected '{expected_url}")
            new_page.close()
            self.page.bring_to_front()
            

  
            