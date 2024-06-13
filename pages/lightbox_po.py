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
        self.brand_name = page.get_attribute("meta[name='apple-mobile-web-app-title']", "content")
        self.alt_text = page.locator("#lightbox-form p.rtecenter img")
        self.alt_text_nicorette = page.locator("#lightbox-form p:nth-child(2) img")
        self.close_icon = page.locator("#careclub-lightbox > div > a")
        self.submit = page.locator(".lightbox-fields .form-submit")
        self.first_name = page.locator("#edit-name")
        self.email = page.locator("#edit-email")
        self.verify_email = page.locator("#edit-confirm-email")
        self.privacy_policy_data_link = page.locator('.lightbox-warnings > p:nth-child(2) > a')
        self.terms_link = page.get_by_role("link", name="full terms and conditions.")
        self.terms_link_fr = page.get_by_role("link", name="conditions générales.")
        self.name_error = page.locator("#edit-lightbox div:nth-child(3) .error-required")
        self.email_error = page.locator("#edit-lightbox div:nth-child(4) .error-required")
        self.verify_email_error_message = page.locator("#edit-lightbox div:nth-child(5) .error-required")
        self.recaptcha_error_message = page.locator("#edit-lightbox div:nth-child(8) .error-required")
        self.name_error_2 = page.locator("#edit-lightbox div:nth-child(2) .error-required")
        self.email_error_2 = page.locator("#edit-lightbox div:nth-child(3) .error-required")
        self.verify_email_error_message_2 = page.locator("#edit-lightbox div:nth-child(4) .error-required")
        self.recaptcha_error_message_2 = page.locator("#edit-lightbox div:nth-child(7) .error-required")
        self.name_error_invalid = page.locator("#edit-lightbox div:nth-child(3) .error-format")
        self.email_error_invalid = page.locator("#edit-lightbox div:nth-child(4) .error-format")
        self.verify_email_error_message_invalid = page.locator("#edit-lightbox div:nth-child(5) .error-format")
        self.recaptcha_error_message_invalid = page.locator("#edit-lightbox .field-recaptcha-error p")
        self.name_error_invalid_2 = page.locator("#edit-lightbox div:nth-child(2) .error-format")
        self.email_error_invalid_2 = page.locator("#edit-lightbox div:nth-child(3) .error-format")
        self.verify_email_error_message_invalid_2 = page.locator("#edit-lightbox div:nth-child(4) .error-format")
        self.content_one = page.locator(".brand-text-lightbox")
        self.content_one_1 = page.locator("#care-club-lightbox-title")#care-club-lightbox-title #.lightbox-header #content-main
        self.content_one_2 = page.locator(".lightbox-header h1")
        self.content_two = page.locator(".lightbox-header p:nth-child(3)")
        self.content_two_1 = page.locator(".lightbox-header p:nth-child(4)")
        self.content_two_2 = page.locator(".lightbox-header p:nth-child(2)")
        self.content_three = page.locator(".lightbox-warnings p:nth-child(1)")
        self.privacy_content_two = page.locator(".lightbox-warnings p:nth-child(2)")
        self.privacy_content_three = page.locator(".lightbox-warnings p:nth-child(3)")
        self.privacy_content_four = page.locator(".lightbox-warnings p:nth-child(4)")
        self.alt_text_checkmark = page.locator("#lightbox-thank-you-message p:nth-child(1) img")
        self.content = page.locator("#lightbox-thank-you-message p:nth-child(2)")
        self.alt_text_1 = page.locator(".lightbox-header-top img")
        self.lb_form = page.locator(".lightbox-content")
        self.req_text = page.locator(".lightbox-header p:nth-child(3)")
        self.submit_zarbees = page.locator("#edit-submit")
        self.bold_text = page.locator(".care-club-lightbox-subheader strong")
        self.reference_image_path = "reference_image.png"
        self.email_address_error_message = page.locator(".error-no-match")

    """
    Function to verify privacy policy content
    """

    def check_privacy_policy(self,site_name, data_1, data_2):
        try:
            text = self.brand_name
            if site_name == "EN":
                if text=="Johnson & Johnson Canada":
                    p_text1 = self.privacy_policy_data_1
                    p_text2 = self.privacy_policy_data_2
                    data_2 = data_2 + " 1‑800‑265‑7323."
                    expect(p_text1).to_have_text(config.Config.jnj_privacy_data_en)
                    expect(p_text2).to_have_text(data_2)
                    print(f"Text is present and is correct: '{config.Config.jnj_privacy_data_en + data_2}'")
                else:
                    p_text1 = self.privacy_policy_data_1
                    p_text2 = self.privacy_policy_data_2
                    data_2 = data_2 + " 1‑800‑265‑7323."
                    expect(p_text1).to_have_text(data_1)
                    expect(p_text2).to_have_text(data_2)
                    print(f"Text is present and is correct: '{data_1 + data_2}'")

            if site_name == "FR":
                if text=="Johnson & Johnson Canada":
                    p_text1 = self.privacy_policy_data_1
                    p_text2 = self.privacy_policy_data_2
                    data_2 = data_2 + " 1 800 265‑7323"
                    expect(p_text1).to_have_text(config.Config.jnj_privacy_data_fr)
                    expect(p_text2).to_have_text(data_2)
                    print(f"Text is present and is correct: '{config.Config.jnj_privacy_data_fr + data_2}'")
                else:
                    p_text1 = self.privacy_policy_data_1
                    p_text2 = self.privacy_policy_data_2
                    data_2 = data_2 + " 1 800 265‑7323"
                    expect(p_text1).to_have_text(data_1)
                    expect(p_text2).to_have_text(data_2)
                    print(f"Text is present and is correct: '{data_1 + data_2}'")
        except TimeoutError:
            print(f"Text not present.")


    """
    Function to verify lightbox image alt tag
    """

    def check_image_alt_tag(self,site_name, alt_tag):
        try:
            text = self.brand_name
            if site_name == "EN":
                if text=="TYLENOL®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.tylenol_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="AVEENO®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.aveeno_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Johnson & Johnson Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == alt_tag:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Zarbee's® Canada":
                    alt_text = self.alt_text_1.get_attribute('alt')
                    if alt_text == config.Config.zarbees_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Quit Smoking with Our Products & Resources | NICORETTE®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.nicorette_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="BENYLIN® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.benylin_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Polysporin® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.polysporin_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="REACTINE®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.reactine_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="LISTERINE® Antiseptic Mouthwash, Rinse & Oral Care Products":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.listerine_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Johnson's® Baby":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.jbaby_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="BAND-AID® Brand":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.bandaid_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="BENADRYL®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.benadryl_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Motrin":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.motrin_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="CLEAN & CLEAR® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.cnc_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="IMODIUM®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.imodium_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="NICODERM®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.nicoderm_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="PENATEN® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.penaten_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="PEPCID® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.pepcid_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="ROGAINE® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.rogaine_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="VISINE®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.visine_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="SUDAFED®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.sudafed_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="NEUTROGENA®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.neutrogena_alt_text:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."

            if site_name == "FR":
                if text=="TYLENOL®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.tylenol_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="AVEENO®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.aveeno_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Johnson & Johnson Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == alt_tag:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Zarbee's® Canada":
                    alt_text = self.alt_text_1.get_attribute('alt')
                    if alt_text == config.Config.zarbees_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Cessez de fumer avec nos produits et ressources | NICORETTE®":
                    alt_text = self.alt_text_nicorette.get_attribute('alt')
                    if alt_text == config.Config.nicorette_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="BENYLIN® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.benylin_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Polysporin® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.polysporin_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="REACTINE®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.reactine_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="LISTERINE® Antiseptic Mouthwash, Rinse & Oral Care Products":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.listerine_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Johnson's® Baby":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.jbaby_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Marque BAND-AID®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.bandaid_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="BENADRYL®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.benadryl_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Motrin":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.motrin_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="CLEAN & CLEAR® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.cnc_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="IMODIUM®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.imodium_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="NICODERM®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.nicoderm_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="PENATEN® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.penaten_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="PEPCID® Canada":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.pepcid_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="Rogaine":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.rogaine_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="VISINE®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.visine_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="SUDAFED®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.sudafed_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
                elif text=="NEUTROGENA®":
                    alt_text = self.alt_text.get_attribute('alt')
                    if alt_text == config.Config.neutrogena_alt_text_fr:
                        assert True
                        print(f"Image Alt Text: {alt_text}")
                    else:
                        assert False, f"Image has no Alt Text."
        except TimeoutError:
            print(f"Text not present or Timeout error.")

    """
    Function to verify close icon alt tag
    """
    def check_close_icon_alt_tag(self,site,alt):
        try:
            if site == "EN":
                #self.page.wait_for_selector()
                alt_text = self.close_icon.get_attribute('aria-label')
                print(alt_text)
                if alt_text == alt:
                    assert True
                    print(f"Icon Alt Text: {alt_text}")
                else:
                    assert False, f"Icon has no Alt Text."
        
            if site == "FR":
                #self.page.wait_for_selector()
                alt_text = self.close_icon.get_attribute('aria-label')
                if alt_text == alt:
                    assert True
                    print(f"Icon Alt Text: {alt_text}")
                else:
                    assert False, f"Icon has no Alt Text."
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
            self.page.wait_for_selector("#edit-name")
            #firstname
            self.first_name.fill(name)
            
            if type == "recaptcha" or type == "verify_email" or type == 'invalid':
                #email
                self.email.fill(email_id)

                #confirm email
                self.verify_email.fill(email_verify)
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
    def verify_links(self, sitename):
        try:
            action_obj = Action(self.page)
            
            #privacy policy
            privacy_policy_en = self.privacy_policy_data_link
            href_link = privacy_policy_en.get_attribute('href')
            action_obj.new_tab_validate_url(privacy_policy_en, href_link)
            self.page.wait_for_load_state()
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
            brand = self.brand_name
            if type == 'empty':
                #name
                error_name = self.name_error_2
                expect(error_name).to_have_text(name_error)
                print(f"Error message is present and is correct: '{name_error}'")

                #email
                error_email = self.email_error_2
                expect(error_email).to_have_text(email_error)
                print(f"Error message is present and is correct: '{email_error}'")

                #verify email
                error_verify_email = self.verify_email_error_message_2
                expect(error_verify_email).to_have_text(verify_email_error)
                print(f"Error message is present and is correct: '{verify_email_error}'")

                #recaptcha
                error_recaptcha = self.recaptcha_error_message_invalid
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")
            elif type == 'invalid':
                #name
                error_name = self.name_error_invalid_2
                expect(error_name).to_have_text(name_error)
                print(f"Error message is present and is correct: '{name_error}'")

                #email
                error_email = self.email_error_invalid_2
                expect(error_email).to_have_text(email_error)
                print(f"Error message is present and is correct: '{email_error}'")

                #verify email
                error_verify_email = self.verify_email_error_message_invalid_2
                expect(error_verify_email).to_have_text(verify_email_error)
                print(f"Error message is present and is correct: '{verify_email_error}'")

                #recaptcha
                error_recaptcha = self.recaptcha_error_message_invalid
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")
        except TimeoutError:
                print(f"Timeout Error")
    
    """
    Function to verify lightbox content
    """
    def verify_lightbox_content(self, site, content_one, content_two, privacy_content_one, privacy_content_two, privacy_content_three, privacy_content_four):
        try:
            brand = self.brand_name
            if brand == "AVEENO®" or brand == "Johnson's® Baby":
                main_title = self.content_one_1
                expect(main_title).to_have_text(content_one)
                print(f"Text is present and is correct: '{content_one}'")
            elif brand == "Quit Smoking with Our Products & Resources | NICORETTE®" or brand == "Johnson & Johnson Canada" or brand == "Polysporin® Canada" or brand == "TYLENOL®" or brand == "Zarbee's® Canada" or brand == "REACTINE®" or brand == "Cessez de fumer avec nos produits et ressources | NICORETTE®":
                main_title = self.content_one_1
                expect(main_title).to_have_text(content_one)
                print(f"Text is present and is correct: '{content_one}'")
            else:
                main_title = self.content_one_1
                expect(main_title).to_have_text(content_one)
                print(f"Text is present and is correct: '{content_one}'")

            if brand == "Quit Smoking with Our Products & Resources | NICORETTE®" or brand == "Cessez de fumer avec nos produits et ressources | NICORETTE®":
                textcontent_one = self.content_two_1
                expect(textcontent_one).to_have_text(content_two)
                print(f"Text is present and is correct: '{content_two}'")
            elif brand == "Zarbee's® Canada":
                textcontent_one = self.content_two_2
                expect(textcontent_one).to_have_text(content_two)
                print(f"Text is present and is correct: '{content_two}'")
            else:
                textcontent_one = self.content_two
                expect(textcontent_one).to_have_text(content_two)
                print(f"Text is present and is correct: '{content_two}'")

            if site == "EN":
                privacy_text_one = self.content_three
                privacy_text = privacy_content_one + "1‑800‑265‑7323."
                expect(privacy_text_one).to_have_text(privacy_text)
                print(f"Text is present and is correct: '{privacy_text}'")
            
            elif site == "FR":
                privacy_text_one = self.content_three
                privacy_text = privacy_content_one + "1 800 265‑7323."
                expect(privacy_text_one).to_have_text(privacy_text)
                print(f"Text is present and is correct: '{privacy_text}'")

            if brand == "Johnson & Johnson Canada":
                if site == "EN":
                    privacy_text_two = self.privacy_content_two
                    expect(privacy_text_two).to_have_text(config.Config.jnj_privacy_data_en_new)
                    print(f"Text is present and is correct: '{config.Config.jnj_privacy_data_en_new}'")
                elif site == "FR":
                    privacy_text_two = self.privacy_content_two
                    expect(privacy_text_two).to_have_text(config.Config.jnj_privacy_data_fr_new)
                    print(f"Text is present and is correct: '{config.Config.jnj_privacy_data_fr_new}'")
            else:
                privacy_text_two = self.privacy_content_two
                expect(privacy_text_two).to_have_text(privacy_content_two)
                print(f"Text is present and is correct: '{privacy_content_two}'")

            if brand == "SUDAFED®":
                if site == "FR":
                    privacy_text_three = self.privacy_content_three
                    expect(privacy_text_three).to_have_text(config.Config.privacy_content_three_sudafed)
                    print(f"Text is present and is correct: '{privacy_content_three}'")
            else:
                privacy_text_three = self.privacy_content_three
                expect(privacy_text_three).to_have_text(privacy_content_three)
                print(f"Text is present and is correct: '{privacy_content_three}'")

            if brand == "SUDAFED®":
                if site == "FR":
                    privacy_text_four = self.privacy_content_four
                    expect(privacy_text_four).to_have_text(config.Config.privacy_content_four_sudafed_lb)
                    print(f"Text is present and is correct: '{config.Config.privacy_content_four_sudafed_lb}'")
            else:
                privacy_text_four = self.privacy_content_four
                expect(privacy_text_four).to_have_text(privacy_content_four)
                print(f"Text is present and is correct: '{privacy_content_four}'")
        except TimeoutError:
                print(f"Error message not present.")

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
            if type == "generic":
                #recaptcha
                error_recaptcha = self.recaptcha_error_message
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")
            elif type == "registered":
                error_recaptcha = self.recaptcha_error_message_2
                expect(error_recaptcha).to_have_text(recaptcha_error)
                print(f"Error message is present and is correct: '{recaptcha_error}'")
         except TimeoutError:
                print(f"Error message not present.")
    
    """
    Function to verify lightbox not present on careclub page
    """
    def lightbox_not_displayed(self):
         try:
            brand = self.brand_name
            # if brand == "PEPCID® Canada" or brand == "Quit Smoking with Our Products & Resources | NICORETTE®" or brand == "Cessez de fumer avec nos produits et ressources | NICORETTE®" or brand == "REACTINE®" or brand == "TYLENOL®":
            #     lb_form = self.lb_form
            #     expect(lb_form).to_be_visible()
            #     print(f"lightbox should be present or displayed")
            # else:
            lb_form = self.lb_form
            expect(lb_form).not_to_be_visible()
            print(f"lightbox should not be present or displayed")
         except TimeoutError:
                print(f"Timeout Error")
    
    """
    Function to verify lightbox present on careclub page after 35 seconds
    """
    def lightbox_displayed(self, sec):
         try:
            brand = self.brand_name
            # if brand == "PEPCID® Canada" or brand == "Quit Smoking with Our Products & Resources | NICORETTE®" or brand == "Cessez de fumer avec nos produits et ressources | NICORETTE®" or brand == "REACTINE®" or brand == "TYLENOL®":
            #     lb_form = self.lb_form
            #     expect(lb_form).to_be_visible()
            #     print(f"lightbox should be present or displayed")
            # else:
            lb_form = self.lb_form
            self.page.wait_for_selector(".lightbox-content", timeout=sec)
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
    def verify_lightbox_required_text(self, text_content):
         try:
            req_text = self.req_text
            expect(req_text).to_have_text(text_content)
            print(f"Text is present and is correct: '{text_content}'")
         except TimeoutError:
                print(f"Text not present.")

    """
    Function to verify "email address" error text
    """
    def email_address_error_check(self, email_error, email_error_text, message):
         try:
            error_email = self.verify_email_error_message_invalid_2
            expect(error_email).to_have_text(email_error)
            print(f"Error message is present and is correct: '{email_error}'")
            #verifyemail
            if message == "no-match":
                error_verifyemail= self.email_address_error_message
                expect(error_verifyemail).to_have_text(email_error_text)
                print(f"Error message is present and is correct: '{email_error_text}'")
            else:
                error_verifyemail= self.verify_email_error_message_invalid_2
                expect(error_verifyemail).to_have_text(email_error_text)
                print(f"Error message is present and is correct: '{email_error_text}'")
         except TimeoutError:
                print(f"Error message not present.")      

    # """
    # Function for visual checks
    # """
    # def verify_bold_text(self):
    #     bold_element = self.bold_text
    #     if bold_element:
    #         # Scroll to the element to ensure it's visible
    #         bold_element.scroll_into_view_if_needed()

    #         # Capture a screenshot of the specific element containing the bold text
    #         bold_element.screenshot(path="screenshot.png")
    #         screenshot_path = "screenshot.png"

    #         # Open the images
    #         image1 = Image.open(screenshot_path)
    #         image2 = Image.open(self.reference_image_path)

    #         mask=None

    #         # Convert images to grayscale
    #         image1_gray = image1.convert("L")
    #         image2_gray = image2.convert("L")

    #         # Resize images if they are too small
    #         min_dimension = min(image1.size[0], image1.size[1], image2.size[0], image2.size[1])
    #         min_dimension_threshold = 7  # Adjust this value as needed
    #         if min_dimension < min_dimension_threshold:
    #             resize_factor = min_dimension_threshold / min_dimension
    #             new_size = (int(image1.size[0] * resize_factor), int(image1.size[1] * resize_factor))
    #             image1 = image1.resize(new_size, Image.ANTIALIAS)
    #             image2 = image2.resize(new_size, Image.ANTIALIAS)

    #         if mask is not None:
    #             image1_array = np.array(image1_gray)
    #             image2_array = np.array(image2_gray)
    #             image1_array[mask] = 255
    #             image2_array[mask] = 255
    #             image1_gray = Image.fromarray(image1_array)
    #             image2_gray = Image.fromarray(image2_array)

    #         # Calculate structural similarity index
    #         # Compare the captured screenshot with the reference image
    #         win_size = 7  # Adjust this value as needed
    #         similarity_index = ssim(np.array(image1), np.array(image2), win_size=win_size)

    #         print(f"Similarity Index: {similarity_index}")

    #         if similarity_index > 0.95:  # Adjust the threshold as needed
    #             print("Bold text matches with reference image.")
    #         else:
    #             print("Bold text does not match with reference image.")
    #     else:
    #         print("Bold element not found!")
        