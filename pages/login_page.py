class LoginPage:

    def __init__(self,page):
        self.page = page
    
    def navigate(self):
        self.page.goto("https://www.hudl.com/login")

    def login(self, email, password):
        self.page.locator('[data-qa-id="email-input"] input').fill(email)
        self.page.locator('button[type="submit"]').click()
        
        self.page.locator('[data-qa-id="password-input"] input').fill(password)
        self.page.locator('button[type="submit"]').click()

    def is_library_visible(self):
        return self.page.locator("text=Library").is_visible()
    
    def is_error_message_visible(self):
        self.page.wait_for_timeout(3000)
        return self.page.locator("text=Incorrect username or password.").is_visible()