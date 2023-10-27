import config
from playwright.sync_api import Playwright, sync_playwright, Page, BrowserContext, Browser, expect
from utils.actions import Action

class Lightbox:
    
    def __init__(self, page : Page):
        self.page = page
        self.privacy_policy_data_1 = page.locator(".lightbox-warnings p:nth-child(1)")
        self.privacy_policy_data_2 = page.locator(".lightbox-warnings p:nth-child(2)")
        self.brand_name = page.get_attribute("meta[name='apple-mobile-web-app-title']", "content")

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


    



            
            

    
            