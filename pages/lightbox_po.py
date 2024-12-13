import config
# import numpy as np
from playwright.sync_api import Page, expect
from utils.actions import Action
from faker import Faker
# from PIL import Image
# from skimage.metrics import structural_similarity as ssim


class Lightbox:
    
    def __init__(self, page : Page):
        self.page = page
        self.privacy_policy_data_1 = page.locator(".lightbox-warnings p:nth-child(1)")
        self.privacy_policy_data_2 = page.locator(".lightbox-warnings p:nth-child(2)")
        #self.brand_name = page.get_attribute("meta[property='og:title']", "content")
        self.alt_text = page.locator(".vds-max-w_358 img")
        self.alt_text_nicorette = page.locator("#lightbox-form p:nth-child(2) img")
        self.close_icon = page.locator(".vds-self_flex-end svg")
        self.submit = page.locator("button[type='submit']")
        self.first_name = page.locator("input[name='name']")
        self.email = page.locator("input[name='email']")
        self.verify_email = page.locator("input[name='verify-email']")
        self.privacy_policy_data_link = page.locator('p:nth-child(2) a') 
        self.terms_link = page.get_by_role("link", name="full terms and conditions.")
        self.terms_link_fr = page.get_by_role("link", name="conditions générales.")
        self.name_error = page.locator("#radix-\:r9\: div p")
        self.email_error = page.locator("#radix-\:ra\: div p")
        self.verify_email_error_message = page.locator("#radix-\:rb\: div p")
        self.recaptcha_error_message = page.locator("#edit-lightbox div:nth-child(8) .error-required")
        self.name_error_2 = page.locator(".vds-d_grid div:nth-child(1) > span > div > p")
        self.email_error_2 = page.locator(".vds-d_grid div:nth-child(2) > span > div > p")
        self.verify_email_error_message_2 = page.locator(".vds-d_grid div:nth-child(3) > span > div > p")
        self.recaptcha_error_message_2 = page.locator("#edit-lightbox div:nth-child(7) .error-required")
        self.name_error_invalid = page.locator("#edit-lightbox div:nth-child(3) .error-format")
        self.email_error_invalid = page.locator("#edit-lightbox div:nth-child(4) .error-format")
        self.verify_email_error_message_invalid = page.locator("#edit-lightbox div:nth-child(5) .error-format")
        self.recaptcha_error_message_invalid = page.locator("#edit-lightbox .field-recaptcha-error p")
        self.name_error_invalid_2 = page.locator(".vds-d_grid div:nth-child(1) > span > div > p")
        self.email_error_invalid_2 = page.locator(".vds-d_grid div:nth-child(2) > span > div > p")
        self.verify_email_error_message_invalid_2 = page.locator(".vds-d_grid div:nth-child(3) > span > div > p")
        self.verify_email_error_message_invalid_3 = page.locator("//*[@id='radix-:r0:']/div/div[1]/div/div/form/div[2]/div[1]/div[2]/span/div/p")
        self.content_one = page.locator(".brand-text-lightbox")
        self.content_one_1 = page.locator(".vds-flex_column > h2")#care-club-lightbox-title #.lightbox-header #content-main
        self.content_one_2 = page.locator(".lightbox-header h1")
        self.content_two = page.locator(".vds-flex_column> div > p:nth-child(1)")
        self.content_two_1 = page.locator(".lightbox-header p:nth-child(4)")
        self.content_two_2 = page.locator(".lightbox-header p:nth-child(2)")
        self.content_three = page.locator(".vds-d_flex div:nth-child(2) > div > p:nth-child(1)")
        self.privacy_content_two = page.locator(".vds-d_flex div:nth-child(2) > div > p:nth-child(2)")
        self.privacy_content_three = page.locator(".vds-d_flex div:nth-child(2) > div > p:nth-child(3)")
        self.privacy_content_four = page.locator(".vds-d_flex div:nth-child(2) > div > p:nth-child(4)")
        self.alt_text_checkmark = page.locator("#lightbox-thank-you-message p:nth-child(1) img")
        self.content = page.locator("#radix-\:r0\: .vds-items_flex-start")
        self.alt_text_1 = page.locator(".lightbox-header-top img")
        self.lb_form = page.locator(" div:nth-child(10) > div > div.vds-max-h_calc\(100vh_-_token\(spacing\.48\)\)")
        self.req_text = page.locator(".vds-d_flex > div > p:nth-child(2)")
        self.submit_zarbees = page.locator("#edit-submit")
        self.bold_text = page.locator(".care-club-lightbox-subheader strong")
        self.reference_image_path = "reference_image.png"
        self.email_address_error_message = page.locator("#radix-\:r8\: div p")
        self.req_firstname_text = page.locator(".vds-d_grid div:nth-child(1) > label span")
        self.req_email_text = page.locator(".vds-d_grid div:nth-child(2) > label span")
        self.req_verifyemail_text = page.locator(".vds-d_grid div:nth-child(3) > label span")

    """
    Function to verify lightbox image alt tag
    """

    def check_image_alt_tag(self,site_name):
        try:
            alt_text = self.alt_text.get_attribute('alt')
            action_obj = Action(self.page)
            #self.lightbox_displayed(10000)
            text = action_obj.get_brand_text()
            alt = action_obj.get_logo_alt()
            if site_name == "EN":
                if  text==config.Config.tylenol_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.tylenol_alt_text)
                elif text==config.Config.aveeno_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.aveeno_alt_text)
                elif alt==config.Config.zarbees_site_name:              
                    action_obj.validate_alt_text(alt_text, config.Config.zarbees_alt_text)
                elif text==config.Config.nicorette_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.nicorette_alt_text)
                elif text==config.Config.benylin_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.benylin_alt_text)
                elif alt==config.Config.polysporin_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.polysporin_alt_text)
                elif text==config.Config.reactine_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.reactine_alt_text)
                elif alt==config.Config.listerine_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.listerine_alt_text)
                elif text==config.Config.jbaby_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.jbaby_alt_text)
                elif alt==config.Config.bandaid_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.bandaid_alt_text)
                elif text==config.Config.benadryl_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.benadryl_alt_text)
                elif text==config.Config.motrin_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.motrin_alt_text)
                elif text==config.Config.cnc_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.cnc_alt_text)
                elif text==config.Config.imodium_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.imodium_alt_text)
                elif alt==config.Config.nicoderm_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.nicoderm_alt_text)
                elif text==config.Config.penaten_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.penaten_alt_text)
                elif alt==config.Config.pepcid_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.pepcid_alt_text)
                elif text==config.Config.rogaine_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.rogaine_alt_text)
                elif text==config.Config.visine_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.visine_alt_text)
                elif alt==config.Config.sudafed_site_name:
                     action_obj.validate_alt_text(alt_text, config.Config.sudafed_alt_text)
                elif alt==config.Config.neutrogena_site_name:
                     action_obj.validate_alt_text(alt_text, config.Config.neutrogena_alt_text)

            if site_name == "FR":
                if  text==config.Config.tylenol_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.tylenol_alt_text_fr)
                elif text==config.Config.aveeno_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.aveeno_alt_text_fr)
                elif alt==config.Config.zarbees_site_name_fr:
                    action_obj.validate_alt_text(alt_text, config.Config.zarbees_alt_text_fr)
                elif text==config.Config.nicorette_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.nicorette_alt_text_fr)
                elif text==config.Config.benylin_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.benylin_alt_text_fr)
                elif alt==config.Config.polysporin_site_name_fr:
                    action_obj.validate_alt_text(alt_text, config.Config.polysporin_alt_text_fr)
                elif text==config.Config.reactine_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.reactine_alt_text_fr)
                elif alt==config.Config.listerine_site_name_fr:
                    action_obj.validate_alt_text(alt_text, config.Config.listerine_alt_text_fr)
                elif text==config.Config.jbaby_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.jbaby_alt_text_fr)
                elif alt==config.Config.bandaid_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.bandaid_alt_text_fr)
                elif text==config.Config.benadryl_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.benadryl_alt_text_fr)
                elif text==config.Config.motrin_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.motrin_alt_text_fr)
                elif text==config.Config.cnc_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.cnc_alt_text_fr)
                elif text==config.Config.imodium_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.imodium_alt_text_fr)
                elif alt==config.Config.nicoderm_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.nicoderm_alt_text_fr)
                elif text==config.Config.penaten_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.penaten_alt_text_fr)
                elif alt==config.Config.pepcid_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.pepcid_alt_text_fr)
                elif text==config.Config.rogaine_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.rogaine_alt_text_fr)
                elif text==config.Config.visine_site_name:
                    action_obj.validate_alt_text(alt_text, config.Config.visine_alt_text_fr)
                elif alt==config.Config.sudafed_site_name:
                     action_obj.validate_alt_text(alt_text, config.Config.sudafed_alt_text_fr)
                elif alt==config.Config.neutrogena_site_name_fr:
                     action_obj.validate_alt_text(alt_text, config.Config.neutrogena_alt_text_fr)
        except TimeoutError:
            print(f"Text not present or Timeout error.")

    """
    Function to verify close icon alt tag
    """
    def check_close_icon_alt_tag(self,site,alt):
        try:
            alt_text = self.close_icon.get_attribute('aria-label')
            action_obj = Action(self.page)
            if site == "EN":
                #self.page.wait_for_selector()               
                action_obj.validate_alt_text(alt_text, alt)
        
            if site == "FR":
                #self.page.wait_for_selector()
                action_obj.validate_alt_text(alt_text, alt)
        except TimeoutError:
            print("Timeout Error")
    
    """
    Function for submit buttom lightbox
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
    Function for form fields lightbox
    """

    def lightbox_form(self, name, email_id, email_verify, type):
        try:
            #self.page.wait_for_selector("#edit-name")
            #firstname
            self.first_name.fill(name)
            print(f"First Name added : '{name}'")
            
            if type == "recaptcha" or type == "verify_email" or type == 'invalid':
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
        except TimeoutError:
                print(f"Timeout Error") 

    """
    Function to verify links on lightbox
    """   
    def verify_links(self):
        try:
            action_obj = Action(self.page)
            
            #privacy policy
            privacy_policy_en = self.privacy_policy_data_link
            href_link = privacy_policy_en.get_attribute('href')
            privacy_policy_en.click()
            action_obj.new_tab_validate_url(href_link)
            #self.page.wait_for_load_state()
            #self.page.go_back()

            # if sitename == 'EN':
            #     #terms and conditions
            #     terms_link_en = self.terms_link
            #     href_link = terms_link_en.get_attribute('href')
            #     action_obj.new_tab_validate_url(terms_link_en, href_link)

            # elif sitename == 'FR':
            #     #terms and conditions
            #     terms_link_fr = self.terms_link_fr
            #     href_link = terms_link_fr.get_attribute('href')
            #     action_obj.new_tab_validate_url(terms_link_fr, href_link)
        except TimeoutError:
                print(f"Timeout Error")

    """
    Function to verify form error messages for empty fields
    """
    def error_messages_fields(self, name_error, email_error, verify_email_error, recaptcha_error, type):
        try:
            action_obj = Action(self.page)
            #brand = self.brand_name
            if type == 'empty':
                #name
                error_name = self.name_error_2
                action_obj.compare_text(error_name, name_error, "error")

                #email
                error_email = self.email_error_2
                action_obj.compare_text(error_email, email_error, "error")

                #verify email
                error_verify_email = self.verify_email_error_message_2
                action_obj.compare_text(error_verify_email, verify_email_error, "error")

                # #recaptcha
                # error_recaptcha = self.recaptcha_error_message_invalid
                # expect(error_recaptcha).to_have_text(recaptcha_error)
                # print(f"Error message is present and is correct: '{recaptcha_error}'")
            elif type == 'invalid':
                #name
                error_name = self.name_error_invalid_2
                action_obj.compare_text(error_name, name_error, "error")

                #email
                error_email = self.email_error_invalid_2
                action_obj.compare_text(error_email, email_error, "error")

                #verify email
                error_verify_email = self.verify_email_error_message_invalid_2
                action_obj.compare_text(error_verify_email, verify_email_error, "error")

                # #recaptcha
                # error_recaptcha = self.recaptcha_error_message_invalid
                # expect(error_recaptcha).to_have_text(recaptcha_error)
                # print(f"Error message is present and is correct: '{recaptcha_error}'")
        except TimeoutError:
                print(f"Timeout Error")
    
    """
    Function to verify lightbox content
    """
    def verify_lightbox_content(self, site, content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four):
        try:
            #brand = self.brand_name
            action_obj = Action(self.page)
            self.lightbox_displayed(50000)
            # if brand == "AVEENO®" or brand == "Johnson's® Baby":
            #     main_title = self.content_one_1
            #     expect(main_title).to_have_text(content_one)
            #     print(f"Text is present and is correct: '{content_one}'")
            # elif brand == "Quit Smoking with Our Products & Resources | NICORETTE®" or brand == "Johnson & Johnson Canada" or brand == "Polysporin® Canada" or brand == "TYLENOL®" or brand == "Zarbee's® Canada" or brand == "REACTINE®" or brand == "Cessez de fumer avec nos produits et ressources | NICORETTE®":
            #     main_title = self.content_one_1
            #     expect(main_title).to_have_text(content_one)
            #     print(f"Text is present and is correct: '{content_one}'")
            # else:
            main_title = self.content_one_1
            action_obj.compare_text(main_title, content_one,"")
            # if brand == "Quit Smoking with Our Products & Resources | NICORETTE®" or brand == "Cessez de fumer avec nos produits et ressources | NICORETTE®":
            #     textcontent_one = self.content_two_1
            #     expect(textcontent_one).to_have_text(content_two)
            #     print(f"Text is present and is correct: '{content_two}'")
            # elif brand == "Zarbee's® Canada":
            #     textcontent_one = self.content_two_2
            #     expect(textcontent_one).to_have_text(content_two)
            #     print(f"Text is present and is correct: '{content_two}'")
            # else:
            textcontent_one = self.content_two
            action_obj.compare_text(textcontent_one, content_two,"")

            if site == "EN":
                privacy_text_one = self.content_three
                privacy_text = privacy_content_one + "1‑800‑265‑7323."
                action_obj.compare_text(privacy_text_one, privacy_text,"")
            
            elif site == "FR":
                privacy_text_one = self.content_three
                privacy_text = privacy_content_one + "1 800 265‑7323."
                action_obj.compare_text(privacy_text_one, privacy_text,"")

            # if brand == "Johnson & Johnson Canada":
            #     if site == "EN":
            #         privacy_text_two = self.privacy_content_two
            #         expect(privacy_text_two).to_have_text(config.Config.jnj_privacy_data_en_new)
            #         print(f"Text is present and is correct: '{config.Config.jnj_privacy_data_en_new}'")
            #     elif site == "FR":
            #         privacy_text_two = self.privacy_content_two
            #         expect(privacy_text_two).to_have_text(config.Config.jnj_privacy_data_fr_new)
            #         print(f"Text is present and is correct: '{config.Config.jnj_privacy_data_fr_new}'")
            # else:
            privacy_text_two = self.privacy_content_two
            action_obj.compare_text(privacy_text_two, privacy_content_two,"")
            # if brand == "SUDAFED®":
            #     if site == "FR":
            #         privacy_text_three = self.privacy_content_three
            #         expect(privacy_text_three).to_have_text(config.Config.privacy_content_three_sudafed)
            #         print(f"Text is present and is correct: '{privacy_content_three}'")
            # else:
            privacy_text_three = self.privacy_content_three
            action_obj.compare_text(privacy_text_three, privacy_content_three,"")
            # if brand == "SUDAFED®":
            #     if site == "FR":
            #         privacy_text_four = self.privacy_content_four
            #         expect(privacy_text_four).to_have_text(config.Config.privacy_content_four_sudafed_lb)
            #         print(f"Text is present and is correct: '{config.Config.privacy_content_four_sudafed_lb}'")
            # else:
            privacy_text_four = self.privacy_content_four
            action_obj.compare_text(privacy_text_four, privacy_content_four,"")
        except TimeoutError:
                print(f"TimeoutError")

    """
    Function to verify lightbox checkmark alt tag
    """

    def check_checkmark_image_alt_tag(self, alt_tag):
        try:
            alt_text = self.alt_text_checkmark.get_attribute('alt')
            if alt_text == alt_tag:
                assert True
                print(f"Image Alt Text: {alt_text}")
            else:
                assert False, f"Image has no Alt Text."       
        except TimeoutError:
                print(f"Error message not present.")
    
    """
    Function to verify thank you modal content
    """

    def check_thankyou_modal_content(self, content):
        try:
            #self.page.wait_for_selector("#radix-\:r0\: .vds-items_flex-start")
            text_content = self.content
            expect(text_content).to_have_text(content)
            print(f"Text is present and is correct: '{content}'") 
        except TimeoutError:
                print(f"Error message not present.")

    """
    Function to verify "recaptcha" error text
    """
    def recaptcha_error_check(self, recaptcha_error, type):
         try:
            action_obj = Action(self.page)
            if type == "generic":
                #recaptcha
                error_recaptcha = self.recaptcha_error_message
                action_obj.compare_text(error_recaptcha, recaptcha_error,"error")
            elif type == "registered":
                error_recaptcha = self.recaptcha_error_message_2
                action_obj.compare_text(error_recaptcha, recaptcha_error,"error")
         except TimeoutError:
                print(f"Error message not present.")
    
    """
    Function to verify lightbox not present on careclub page
    """
    def lightbox_not_displayed(self):
         try:
            #brand = self.brand_name
            # if brand == "PEPCID® Canada" or brand == "Quit Smoking with Our Products & Resources | NICORETTE®" or brand == "Cessez de fumer avec nos produits et ressources | NICORETTE®" or brand == "REACTINE®" or brand == "TYLENOL®":
            #     lb_form = self.lb_form
            #     expect(lb_form).to_be_visible()
            #     print(f"lightbox should be present or displayed")
            # else:
            lb_form = self.lb_form
            expect(lb_form).not_to_be_visible(timeout=10000)
            print(f"lightbox should not be present or displayed")
         except TimeoutError:
                print(f"Timeout Error")
    
    """
    Function to verify lightbox present on careclub page after 35 seconds
    """
    def lightbox_displayed(self, sec):
         try:
            #brand = self.brand_name
            # if brand == "PEPCID® Canada" or brand == "Quit Smoking with Our Products & Resources | NICORETTE®" or brand == "Cessez de fumer avec nos produits et ressources | NICORETTE®" or brand == "REACTINE®" or brand == "TYLENOL®":
            #     lb_form = self.lb_form
            #     expect(lb_form).to_be_visible()
            #     print(f"lightbox should be present or displayed")
            # else:
            lb_form = self.content_one_1
            expect(lb_form).to_be_visible(timeout=sec)
            print(f"lightbox should be present or displayed")
         except TimeoutError:
                print(f"Timeout Error")
    
    """
    Function to verify lightbox not displayed once closed
    """
    def lightbox_not_displayed_on_close(self):
         try:
            lb_form = self.lb_form
            icon = self.close_icon
            icon.highlight()
            icon.click()
            self.page.reload()
            expect(lb_form).not_to_be_visible()
            print(f"lightbox not present or displayed")
         except TimeoutError:
                print(f"Error message not present.")

    """
    Function to verify lightbox required text
    """
    def verify_lightbox_required_text(self, firstname, email, verifyemail):
        try:
            action_obj = Action(self.page)
            self.lightbox_displayed(50000)

            # req_text = self.req_text
            # action_obj.compare_text(req_text, text_content,"")

            req_firstname_text = self.req_firstname_text
            action_obj.compare_text(req_firstname_text, firstname,"")
            
            req_email_text = self.req_email_text
            action_obj.compare_text(req_email_text, email,"")
            
            req_verifyemail_text = self.req_verifyemail_text
            action_obj.compare_text(req_verifyemail_text, verifyemail,"")
        except TimeoutError:
                print(f"TimeoutError")

    """
    Function to verify "email address" error text
    """
    def email_address_error_check(self, email_error, email_error_text, message):
        try:
            action_obj = Action(self.page)
            #verifyemail
            if message == "no-match":
                error_verifyemail= self.verify_email_error_message_invalid_2
                action_obj.compare_text(error_verifyemail, email_error_text, "error")
            else:
                error_email = self.email_error_invalid_2
                action_obj.compare_text(error_email, email_error, "error")
                
                error_verifyemail= self.verify_email_error_message_invalid_2
                action_obj.compare_text(error_verifyemail, email_error_text, "error")
        except TimeoutError:
            print(f"TimeoutError")

    """
    Function to verify placeholder texts
    """
    def verify_placeholder_text(self, text_firstname, text_email, text_verifyemail):
        action_obj = Action(self.page)
    
        action_obj.validate_placeholder(self.first_name, text_firstname)
        action_obj.validate_placeholder(self.email, text_email)
        action_obj.validate_placeholder(self.verify_email, text_verifyemail)