import config
from playwright.sync_api import Page, expect
from utils.actions import Action
from faker import Faker

class Webform:

    def __init__(self, page : Page):
        self.page = page
        self.card_alt = "section > .vds-d_grid > div:nth-child(2) > div >"
        self.meta_description = page.get_attribute("meta[name='description']", "content")
        self.logo_image = page.locator(".vds-image--ratio_standardHorizontal")
        self.brand_image = page.locator("main > .vds-d_flex img")
        self.href_lang_en = page.locator("link[hreflang = 'en-CA']")
        self.href_lang_fr = page.locator("link[hreflang = 'fr-CA']")
        self.privacy_policy_en_p1 = page.locator(".careclub-form .careclub-warnings p:nth-child(2)")
        self.privacy_policy_en_p2 = page.locator(".careclub-form .careclub-warnings p:nth-child(3)")
        self.privacy_policy_data_link = page.locator('p:nth-child(3) a')
        self.first_name = page.locator("input[name='name']")
        self.email = page.locator("input[name='email']")
        self.verify_email = page.locator("input[name='verify-email']")
        self.birthdate = page.locator("div:nth-child(4) > div > div > div:nth-child(1) button span")
        self.month = page.locator("div:nth-child(4) > div > div > div:nth-child(2) button span")
        self.checkbox = page.locator("#edit-term")
        self.submit = page.locator("button[type='submit']")
        self.name_error = page.locator("div:nth-child(4) > .error-required")
        self.name_error_2 = page.locator("#radix-\:rb\: > div > p")
        self.email_error = page.locator("div:nth-child(5) > .error-required")
        self.email_error_2 = page.locator("#radix-\:rc\: > div > p")
        self.verify_email_error_message = page.locator("div:nth-child(6) > .error-required")
        self.verify_email_error_message_2 = page.locator("#radix-\:rd\: > div > p")
        self.checkbox_error_message_1 = page.locator("#edit-care-club .careclub-term .error-format")
        self.checkbox_error_message_2 = page.locator("div:nth-child(8) > .error-required")
        self.recaptcha_error_message = page.locator(".recaptcha-error")
        self.name_error_invalid = page.locator("div:nth-child(4) > .error-format")
        self.email_error_invalid = page.locator("div:nth-child(5) > .error-format")
        self.verify_email_error_message_invalid = page.locator("div:nth-child(6) > .error-format")
        self.birthdate_error_invalid = page.locator(".field-birthdate .error-format")
        self.name_error_invalid_2 = page.locator(" .vds-grid-cols_1fr > div:nth-child(1) p")
        self.email_error_invalid_2 = page.locator(" .vds-grid-cols_1fr > div:nth-child(2) p")
        self.verify_email_error_message_invalid_2 = page.locator(".vds-grid-cols_1fr > div:nth-child(3) p")
        self.content_three = page.locator("[data-sb-field-path='topHeadline']")
        self.content_two = page.locator("[data-sb-field-path='body']")
        self.content_four = page.locator("[data-sb-field-path='topContent']")
        self.content_six = page.locator("//*[@data-sb-field-path='bottomContent']/p[2]")
        self.page_content_two_4 = page.locator(".main-row.region-row p:nth-child(2)")
        self.dob = page.locator(".field-birthdate em")
        self.dob_fr = page.locator(".field-birthdate i")
        self.content_five = page.locator("//*[@data-sb-field-path='bottomContent']/p[1]")
        self.content_seven = page.locator("//*[@data-sb-field-path='bottomContent']/p[3]")
        self.content_eight = page.locator("//*[@data-sb-field-path='bottomContent']/p[4]")
        self.content_nine = page.locator("//*[@data-sb-field-path='bottomContent']/p[5]")
        self.content_eleven = page.locator("//section[2]/div/div/section/div[1]/div/h2/span")
        self.content_twelve = page.locator("[data-sb-field-path='.content']")
        self.content_twentytwo = page.locator("//section[3]/div/div/section/div[1]/div/h2/span")
        self.recaptcha_error_message_2 = page.locator("#submit-error")
        self.recaptcha_error_message_3 = page.locator("#email-registered-error")
        self.email_address_error_message = page.locator(".vds-grid-cols_1fr > div:nth-child(3) p")
        self.content_one_1 = page.locator("[data-sb-field-path='.headline']")
        self.first_name_text = page.locator(".vds-grid-rows_auto > div:nth-child(1) > label > span")
        self.email_text = page.locator(".vds-grid-rows_auto > div:nth-child(2) > label > span")
        self.verifyemail_text = page.locator(".vds-grid-rows_auto > div:nth-child(3) > label > span")
        self.birthdate_text = page.locator(".vds-grid-rows_auto > div:nth-child(4) > label > span")
        self.logo_tiles = ".vds-mediaWrapper--ratio_standardHorizontal > a"
        

    """
    Function to verify page titles
    """
    def verify_page_title(self, page_title):
        try:
            action_obj = Action(self.page)
            text = action_obj.get_brand_text()
            alt = action_obj.get_logo_alt()
            if text == config.Config.visine_site_name:
                action_obj.validate_page_title(page_title, config.Config.visine_brand_name)
            elif text == config.Config.tylenol_site_name:
                action_obj.validate_page_title(page_title, config.Config.tylenol_brand_name)
            elif alt == config.Config.neutrogena_site_name:
                action_obj.validate_page_title(page_title, config.Config.neutrogena_brand_name)
            elif text == config.Config.reactine_site_name:
               action_obj.validate_page_title(page_title, config.Config.reactine_brand_name)
            elif text == config.Config.nicorette_site_name:
               action_obj.validate_page_title(page_title, config.Config.nicorette_brand_name)
            elif text == config.Config.aveeno_site_name:
                action_obj.validate_page_title(page_title, config.Config.aveeno_brand_name)
            elif alt == config.Config.polysporin_site_name:
               action_obj.validate_page_title(page_title, config.Config.polysporin_brand_name)
            elif text == config.Config.jbaby_site_name:
                action_obj.validate_page_title(page_title, config.Config.jbaby_brand_name)
            elif alt == config.Config.listerine_site_name:
                action_obj.validate_page_title(page_title, config.Config.listerine_brand_name)
            elif text == config.Config.benylin_site_name:
                action_obj.validate_page_title(page_title, config.Config.benylin_brand_name)
            elif text == config.Config.benadryl_site_name:
                action_obj.validate_page_title(page_title, config.Config.benadryl_brand_name)
            elif alt == config.Config.zarbees_site_name:
               action_obj.validate_page_title(page_title, config.Config.zarbees_brand_name)
            elif text == config.Config.motrin_site_name:
               action_obj.validate_page_title(page_title, config.Config.motrin_brand_name)
            elif alt == config.Config.bandaid_site_name:
                action_obj.validate_page_title(page_title, config.Config.bandaid_brand_name)
            elif text == config.Config.rogaine_site_name:
               action_obj.validate_page_title(page_title, config.Config.rogaine_brand_name)
            elif text == config.Config.imodium_site_name:
               action_obj.validate_page_title(page_title, config.Config.imodium_brand_name)
            elif alt == config.Config.nicoderm_site_name:
               action_obj.validate_page_title(page_title, config.Config.nicoderm_brand_name)
            elif alt == config.Config.pepcid_site_name:
               action_obj.validate_page_title(page_title, config.Config.pepcid_brand_name)
            elif text == config.Config.cnc_site_name:
               action_obj.validate_page_title(page_title, config.Config.cnc_brand_name)
            elif text == config.Config.penaten_site_name:
                action_obj.validate_page_title(page_title, config.Config.penaten_brand_name)
            elif text == config.Config.visine_site_name:
              action_obj.validate_page_title(page_title, config.Config.visine_brand_name)
            elif alt == config.Config.sudafed_site_name:
               action_obj.validate_page_title(page_title, config.Config.sudafed_brand_name)
            elif alt == config.Config.listerine_site_name_fr:
               action_obj.validate_page_title(page_title, config.Config.listerine_brand_name)
            elif alt == config.Config.polysporin_site_name_fr:
               action_obj.validate_page_title(page_title, config.Config.polysporin_brand_name)
            elif alt == config.Config.neutrogena_site_name_fr:
               action_obj.validate_page_title(page_title, config.Config.neutrogena_brand_name)
            elif alt == config.Config.zarbees_site_name_fr:
               action_obj.validate_page_title(page_title, config.Config.zarbees_brand_name)
        except TimeoutError:
            print("Page title not verified")

    """
    Function to verify meta description
    """
    def meta_description_check(self, site, meta):
        try:
            action_obj = Action(self.page)
            meta_desc = self.meta_description
            text = action_obj.get_brand_text()
            alt = action_obj.get_logo_alt()
            brand_map = {
                "EN": {
                    config.Config.visine_site_name: config.Config.visine_brand_name,
                    config.Config.tylenol_site_name: config.Config.tylenol_brand_name,
                    config.Config.neutrogena_site_name: config.Config.neutrogena_brand_name,
                    config.Config.reactine_site_name: config.Config.reactine_brand_name,
                    config.Config.nicorette_site_name: config.Config.nicorette_brand_name,
                    config.Config.aveeno_site_name: config.Config.aveeno_brand_name,
                    config.Config.polysporin_site_name: config.Config.polysporin_brand_name,
                    config.Config.jbaby_site_name: config.Config.jbaby_brand_name,
                    config.Config.listerine_site_name: config.Config.listerine_brand_name,
                    config.Config.benylin_site_name: config.Config.benylin_brand_name,
                    config.Config.benadryl_site_name: config.Config.benadryl_brand_name,
                    config.Config.zarbees_site_name: config.Config.zarbees_brand_name,
                    config.Config.motrin_site_name: config.Config.motrin_brand_name,
                    config.Config.bandaid_site_name: config.Config.bandaid_brand_name,
                    config.Config.rogaine_site_name: config.Config.rogaine_brand_name,
                    config.Config.imodium_site_name: config.Config.imodium_brand_name,
                    config.Config.nicoderm_site_name: config.Config.nicoderm_brand_name,
                    config.Config.pepcid_site_name: config.Config.pepcid_brand_name,
                    config.Config.cnc_site_name: config.Config.cnc_brand_name,
                    config.Config.penaten_site_name: config.Config.penaten_brand_name,
                    config.Config.sudafed_site_name: config.Config.sudafed_brand_name
                },
                "FR": {
                    config.Config.visine_site_name: config.Config.visine_brand_name,
                    config.Config.tylenol_site_name: config.Config.tylenol_brand_name,
                    config.Config.neutrogena_site_name_fr: config.Config.neutrogena_brand_name,
                    config.Config.reactine_site_name: config.Config.reactine_brand_name,
                    config.Config.nicorette_site_name: config.Config.nicorette_brand_name,
                    config.Config.aveeno_site_name: config.Config.aveeno_brand_name,
                    config.Config.polysporin_site_name_fr: config.Config.polysporin_brand_name,
                    config.Config.jbaby_site_name: config.Config.jbaby_brand_name,
                    config.Config.listerine_site_name_fr: config.Config.listerine_brand_name,
                    config.Config.benylin_site_name: config.Config.benylin_brand_name,
                    config.Config.benadryl_site_name: config.Config.benadryl_brand_name,
                    config.Config.zarbees_site_name_fr: config.Config.zarbees_brand_name,
                    config.Config.motrin_site_name: config.Config.motrin_brand_name,
                    config.Config.bandaid_site_name: config.Config.bandaid_brand_name,
                    config.Config.rogaine_site_name: config.Config.rogaine_brand_name,
                    config.Config.imodium_site_name: config.Config.imodium_brand_name,
                    config.Config.nicoderm_site_name: config.Config.nicoderm_brand_name,
                    config.Config.pepcid_site_name: config.Config.pepcid_brand_name,
                    config.Config.cnc_site_name: config.Config.cnc_brand_name,
                    config.Config.penaten_site_name: config.Config.penaten_brand_name,
                    config.Config.sudafed_site_name: config.Config.sudafed_brand_name
                }
            }
            site_name = text if text in brand_map[site] else alt
            if site_name in brand_map[site]:
                brand_name = brand_map[site][site_name]
                action_obj.validate_meta_desc(meta_desc, brand_name, site, "" if site == "EN" else meta)
            else:
                print(f"Unknown site name: {site_name}")
        except TimeoutError:
            print("Page title not verified") 

    """
    Function to verify brand image alt tag
    """

    def check_brand_img_alt_tag(self, site_name):
        try:
            alt_text = self.brand_image.get_attribute('alt')
            action_obj = Action(self.page)
            text = action_obj.get_brand_text()
            alt = action_obj.get_logo_alt()
            brand_map = {
                "EN": {
                    "text": {
                        config.Config.tylenol_site_name: config.Config.tylenol_alt_text,
                        config.Config.aveeno_site_name: config.Config.aveeno_alt_text,
                        config.Config.nicorette_site_name: config.Config.nicorette_alt_text,
                        config.Config.benylin_site_name: config.Config.benylin_alt_text,
                        config.Config.reactine_site_name: config.Config.reactine_alt_text,
                        config.Config.jbaby_site_name: config.Config.jbaby_alt_text,
                        config.Config.benadryl_site_name: config.Config.benadryl_alt_text,
                        config.Config.motrin_site_name: config.Config.motrin_alt_text,
                        config.Config.cnc_site_name: config.Config.cnc_alt_text,
                        config.Config.imodium_site_name: config.Config.imodium_alt_text,
                        config.Config.penaten_site_name: config.Config.penaten_alt_text,
                        config.Config.rogaine_site_name: config.Config.rogaine_alt_text,
                        config.Config.visine_site_name: config.Config.visine_alt_text
                    },
                    "alt": {
                        config.Config.zarbees_site_name: config.Config.zarbees_alt_text,
                        config.Config.polysporin_site_name: config.Config.polysporin_alt_text,
                        config.Config.listerine_site_name: config.Config.listerine_alt_text,
                        config.Config.bandaid_site_name: config.Config.bandaid_alt_text,
                        config.Config.nicoderm_site_name: config.Config.nicoderm_alt_text,
                        config.Config.pepcid_site_name: config.Config.pepcid_alt_text,
                        config.Config.sudafed_site_name: config.Config.sudafed_alt_text,
                        config.Config.neutrogena_site_name: config.Config.neutrogena_alt_text
                    }
                },
                "FR": {
                    "text": {
                        config.Config.tylenol_site_name: config.Config.tylenol_alt_text_fr,
                        config.Config.aveeno_site_name: config.Config.aveeno_alt_text_fr,
                        config.Config.nicorette_site_name: config.Config.nicorette_alt_text_fr,
                        config.Config.benylin_site_name: config.Config.benylin_alt_text_fr,
                        config.Config.reactine_site_name: config.Config.reactine_alt_text_fr,
                        config.Config.jbaby_site_name: config.Config.jbaby_alt_text_fr,
                        config.Config.benadryl_site_name: config.Config.benadryl_alt_text_fr,
                        config.Config.motrin_site_name: config.Config.motrin_alt_text_fr,
                        config.Config.cnc_site_name: config.Config.cnc_alt_text_fr,
                        config.Config.imodium_site_name: config.Config.imodium_alt_text_fr,
                        config.Config.penaten_site_name: config.Config.penaten_alt_text_fr,
                        config.Config.rogaine_site_name: config.Config.rogaine_alt_text_fr,
                        config.Config.visine_site_name: config.Config.visine_alt_text_fr
                    },
                    "alt": {
                        config.Config.zarbees_site_name_fr: config.Config.zarbees_alt_text_fr,
                        config.Config.polysporin_site_name_fr: config.Config.polysporin_alt_text_fr,
                        config.Config.listerine_site_name_fr: config.Config.listerine_alt_text_fr,
                        config.Config.bandaid_site_name: config.Config.bandaid_alt_text_fr,
                        config.Config.nicoderm_site_name: config.Config.nicoderm_alt_text_fr,
                        config.Config.pepcid_site_name: config.Config.pepcid_alt_text_fr,
                        config.Config.sudafed_site_name: config.Config.sudafed_alt_text_fr,
                        config.Config.neutrogena_site_name_fr: config.Config.neutrogena_alt_text_fr
                    }
                }
            }
            if text in brand_map[site_name]["text"]:
                expected_alt = brand_map[site_name]["text"][text]
            elif alt in brand_map[site_name]["alt"]:
                expected_alt = brand_map[site_name]["alt"][alt]
            else:
                print(f"Unknown brand: {text or alt}")
                return
            action_obj.validate_alt_text(alt_text, expected_alt)
        except TimeoutError:
            print("Timeout Error")

    """
    Function to verify brand image alt tag
    """

    def check_brand_logo_alt_tag(self, site_name):
        try:
            action_obj = Action(self.page)
            brands = config.Config.brands
            for brand in brands:
                if site_name == "EN":
                    expected_alt = f"{brand} logo"
                    logo_selector = f'img[class*="vds-image"][alt*="{expected_alt}"]'
                    logo_element = self.page.locator(logo_selector)
                    actual_alt = logo_element.get_attribute('alt')
                    action_obj.validate_alt_text(actual_alt, expected_alt) 

                elif site_name == "FR":
                    expected_alt = f"Logo {brand}"
                    logo_selector = f'img[class*="vds-image"][alt*="{expected_alt}"]'
                    logo_element = self.page.locator(logo_selector)
                    actual_alt = logo_element.get_attribute('alt')
                    action_obj.validate_alt_text(actual_alt, expected_alt)                    
        except TimeoutError:
            print("Timeout Error")

    """
    Function to verify card icon alt tags
    """

    def check_card_icon_alt_tag(self, site_name):
        try:
            action_obj = Action(self.page)
            icon_map = {
                "EN": [
                    config.Config.price_icon,
                    config.Config.cash_icon,
                    config.Config.envelope_icon,
                    config.Config.innovation_icon
                ],
                "FR": [
                    config.Config.price_icon_fr,
                    config.Config.cash_icon_fr,
                    config.Config.envelope_icon_fr,
                    config.Config.innovation_icon_fr
                ]
            }
            for i in range(1, 5):
                icon_element = self.page.locator(f"{self.card_alt} div:nth-child({i}) img")
                actual_alt = icon_element.get_attribute('alt')
                expected_alt = icon_map[site_name][i-1]
                action_obj.validate_alt_text(actual_alt, expected_alt)              
        except TimeoutError:
             print("Timeout Error")

    """
    Function to verify href lang
    """
    def check_href_lang(self,site, href):
        if  site == "EN":
            href_text = self.href_lang_en.get_attribute('hreflang')
            if href_text == href:
                assert True
                print(f"href lang text is: {href_text}")
            else:
                assert False, f"href lang text not present."
        
        if  site == "FR":
            href_text = self.href_lang_fr.get_attribute('hreflang')
            if href_text == href:
                assert True
                print(f"href lang text is: {href_text}")
            else:
                assert False, f"href lang text not present."

    """
    Function for form fields
    """
    def webform_form(self, name, email_id, email_verify, date, month, type):
        try:
            action_obj = Action(self.page)
            #brand = self.brand_name
            #firstname
            self.first_name.fill(name)
            print(f"First Name added : '{name}'")

            if type == "recaptcha" or type == "verify_email" or type == 'invalid' or type == 'empty':
                #email
                self.email.fill(email_id)
                print(f"Email id added : '{email_id}'")

                #confirm email
                self.verify_email.fill(email_verify)
                print(f"Verify email id added : '{email_verify}'")
            else:
                #email
                fake = Faker()
                random_email = fake.email()
                self.email.fill(random_email)

                #confirm email
                self.verify_email.fill(random_email)
    
            #birthdate
            if date != "" or month !="":
                action_obj.select_dropdown_option(self.birthdate, date)
                print(f"Date added: {date}")

                action_obj.select_dropdown_option(self.month, month)
                print(f"Date added: {month}")  

            # #checkbox
            # if brand == "NEUTROGENA®":
            #     check_box = self.checkbox_neutrogena
            #     check_box.highlight()
            #     check_box.check()  
            # else:
            #     check_box = self.checkbox
            #     check_box.highlight()
            #     check_box.check()  
        except TimeoutError:
                print(f"Timeout Error")

    """
    Function for submit buttom
    """
    def submit_button(self):
        try:
            #submit
            button = self.submit
            button.highlight()
            button.click()
        except TimeoutError:
                print(f"Timeout Error")
    
    """
    Function to verify form error messages for empty fields
    """
    def error_messages_fields(self, name_error, email_error, verify_email_error, checkbox_birthdate_error, recaptcha_error, type):
        #brand = self.brand_name
        action_obj = Action(self.page)
        if type == 'empty':
            try:
                #name
                error_name = self.name_error_2
                action_obj.compare_text(error_name, name_error, "error")

                #email
                error_email = self.email_error_2
                action_obj.compare_text(error_email, email_error, "error")

                #verify email
                error_verify_email = self.verify_email_error_message_2
                action_obj.compare_text(error_verify_email, verify_email_error, "error")
               
                # #checkbox
                # error_checkbox = self.checkbox_error_message_2
                # expect(error_checkbox).to_have_text(checkbox_birthdate_error)
                # print(f"Error message is present and is correct: '{checkbox_birthdate_error}'")

                # #recaptcha
                # error_recaptcha = self.recaptcha_error_message
                # expect(error_recaptcha).to_have_text(recaptcha_error)
                # print(f"Error message is present and is correct: '{recaptcha_error}'")

            except TimeoutError:
                print(f"Error message not present.")
        
        if type == 'invalid': #need to update locator code
            #brand = self.brand_name
            try:
                #name
                error_name = self.name_error_invalid_2
                action_obj.compare_text(error_name, name_error, "error")

                #email
                error_email = self.email_error_invalid_2
                action_obj.compare_text(error_email, email_error, "error")

                #verify email
                error_verify_email = self.verify_email_error_message_invalid_2
                action_obj.compare_text(error_verify_email, verify_email_error, "error")

                # #birthdate
                # birthdate_error = self.birthdate_error_invalid
                # action_obj.compare_text(birthdate_error, checkbox_birthdate_error, "error")

                # #recaptcha
                # error_recaptcha = self.recaptcha_error_message
                # expect(error_recaptcha).to_have_text(recaptcha_error)
                # print(f"Error message is present and is correct: '{recaptcha_error}'")

            except TimeoutError:
                print(f"Error message not present.")
    
    """
    Function to verify links on webform
    """
    def verify_links(self, site, env):
        action_obj = Action(self.page)
        #logo tiles
        logo_selector = self.logo_tiles
        if site == "EN" and env == "prod":
            action_obj.validate_logo_redirections(logo_selector, config.Config.URLs_en)
        elif site == "EN" and env == "stage":
            action_obj.validate_logo_redirections(logo_selector, config.Config.URLs_en_stage)
        elif site == "FR" and env == "prod":
            action_obj.validate_logo_redirections(logo_selector, config.Config.URLs_fr)
        elif site == "FR" and env == "stage":
            action_obj.validate_logo_redirections(logo_selector, config.Config.URLs_fr_stage)

        #privacy policy
        privacy_policy_en = self.privacy_policy_data_link
        href_link = privacy_policy_en.get_attribute('href')
        privacy_policy_en.click()
        action_obj.new_tab_validate_url( href_link)
        self.page.wait_for_load_state()
    """
    Function to verify webform card content
    """
    def verify_webform_card_content(self, site_name):
        try:
            action_obj = Action(self.page)
            content_map = {
                "EN": [
                    (config.Config.form_content_thirteen, config.Config.form_content_fifteen),
                    (config.Config.form_content_sixteen, config.Config.form_content_seventeen),
                    (config.Config.form_content_eighteen, config.Config.form_content_nineteen),
                    (config.Config.form_content_twenty, config.Config.form_content_twentyone)
                ],
                "FR": [
                    (config.Config.form_content_thirteen_fr, config.Config.form_content_fifteen_fr),
                    (config.Config.form_content_sixteen_fr, config.Config.form_content_seventeen_fr),
                    (config.Config.form_content_eighteen_fr, config.Config.form_content_nineteen_fr),
                    (config.Config.form_content_twenty_fr, config.Config.form_content_twentyone_fr)
                ]
            }
            for i in range(1, 5):
                title = self.page.locator(f"{self.card_alt} div:nth-child({i}) > div:nth-child(2) > div > div > h4")
                content = self.page.locator(f"{self.card_alt} div:nth-child({i}) > div:nth-child(2) > div > div > div")
                title_text, content_text = content_map[site_name][i-1]
                action_obj.compare_text(title, title_text, "")
                action_obj.compare_text(content, content_text, "")            
        except TimeoutError:
             print("Timeout Error")

    """
    Function to verify webform content
    """
    def verify_webform_content(self, site):
        try:
            action_obj = Action(self.page)
            lang_suffix = "_fr" if site == "FR" else ""
            content_map = {
                "content_one_1": f"form_content_one{lang_suffix}",
                "content_two": f"form_content_two{lang_suffix}",
                "content_three": f"form_content_three{lang_suffix}",
                "content_four": f"form_content_four{lang_suffix}",
                "content_five": f"form_content_five{lang_suffix}",
                "content_six": f"form_content_six{lang_suffix}",
                "content_seven": f"form_content_seven{lang_suffix}",
                "content_eight": f"form_content_eight{lang_suffix}",
                "content_nine": f"form_content_nine{lang_suffix}",
                "submit": f"form_content_ten{lang_suffix}",
                "content_eleven": f"form_content_eleven{lang_suffix}",
                "content_twelve": f"form_content_twelve{lang_suffix}",
                "content_twentytwo": f"form_content_twentytwo{lang_suffix}"
            }
            # Validate H1 title
            action_obj.validate_h1_title(getattr(config.Config, f"form_content_one{lang_suffix}"))
            # Compare text for each content element
            for attr, config_attr in content_map.items():
                content_text = getattr(self, attr)
                expected_text = getattr(config.Config, config_attr)
                action_obj.compare_text(content_text, expected_text, "")
            # Uncomment these lines if you want to check for bold text
            # action_obj.is_text_bold(self.content_one, self.content_one_1)
            # action_obj.is_text_bold(self.content_nine, self.content_nine)
        except TimeoutError:
            print("Timeout Error")   

    """
    Function to verify thank you page content
    """
    def verify_thankyou_page_content(self, thank_you_content_one, page_content_two):
        try:
            text = self.brand_name
            main_title = self.content_one
            expect(main_title).to_have_text(thank_you_content_one)
            print(f"Text is present and is correct: '{thank_you_content_one}'")

            if text == "CLEAN & CLEAR® Canada" or text == "SUDAFED®" or text == "BENADRYL®":
                content_two = self.page_content_two_2
                expect(content_two).to_have_text(page_content_two)
                print(f"Text is present and is correct: '{page_content_two}'")
            elif text == "Zarbee's® Canada":
                content_two = self.page_content_two_4
                expect(content_two).to_have_text(page_content_two)
                print(f"Text is present and is correct: '{page_content_two}'")
            else:
                content_two = self.page_content_two
                expect(content_two).to_have_text(page_content_two)
                print(f"Text is present and is correct: '{page_content_two}'")

        except TimeoutError:
                print(f"Error message not present.")


    """
    Function to verify "facultative" text and required field content
    """
    def verify_dob_and_required_field_content(self, text_firstname, text_email, text_verifyemail, text_birthdate):
        action_obj = Action(self.page)

        firstName = self.first_name_text
        action_obj.compare_text(firstName, text_firstname,"")

        email = self.email_text
        action_obj.compare_text(email, text_email,"")

        birthDate = self.birthdate_text
        action_obj.compare_text(birthDate, text_birthdate,"")

        verifyEmail = self.verifyemail_text 
        action_obj.compare_text(verifyEmail, text_verifyemail,"")
    
    """
    Function to verify placeholder texts
    """
    def verify_placeholder_text(self, text_firstname, text_email, text_verifyemail, text_month, text_date):
        action_obj = Action(self.page)
    
        action_obj.validate_placeholder(self.first_name, text_firstname)

        action_obj.validate_placeholder(self.email, text_email)

        action_obj.validate_placeholder(self.verify_email, text_verifyemail)

        action_obj.compare_text(self.birthdate, text_date, "")

        action_obj.compare_text(self.month, text_month, "")

    """
    Function to verify "recaptcha" error text
    """
    def recaptcha_error_check(self, recaptcha_error, type):
         try:
            if type == "generic":
                #recaptcha
                error_recaptcha = self.recaptcha_error_message_2
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")
            elif type == "registered":
                error_recaptcha = self.recaptcha_error_message_3
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")
         except TimeoutError:
                print(f"Error message not present.")

    """
    Function to verify "email address" error text
    """
    def email_address_error_check(self, email_error, email_error_text, message):
         try:
            action_obj = Action(self.page)
            #verifyemail
            if message == "no-match":
                error_verifyemail= self.email_address_error_message
                action_obj.compare_text(error_verifyemail, email_error_text, "error")
            else:
                error_email = self.email_error_invalid_2
                action_obj.compare_text(error_email, email_error, "error")
                
                error_verifyemail= self.verify_email_error_message_invalid_2
                action_obj.compare_text(error_verifyemail, email_error_text, "error")
         except TimeoutError:
                print(f"Error message not present.")              
            
            
    # """
    # Function for cloud page login
    # """
    # def verify_login(self):
    #      try:
    #        self.username.fill(config.Config.username)
    #        self.password.fill(config.Config.password)
    #        self.cloud_page_submit.click()
    #      except TimeoutError:
    #             print(f"Text not present.")
    
            