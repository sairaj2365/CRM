from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #launch browser
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    #new page
    page = browser.new_page()
    #visit url
    page.goto("https://jjuser:JJJJpassword2022!@con-na-tylenol-ca-en.jnjnab13d6-test.jjc-devops.com/ ")

    #heading
    name="Sign up and earn a reward"
    #heading = page.get_by_role("heading", name)
    heading = page.get_by_text(name, exact=True)
    heading.highlight()

    #input field
    #firstName
    firstName = page.locator("#edit-name")
    firstName.highlight()
    firstName.fill("test")

    #email
    email = page.locator("#edit-email")
    email.highlight()
    email.fill("test@gmail.com")

    #verifyEmail
    verifyEmail = page.locator("#edit-confirm-email")
    verifyEmail.highlight()
    verifyEmail.fill("test@gmail.com")

    #signUp
    signUp = page.get_by_text("Submit")
    signUp.click()


    # #checkbox
    # checkbox = page.get_by_role('checkbox', name = "add name")
    # checkbox.highlight()
    # checkbox.check()

    # #locate alt text
    # altImageText = page.locator("#lightbox-form img")
    # ImageText = altImageText.inner_text()
    

    #locate element
    closeIcon = page.locator("#careclub-lightbox > div > a")
    closeIcon.highlight()
    closeIcon.click()

    #get url
 

    browser.close() 