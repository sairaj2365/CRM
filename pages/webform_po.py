import config
from playwright.sync_api import Page, expect
from utils.actions import Action
from faker import Faker

class Webform:
    jnj_title_text = "Johnson and Johnson Inc."
    jnj_meta_text_fr = "Obtenez-en plus de la part de J&J Canada en devenant membre du Club Bons soins. Recevez des offres et de l'information exclusives directement dans votre boîte de réception, et l'accès à tous les nouveaux produits!"
    jnj_meta_text = "Get more out of JNJ Canada by signing up as a Care Club member. Get exclusive offers & education straight to your inbox with access to all product releases!"
    privacy_policy_data_en_p1 = "Your personal information will be governed by the Privacy Policy Open link in new window and will be used by Johnson & Johnson, Inc. (“Kenvue”), and its third party service providers inside and outside QC & Canada. You consent to the transfer of your data to jurisdictions outside your province and/or country of residence, which may have different data protection rules governing your personal information."
    privacy_policy_data_fr_p1 = "Vos renseignements personnels seront régis par notre Politique de confidentialité Open link in new window et seront utilisés par Johnson & Johnson Inc. (« Kenvue ») et ses tiers fournisseurs de services au Québec, au Canada et à l’étranger. Vous acceptez que vos données soient transférées vers des juridictions situées en dehors de votre province et/ou de votre pays de résidence, où les règles qui régissent la protection de vos renseignements personnels peuvent différer."
    privacy_policy_data_en_p2 = "You may opt-out of receiving emails from us at any time by following the unsubscribe instructions provided in any email message sent to you. Johnson & Johnson Inc., 88 McNabb Street, Markham, ON L3R 5L2, 1‑800‑265‑7323."
    privacy_policy_data_fr_p2 = "Vous pouvez refuser à tout moment de recevoir des courriels de notre part en suivant les instructions de désabonnement fournies dans tout message électronique qui vous est envoyé. Johnson & Johnson Inc., 88 McNabb Street, Markham, ON L3R 5L2, 1 800 265‑7323"


    def __init__(self, page : Page):
        self.page = page
        self.meta_description = page.get_attribute("meta[name='description']", "content")
        self.logo_image = page.locator(".vds-image--ratio_standardHorizontal")
        self.brand_image = page.locator("main > .vds-d_flex img")
        self.href_lang_en = page.locator("link[hreflang = 'en-CA']")
        self.href_lang_fr = page.locator("link[hreflang = 'fr-CA']")
        self.privacy_policy_en_p1 = page.locator(".careclub-form .careclub-warnings p:nth-child(2)")
        self.privacy_policy_en_p2 = page.locator(".careclub-form .careclub-warnings p:nth-child(3)")
        self.privacy_policy_data_link = page.locator('p:nth-child(2) a')
        self.first_name = page.locator("input[name='name']")
        self.email = page.locator("input[name='email']")
        self.verify_email = page.locator("input[name='verify-email']")
        self.birthdate = page.locator(" div:nth-child(4) > div > div > div:nth-child(1) button")
        self.month = page.locator(" div:nth-child(4) > div > div > div:nth-child(2) button")
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
        self.terms_link = page.get_by_role("link", name="full terms and conditions.")
        self.terms_link_fr = page.get_by_role("link", name="conditions générales.")
        self.content_three = page.locator("[data-sb-field-path='topHeadline']")
        self.content_two = page.locator("[data-sb-field-path='body']")
        self.content_four = page.locator(".careclub-term label")
        self.privacy_content_one = page.locator(".careclub-warnings p:nth-child(2)")
        self.privacy_content_two = page.locator(".careclub-warnings p:nth-child(3)")
        self.privacy_content_three = page.locator(".careclub-warnings p:nth-child(4)")
        self.privacy_content_four = page.locator("[data-sb-field-path='topContent']")
        self.content_six = page.locator("//*[@data-sb-field-path='bottomContent']/p[2]")
        self.page_content_two_4 = page.locator(".main-row.region-row p:nth-child(2)")
        self.dob = page.locator(".field-birthdate em")
        self.dob_fr = page.locator(".field-birthdate i")
        self.content_five = page.locator("//*[@data-sb-field-path='bottomContent']/p[1]")
        self.content_seven = page.locator("//*[@data-sb-field-path='bottomContent']/p[3]")
        self.content_eight = page.locator("//*[@data-sb-field-path='bottomContent']/p[4]")
        self.recaptcha_error_message_2 = page.locator("#submit-error")
        self.recaptcha_error_message_3 = page.locator("#email-registered-error")
        self.email_address_error_message = page.locator(".vds-grid-cols_1fr > div:nth-child(3) p")
        self.content_one_1 = page.locator("[data-sb-field-path='.headline']")
        self.content_one_1_benadryl_stage = page.locator(".careclub-header h1")
        self.checkbox_neutrogena = page.locator(".careclub-term label")
        self.first_name_text = page.locator(".vds-grid-rows_auto > div:nth-child(1) > label > span")
        self.email_text = page.locator(".vds-grid-rows_auto > div:nth-child(2) > label > span")
        self.verifyemail_text = page.locator(".vds-grid-rows_auto > div:nth-child(3) > label > span")
        self.birthdate_text = page.locator(".vds-grid-rows_auto > div:nth-child(4) > label > span")
        

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
               action_obj.validate_page_title(page_title, config.Config.sudafed_brand_name)
            elif alt == config.Config.polysporin_site_name_fr:
               action_obj.validate_page_title(page_title, config.Config.sudafed_brand_name)
            elif alt == config.Config.neutrogena_site_name_fr:
               action_obj.validate_page_title(page_title, config.Config.sudafed_brand_name)
            elif alt == config.Config.zarbees_site_name_fr:
               action_obj.validate_page_title(page_title, config.Config.sudafed_brand_name)
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
            if site == "EN":
                if text == config.Config.visine_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.visine_brand_name, site,"")
                elif text == config.Config.tylenol_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.tylenol_brand_name, site,"")
                elif alt == config.Config.neutrogena_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.neutrogena_brand_name, site,"")
                elif text == config.Config.reactine_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.reactine_brand_name, site,"")
                elif text == config.Config.nicorette_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.nicorette_brand_name, site,"")
                elif text == config.Config.aveeno_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.aveeno_brand_name, site,"")
                elif alt == config.Config.polysporin_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.polysporin_brand_name, site,"")
                elif text == config.Config.jbaby_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.jbaby_brand_name, site,"")
                elif alt == config.Config.listerine_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.listerine_brand_name, site,"")
                elif text == config.Config.benylin_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.benylin_brand_name, site,"")
                elif text == config.Config.benadryl_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.benadryl_brand_name, site,"")
                elif alt == config.Config.zarbees_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.zarbees_brand_name, site,"")
                elif text == config.Config.motrin_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.motrin_brand_name, site,"")
                elif alt == config.Config.bandaid_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.bandaid_brand_name, site,"")
                elif text == config.Config.rogaine_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.rogaine_brand_name, site,"")
                elif text == config.Config.imodium_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.imodium_brand_name, site,"")
                elif alt == config.Config.nicoderm_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.nicoderm_brand_name, site,"")
                elif alt == config.Config.pepcid_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.pepcid_brand_name, site,"")
                elif text == config.Config.cnc_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.cnc_brand_name, site,"")
                elif text == config.Config.penaten_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.penaten_brand_name, site,"")
                elif text == config.Config.visine_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.visine_brand_name, site,"")
                elif alt == config.Config.sudafed_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.sudafed_brand_name, site,"")

            elif site == "FR":    
                if text == config.Config.visine_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.visine_brand_name, site, meta)
                elif text == config.Config.tylenol_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.tylenol_brand_name, site, meta)
                elif text == config.Config.neutrogena_site_name_fr:
                    action_obj.validate_meta_desc( meta_desc, config.Config.neutrogena_brand_name, site, meta)
                elif text == config.Config.reactine_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.reactine_brand_name, site, meta)
                elif text == config.Config.nicorette_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.nicorette_brand_name, site, meta)
                elif text == config.Config.aveeno_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.aveeno_brand_name, site, meta)
                elif text == config.Config.polysporin_site_name_fr:
                    action_obj.validate_meta_desc( meta_desc, config.Config.polysporin_brand_name, site, meta)
                elif text == config.Config.jbaby_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.jbaby_brand_name, site, meta)
                elif text == config.Config.listerine_site_name_fr:
                    action_obj.validate_meta_desc( meta_desc, config.Config.listerine_brand_name, site, meta)
                elif text == config.Config.benylin_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.benylin_brand_name, site, meta)
                elif text == config.Config.benadryl_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.benadryl_brand_name, site, meta)
                elif text == config.Config.zarbees_site_name_fr:
                    action_obj.validate_meta_desc( meta_desc, config.Config.zarbees_brand_name, site, meta)
                elif text == config.Config.motrin_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.motrin_brand_name, site, meta)
                elif text == config.Config.bandaid_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.bandaid_brand_name, site, meta)
                elif text == config.Config.rogaine_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.rogaine_brand_name, site, meta)
                elif text == config.Config.imodium_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.imodium_brand_name, site, meta)
                elif text == config.Config.nicoderm_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.nicoderm_brand_name, site, meta)
                elif text == config.Config.pepcid_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.pepcid_brand_name, site, meta)
                elif text == config.Config.cnc_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.cnc_brand_name, site, meta)
                elif text == config.Config.penaten_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.penaten_brand_name, site, meta)
                elif text == config.Config.visine_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.visine_brand_name, site, meta)
                elif text == config.Config.sudafed_site_name:
                    action_obj.validate_meta_desc( meta_desc, config.Config.sudafed_brand_name, site, meta)
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
                    logo_selector = f"img[class*='vds-image'][alt*='{expected_alt}']"
                    logo_element = self.page.locator(logo_selector)
                    actual_alt = logo_element.get_attribute('alt')
                    action_obj.validate_alt_text(actual_alt, expected_alt) 

                elif site_name == "FR":
                    expected_alt = f"Logo {brand}"
                    logo_selector = f"img[class*='vds-image'][alt*='{expected_alt}']"
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
            for i in range(1,5):
                icon_element = self.page.locator(f"section > .vds-d_grid > div:nth-child(2) > div > div:nth-child({i}) img")
                if site_name == "EN":            
                    actual_alt = icon_element.get_attribute('alt')
                    if i==1:
                        action_obj.validate_alt_text(actual_alt, config.Config.price_icon)
                    elif i==2:
                        action_obj.validate_alt_text(actual_alt, config.Config.cash_icon)
                    elif i==3:
                        action_obj.validate_alt_text(actual_alt, config.Config.envelope_icon)
                    elif i==4:
                        action_obj.validate_alt_text(actual_alt, config.Config.innovation_icon)

                elif site_name == "FR":
                    actual_alt = icon_element.get_attribute('alt')
                    if i==1:
                        action_obj.validate_alt_text(actual_alt, config.Config.price_icon_fr)
                    elif i==2:
                        action_obj.validate_alt_text(actual_alt, config.Config.cash_icon_fr)
                    elif i==3:
                        action_obj.validate_alt_text(actual_alt, config.Config.envelope_icon_fr)
                    elif i==4:
                        action_obj.validate_alt_text(actual_alt, config.Config.innovation_icon_fr)              
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

                #birthdate
                birthdate_error = self.birthdate_error_invalid
                action_obj.compare_text(birthdate_error, checkbox_birthdate_error, "error")

                # #recaptcha
                # error_recaptcha = self.recaptcha_error_message
                # expect(error_recaptcha).to_have_text(recaptcha_error)
                # print(f"Error message is present and is correct: '{recaptcha_error}'")

            except TimeoutError:
                print(f"Error message not present.")
    
    """
    Function to verify links on webform
    """
    def verify_links(self):
        action_obj = Action(self.page)
            
        #privacy policy
        privacy_policy_en = self.privacy_policy_data_link
        href_link = privacy_policy_en.get_attribute('href')
        privacy_policy_en.click()
        action_obj.new_tab_validate_url( href_link)
        self.page.wait_for_load_state()
        #self.page.go_back()

        # if sitename == 'EN':
        #     #terms and conditions
        #     terms_link_en = self.terms_link
        #     href_link = terms_link_en.get_attribute('href')
        #     action_obj.new_tab_validate_url(terms_link_en, href_link)

        # if sitename == 'FR':
        #     #terms and conditions
        #     terms_link_fr = self.terms_link_fr
        #     href_link = terms_link_fr.get_attribute('href')
        #     action_obj.new_tab_validate_url(terms_link_fr, href_link)

    """
    Function to verify webform content
    """
    def verify_webform_content(self, site, content_one, content_two, content_three, content_four, content_five, content_six, content_seven, content_eight):
        try:
            action_obj = Action(self.page)
            if site == "EN":
                    main_title = self.content_one_1
                    action_obj.validate_h1_title(content_one)
                    action_obj.compare_text(main_title, content_one,"")

                    content_two_text = self.content_two
                    action_obj.compare_text(content_two_text, content_two,"")

                    content_three_text = self.content_three
                    action_obj.compare_text(content_three_text, content_three,"")

                    content_four_text = self.content_four
                    action_obj.compare_text(content_four_text, content_four,"")

                    content_five_text = self.content_five
                    action_obj.compare_text(content_five_text, content_five,"")

                    content_six_text = self.content_six
                    action_obj.compare_text(content_six_text, content_six,"")

                    content_seven_text = self.content_seven
                    action_obj.compare_text(content_seven_text, content_seven,"")

                    content_eight_text = self.content_eight
                    action_obj.compare_text(content_eight_text, content_eight,"")
        except TimeoutError:
            print(f"Timeout Error")   

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

        # action_obj.validate_placeholder(self.birthdate, text_date)

        # action_obj.validate_placeholder(self.month, text_month)

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
    
            